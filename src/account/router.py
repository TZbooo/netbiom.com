from fastapi import APIRouter, Depends

from src.account.models import User
from src.account.schemas import UserOut
from src.account.dependencies import get_current_user
from src.account.service import change_user_password


router = APIRouter(
    prefix='/account',
    tags=['account']
)


@router.get('/me')
async def get_me(current_user: User = Depends(get_current_user)) -> UserOut:
    return current_user


@router.patch('/me/username')
async def change_username(
    username: str,
    current_user: User = Depends(get_current_user)
) -> UserOut:
    current_user.username = username
    await current_user.save()
    return current_user


@router.patch('/me/password')
async def change_password(
    password: str,
    current_user: User = Depends(get_current_user)
) -> UserOut:
    current_user = await change_user_password(
        current_user,
        password
    )
    return current_user
