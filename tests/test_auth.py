import pytest
from sqlalchemy import insert, select

from auth.models import Role
from conftest import async_session_maker, client


@pytest.mark.asyncio
async def test_add_role():
    async with async_session_maker() as session:
        stmt = insert(Role).values(id=1, name='Admin', permissions=None)
        await session.execute(stmt)
        await session.commit()

        query = select(Role)
        result = await session.execute(query)
        role = result.scalars().all()[0]
        assert (role.id, role.name, role.permissions) == (1, 'Admin', None), 'Роль не добавилась.'


test_user = {
  "email": "test@gmail.com",
  "password": "Test123321",
  "is_active": True,
  "is_superuser": False,
  "is_verified": False,
  "username": "Test",
  "role_id": 1
}


@pytest.mark.asyncio
async def test_register():
    response = client.post('/api/v1/auth/register', json=test_user)

    assert response.status_code == 201
    assert response.json()['email'] == test_user['email']
