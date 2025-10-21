from fastapi import FastAPI
from pydantic import BaseModel
from appsec_analytics.db.engine import SessionLocal
from appsec_analytics.db.repository import upsert_vuln

app = FastAPI(title="AppSec Metrics")

class VulnIn(BaseModel):
    source: str
    service: str
    vuln_id: str | None = None
    title: str | None = None
    severity: str
    discovered_at: str
    url: str | None = None
    raw: dict | None = None

@app.post("/ingest")
def ingest(v: VulnIn):
    upsert_vuln(v.model_dump())
    return {"ok": True}

@app.get("/metrics/open")
def open_counts():
    q = """
    SELECT severity, COUNT(*) AS cnt
    FROM vulns
    WHERE fixed_at IS NULL
    GROUP BY severity
    ORDER BY 1;
    """
    with SessionLocal() as s:
        res = s.execute(q).mappings().all()
        return {r["severity"]: r["cnt"] for r in res}
