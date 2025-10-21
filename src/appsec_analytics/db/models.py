from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, JSON, Enum, TIMESTAMP
import enum

class Base(DeclarativeBase):
    pass

class Severity(enum.Enum):
    low = "low"
    medium = "medium"
    high = "high"
    critical = "critical"

class Vuln(Base):
    __tablename__ = "vulns"
    id: Mapped[int] = mapped_column(primary_key=True)
    source: Mapped[str] = mapped_column(String)
    service: Mapped[str] = mapped_column(String)
    vuln_id: Mapped[str | None] = mapped_column(String, nullable=True)
    title: Mapped[str | None] = mapped_column(String, nullable=True)
    severity: Mapped[Severity] = mapped_column(Enum(Severity))
    discovered_at: Mapped[str] = mapped_column(TIMESTAMP)
    fixed_at: Mapped[str | None] = mapped_column(TIMESTAMP, nullable=True)
    url: Mapped[str | None] = mapped_column(String, nullable=True)
    raw: Mapped[dict | None] = mapped_column(JSON, nullable=True)
