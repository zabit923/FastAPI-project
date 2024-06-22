from redis import asyncio as aioredis
from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from auth.base_config import fastapi_users, auth_backend
from auth.schemas import UserRead, UserCreate

from operations.router import router as operation_router
from tasks.router import router as tasks_router


app = FastAPI(
    title='College-messanger'
)


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/api/v1/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/api/v1/auth",
    tags=["auth"],
)

app.include_router(operation_router)
app.include_router(tasks_router)


@app.on_event('startup')
async def startup_event():
    redis = aioredis.from_url('redis://localhost', encoding='utf8', decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix='fastapi-cache')
