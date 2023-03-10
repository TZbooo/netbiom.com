from fastapi import Request, HTTPException, status

from src.account.models import User
from src.account.service import get_user_by_auth_token


async def get_current_user(request: Request) -> User:
    auth_token = request.headers['Web-Panel-Token']
    current_user = await get_user_by_auth_token(auth_token)
    if current_user is None:
        raise HTTPException(
            status.HTTP_401_UNAUTHORIZED,
            'token is wrong'
        )
    return current_user
