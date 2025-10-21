from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from appsec_analytics.config import settings

engine = create_engine(settings.pg_dsn, pool_pre_ping=True, future=True)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False, future=True)
