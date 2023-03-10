import motor
from beanie import init_beanie

from src.config import MONGODB_URL
from src.account.models import User


async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
    db = client.web_panel
    await init_beanie(
        db,
        document_models=[
            User
        ]
    )
