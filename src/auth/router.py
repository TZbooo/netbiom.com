from fastapi import APIRouter, HTTPException, status
from pymongo.errors import DuplicateKeyError

from src.config import HOST
from src.account.schemas import (
    UserCreate,
    UserSignIn,
    UserOut,
    UserAuthToken
)
from src.account.service import (
    create_user,
    confirm_email_by_email_confirmation_token,
    get_user_by_username,
)
from src.auth.service import Hasher, send_email


router = APIRouter(
    prefix='/auth',
    tags=['auth']
)


@router.get('/confirm-email/{email_confirmation_token}')
async def confirm_email(email_confirmation_token: str) -> UserOut:
    user = await confirm_email_by_email_confirmation_token(
        email_confirmation_token
    )
    return user


@router.post('/signup')
async def signup(user_data: UserCreate) -> UserAuthToken:
    try:
        new_user = await create_user(
            user_data.username,
            user_data.email,
            user_data.password
        )
        message = HOST + router.url_path_for(
            'confirm_email',
            email_confirmation_token=new_user.email_confirmation_token
        )
        send_email(
            recipient=new_user.email,
            message=message
        )
        return new_user
    except DuplicateKeyError:
        raise HTTPException(
            status.HTTP_409_CONFLICT,
            'username or email already exists'
        )


@router.get('/token')
async def get_auth_token(user_data: UserSignIn) -> UserAuthToken:
    user = await get_user_by_username(user_data.username)
    if user is not None and Hasher.verify_password(user_data.password, user.password):
        return user

    raise HTTPException(
        status.HTTP_401_UNAUTHORIZED,
        'username or password is wrong'
    )
