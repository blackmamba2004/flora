from sqlalchemy import insert, select, delete, func

from app.base.schemas import BaseSchema
from app.database import async_session_maker, Base


class BaseDAO:
    model: Base = None

    # @classmethod
    # async def create(cls, **data):
    #     async with async_session_maker() as session:
    #         query = (
    #             insert(cls.model)
    #             .values(**data)
    #             .returning(cls.model)
    #         )
    #         result = await session.execute(query)
    #         await session.commit()
    #         return result.scalar_one_or_none()

    @classmethod
    async def create(cls, data: BaseSchema):
        async with async_session_maker() as session:
            data_obj = cls.model(**data.model_dump())
            session.add(data_obj)
            await session.commit()
            return data_obj

    @classmethod
    async def filter(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar_one_or_none()
    
    @classmethod
    async def find_all_by_filter(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalars()
        
    @classmethod
    async def destroy_all(cls):
        async with async_session_maker() as session:
            query = delete(cls.model)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def count(cls):
        async with async_session_maker() as session:
            query = select(func.count("*")).select_from(cls.model)
            count = await session.execute(query)
            return count.scalar()
