from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.category import Category

class CategoryRepository:
    def __init__(self, db: AsyncSession) -> None:
        self.db = db

    async def create(self, category: Category) -> Category:
        self.db.add(category)
        try:
            await self.db.commit()
            await self.db.refresh(category)
            return category
        except Exception:
            await self.db.rollback()
            raise

    async def get_all(self) -> list[Category]:
        result = await self.db.execute(select(Category))
        categories = result.scalars().all()
        return categories

    async def get_by_id(self, category_id: int) -> Category | None:
        result = await self.db.execute(select(Category).where(Category.id == category_id))
        return result.scalars().first()

    async def update(self, category: Category) -> Category:
        self.db.merge(category)
        try:
            await self.db.commit()
            await self.db.refresh(category)
            return category
        except Exception:
            await self.db.rollback()
            raise

    async def delete(self, category: Category) -> None:
        await self.db.delete(category)

        try:
            await self.db.commit()
        except Exception:
            await self.db.rollback()
            raise