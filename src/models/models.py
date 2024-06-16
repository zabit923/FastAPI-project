from datetime import datetime

from sqlalchemy import MetaData, Integer, String, TIMESTAMP, ForeignKey, Table, Column, JSON


metadata = MetaData()


roles = Table(
    'roles',
    metadata,
    Column('id', Integer, unique=True, primary_key=True, autoincrement=True),
    Column('name', String, nullable=False),
    Column('permissions', JSON),
)

users = Table(
    'users',
    metadata,
    Column('id', Integer, unique=True, primary_key=True, autoincrement=True),
    Column('email', String, nullable=False),
    Column('username', String, unique=True, nullable=False),
    Column('password', String, nullable=False),
    Column('registered_at', TIMESTAMP, default=datetime.utcnow),
    Column('role_id', Integer, ForeignKey('roles.id')),
)
