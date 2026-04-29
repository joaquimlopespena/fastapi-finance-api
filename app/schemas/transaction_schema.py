from datetime import UTC, datetime
from typing import Optional
from pydantic import BaseModel as SCBaseModel, Field

class TransactionCreate(SCBaseModel):
    category_id: int = Field(..., description="ID da categoria")
    description: str = Field(..., description="Descrição da transação")
    amount: float = Field(..., description="Valor da transação")
    transaction_date: datetime = Field(..., description="Data da transação")

    class Config:
        orm_mode = True 

class TransactionResponse(TransactionCreate):
    id: int = Field(..., description="ID da transação")
    category_id: int = Field(..., description="ID da categoria")
    description: str = Field(..., description="Descrição da transação")
    amount: float = Field(..., description="Valor da transação")
    transaction_date: datetime = Field(..., description="Data da transação")
    created_at: datetime = Field(default_factory=datetime.now(UTC))
    updated_at: datetime = Field(default_factory=datetime.now(UTC)) 

    class Config:
        orm_mode = True 


class TransactionUpdate(TransactionCreate):
    category_id: Optional[int] = Field(None, description="ID da categoria")
    description: Optional[str] = Field(None, description="Descrição da transação")
    amount: Optional[float] = Field(None, description="Valor da transação")
    transaction_date: Optional[datetime] = Field(None, description="Data da transação")
    updated_at: datetime = Field(default_factory=datetime.now(UTC)) 

    class Config:
        orm_mode = True 

