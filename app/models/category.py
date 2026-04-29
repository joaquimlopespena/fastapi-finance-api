from core.config import settings
from sqlalchemy import Column, DateTime, Integer, String
from datetime import UTC, datetime

class Category(settings.DBBaseModel):
    __tablename__ = "categories"

    id: Column[int] = Column(Integer, primary_key=True, autoincrement=True)
    name: Column[str] = Column(String(length=100), nullable=True)
    created_at: Column[datetime] = Column(DateTime(timezone=True), default=datetime.now(UTC))
