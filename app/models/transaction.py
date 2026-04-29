from core.config import settings
from sqlalchemy import Column, DateTime, Integer, String
from datetime import UTC, datetime

class Transaction(settings.DBBaseModel):
    __tablename__ = "transactions"

    id: Column[int] = Column(Integer, primary_key=True, autoincrement=True)
    category_id: Column[int] = Column(Integer, nullable=True)
    description: Column[str] = Column(String(length=255), nullable=True)
    amount: Column[float] = Column(Float, nullable=True)
    transaction_date: Column[datetime] = Column(DateTime(timezone=True), nullable=True)
    created_at: Column[datetime] = Column(DateTime(timezone=True), default=datetime.now(UTC))
    updated_at: Column[datetime] = Column(DateTime(timezone=True), default=datetime.now(UTC))
