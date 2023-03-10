from fastapi import APIRouter, Depends

from src.account.models import User
from src.account.dependencies import get_current_user
from src.page.schemas import PageCreate
from src.page.service import create_page


router = APIRouter(
    prefix='/page',
    tags=['page']
)


@router.post('/')
async def add_page(
    page: PageCreate,
    current_user: User = Depends(get_current_user)
) -> User:
    current_user = await create_page(
        current_user,
        page
    )
    return current_user
