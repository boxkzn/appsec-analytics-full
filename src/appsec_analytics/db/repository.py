from sqlalchemy import text
from appsec_analytics.db.engine import SessionLocal

def upsert_vuln(v: dict) -> None:
    q = text(
        """
        INSERT INTO vulns (source, service, vuln_id, title, severity, discovered_at, url, raw)
        VALUES (:source,:service,:vuln_id,:title,:severity,:discovered_at,:url,CAST(:raw AS JSONB))
        ON CONFLICT (source, service, vuln_id, url) DO NOTHING
        """
    )
    with SessionLocal() as s:
        s.execute(q, v)
        s.commit()
