from beanie import Document, Indexed
from pydantic import Field, EmailStr

from src.service import get_hex_uuid
from src.page.schemas import PageModel


class User(Document):
    username: Indexed(str, unique=True)
    email: Indexed(EmailStr, unique=True)
    email_is_confirmed: bool = False
    password: str

    auth_token: str = Field(default_factory=get_hex_uuid)
    email_confirmation_token: str = Field(default_factory=get_hex_uuid)

    pages: list[PageModel]
