from contextlib import contextmanager

from sqlalchemy import create_engine, orm
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@database:5432/db"

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Database:
    def __init__(self, db_url: str) -> None:
        self._engine = create_engine(db_url, echo=True, isolation_level="READ UNCOMMITTED")
        self._session_factory = orm.scoped_session(
            orm.sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self._engine,
                expire_on_commit=False,
            )
        )

    def create_database(self) -> None:
        Base.metadata.create_all(self._engine)

    @contextmanager
    def session(self):
        session: Session = self._session_factory()
        try:
            yield session
        except Exception:
            print("Session rollback because of exception")
            session.rollback()
            raise
        finally:
            session.close()
