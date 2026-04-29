from datetime import UTC, datetime
from typing import Optional
from pydantic import BaseModel as SCBaseModel, Field

class CategoryCreate(SCBaseModel):
    id: Optional[int] = Field(None, description="ID da categoria")
    name: str = Field(..., description="Nome da categoria")

    class Config:
        orm_mode = True 

class CategoryResponse(CategoryCreate):
    id: int = Field(..., description="ID da categoria")
    name: str = Field(..., description="Nome da categoria")
    created_at: datetime = Field(default_factory=datetime.now(UTC))
    updated_at: datetime = Field(default_factory=datetime.now(UTC)) 

class CategoryUpdate(CategoryCreate):
    name: Optional[str] = Field(None, description="Nome da categoria")
    updated_at: datetime = Field(default_factory=datetime.now(UTC))
