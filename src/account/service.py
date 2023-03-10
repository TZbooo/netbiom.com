from src.account.models import User
from src.auth.service import Hasher


async def create_user(username: str, email: str, password: str) -> User:
    password_hash = Hasher.get_password_hash(password)
    new_user = User(
        username=username,
        email=email,
        password=password_hash
    )
    await new_user.insert()
    return new_user


async def confirm_email_by_email_confirmation_token(
        email_confirmation_token: str
) -> bool:
    user = await User.find_one(
        User.email_confirmation_token == email_confirmation_token
    )
    await user.set({User.email_is_confirmed: True})
    return user


async def get_user_by_username(username: str) -> User:
    return await User.find_one(
        User.username == username
    )


async def get_user_by_auth_token(auth_token: str) -> User:
    return await User.find_one(
        User.auth_token == auth_token
    )


async def change_user_password(user: User, new_password: str) -> User:
    user.password = Hasher.get_password_hash(new_password)
    await user.save()
    return user
