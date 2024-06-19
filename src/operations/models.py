from sqlalchemy import Column, Integer, String, TIMESTAMP, MetaData
from sqlalchemy.orm import DeclarativeMeta, declarative_base


metadata = MetaData()
Base: DeclarativeMeta = declarative_base(metadata=metadata)


class Operation(Base):
    __tablename__ = 'operation'
    id = Column(Integer, primary_key=True, autoincrement=True)
    quantity = Column(String)
    figi = Column(String)
    instrument_type = Column(String, nullable=True)
    date = Column(TIMESTAMP)
    type = Column(String)
