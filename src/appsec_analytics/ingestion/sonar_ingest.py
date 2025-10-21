from appsec_analytics.clients.sonar import Sonar
from appsec_analytics.db.repository import upsert_vuln
from appsec_analytics.utils.logging import setup_logger

log = setup_logger("ingest.sonar")

SEV_MAP = {
    "INFO":"low","MINOR":"low","MAJOR":"medium","CRITICAL":"high","BLOCKER":"critical"
}

def run(component_key: str, service: str) -> None:
    api = Sonar()
    data = api.issues(component_key)
    for issue in data.get("issues", []):
        sev = SEV_MAP.get(issue.get("severity","MAJOR"), "medium")
        upsert_vuln({
            "source":"SONAR","service":service,
            "vuln_id": issue.get("rule"),
            "title": issue.get("message"),
            "severity": sev,
            "discovered_at": issue.get("creationDate","NOW()"),
            "url": issue.get("project",""),
            "raw": issue,
        })
    log.info("Sonar ingest: service=%s count=%d", service, len(data.get("issues", [])))
