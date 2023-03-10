from src.account.models import User
from src.page.schemas import PageCreate


async def create_page(user: User, page: PageCreate) -> User:
    user.pages.append(page)
    await user.save()
    return user
