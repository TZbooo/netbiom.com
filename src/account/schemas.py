from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    email: EmailStr
    password: str


class UserSignIn(UserBase):
    password: str


class UserOut(UserBase):
    email: EmailStr
    email_is_confirmed: bool


class UserAuthToken(BaseModel):
    auth_token: str
