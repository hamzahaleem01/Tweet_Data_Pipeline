from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker


class DBconnector:
    """Sets up asynchronous connection to a database base on given environment settings."""

    __db_url: str
    __engine: AsyncEngine
    async_session_factory: sessionmaker[AsyncSession]  # type: ignore

    def __init__(
        self,
        DB_HOST: str,
        DB_NAME: str,
        DB_USER: str,
        DB_PASSWORD: str,
        DB_PORT: str,
    ):
        """Initialize asynchronous engine, s.t. asynchronous may be created using the async_session_factory."""
        self.DB_HOST = DB_HOST
        self.DB_NAME = DB_NAME
        self.DB_USER = DB_USER
        self.DB_PASSWORD = DB_PASSWORD
        self.DB_PORT = DB_PORT
        self.__db_url = (
            f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}"
            + f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )
        self.__engine = create_async_engine(self.__db_url, echo=False, echo_pool=False)
        self.async_session_factory = sessionmaker(
            autocommit=False, autoflush=False, bind=self.__engine, class_=AsyncSession
        )

    async def dispose_engine(self):
        """Close and delete created engine."""
        await self.__engine.dispose()

    def get_engine(self) -> AsyncEngine:
        """Get private variable __engine."""
        return self.__engine
