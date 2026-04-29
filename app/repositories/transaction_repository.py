from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.transaction import Transaction

class TransactionRepository:
    def __init__(self, db: AsyncSession) -> None:
        self.db = db

    async def create(self, transaction: Transaction) -> Transaction:
        self.db.add(transaction)
        await self.db.commit()
        await self.db.refresh(transaction)
        return transaction

    async def get_all(self) -> list[Transaction]:
        result = await self.db.execute(select(Transaction))
        return result.scalars().all()

    async def get_by_id(self, transaction_id: int) -> Transaction:
        result = await self.db.execute(select(Transaction).where(Transaction.id == transaction_id))
        return result.scalars().first()

    async def update(self, transaction: Transaction) -> Transaction:
        self.db.add(transaction)
        await self.db.commit()
        await self.db.refresh(transaction)
        return transaction

    async def delete(self, transaction: Transaction) -> None:
        await self.db.delete(transaction)
        await self.db.commit()
