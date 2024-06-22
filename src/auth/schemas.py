from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    id: int
    username: str
    email: str
    role_id: int


class UserCreate(schemas.BaseUserCreate):
    username: str
    email: str
    role_id: int
