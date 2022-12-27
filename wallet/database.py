from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.util._compat_py3k import asynccontextmanager

Base = declarative_base()

engine = create_async_engine(
    'sqlite+aiosqlite:///base.db',
    future=True,
)


async def create_base():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


def async_session_generator():
    return sessionmaker(
        engine, class_=AsyncSession
    )


@asynccontextmanager
async def get_session():
    try:
        async_session = async_session_generator()

        async with async_session() as session:
            yield session
    except Exception:
        await session.rollback()
        raise
    finally:
        await session.close()


