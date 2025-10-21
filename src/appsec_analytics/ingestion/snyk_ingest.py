from appsec_analytics.clients.snyk import Snyk
from appsec_analytics.db.repository import upsert_vuln
from appsec_analytics.utils.logging import setup_logger

log = setup_logger("ingest.snyk")

SEV_MAP = {"low":"low","medium":"medium","high":"high","critical":"critical"}

def run(org_id: str, project_id: str, service: str) -> None:
    api = Snyk()
    data = api.list_vulns(org_id, project_id)
    for item in data.get("data", []):
        attrs = item.get("attributes", {})
        sev = SEV_MAP.get(attrs.get("severity", "medium"), "medium")
        upsert_vuln({
            "source":"SNYK","service":service,
            "vuln_id": attrs.get("identifier"),
            "title": attrs.get("title"),
            "severity": sev,
            "discovered_at": attrs.get("introducedDate", "NOW()"),
            "url": attrs.get("url"),
            "raw": item,
        })
    log.info("Snyk ingest: service=%s count=%d", service, len(data.get("data", [])))
