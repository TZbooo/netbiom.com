from fastapi import FastAPI

from src.database import init_db
from src.auth.router import router as auth_router
from src.account.router import router as account_router
from src.page.router import router as page_router


app = FastAPI()
app.include_router(auth_router)
app.include_router(account_router)
app.include_router(page_router)


@app.on_event('startup')
async def startup():
    await init_db()
