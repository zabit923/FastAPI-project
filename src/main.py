from datetime import datetime
from enum import Enum
from typing import List, Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI(
    title='College-messanger'
)


users = [
    {'id': 1, 'role': 'user1', 'name': 'Maga1', 'degree': [
        {'id': 1, 'created_at': '2024-04-06T04:05:00', 'type_degree': 'expert'}
    ]},
    {'id': 2, 'role': 'user2', 'name': 'Maga2', 'degree': [
        {'id': 1, 'created_at': '2024-04-06T04:05:00', 'type_degree': 'expert'}
    ]},
    {'id': 3, 'role': 'user3', 'name': 'Maga3', 'degree': [
        {'id': 1, 'created_at': '2024-04-06T04:05:00', 'type_degree': 'expert'}
    ]},
]

fake_trades = [
    {'id': 1, 'user_id': 1, 'currency': 'BTC', 'side': 'buy', 'price': 123, 'amount': 123},
    {'id': 2, 'user_id': 2, 'currency': 'ETH', 'side': 'sell', 'price': 321, 'amount': 321}
]


class DegreeType(Enum):
    newbie = 'newbie'
    expert = 'expert'


class Degree(BaseModel):
    id: int
    created_at: datetime
    type_degree: DegreeType


class User(BaseModel):
    id: int
    role: str
    name: str
    degree: Optional[List[Degree]]


@app.get('/users/{user_id}', response_model=List[User])
def get_users(user_id: int):
    return [user for user in users if user.get('id') == user_id]


class Trade(BaseModel):
    id: int
    user_id: int
    currency: str = Field(max_length=10)
    side: str
    price: int = Field(ge=0)
    amount: int


@app.post('/trades')
def add_trades(trades: List[Trade]):
    fake_trades.extend(trades)
    return {
        'status': 200,
        'data': fake_trades
    }
