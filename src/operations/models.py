from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.orm import DeclarativeMeta, declarative_base

from src.database import metadata


Base: DeclarativeMeta = declarative_base(metadata=metadata)


class Operation(Base):
    __tablename__ = 'operation'
    id = Column(Integer, primary_key=True, autoincrement=True)
    quantity = Column(String)
    figi = Column(String)
    instrument_type = Column(String, nullable=True)
    date = Column(TIMESTAMP)
    type = Column(String)
