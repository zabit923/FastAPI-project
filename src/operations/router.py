from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from .models import Operation
from .schemas import OperationCreate


router = APIRouter(
    prefix="/operations",
    tags=["Operation"]
)


@router.get("")
async def get_specific_operations(operation_type: str, session: AsyncSession = Depends(get_async_session)):
    query = select(Operation).where(Operation.type == operation_type)
    result = await session.execute(query)
    return {
        "status": "success",
        "data": result.scalars().all(),
        "details": None
    }


@router.post("")
async def add_specific_operations(new_operation: OperationCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Operation).values(**new_operation.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}
