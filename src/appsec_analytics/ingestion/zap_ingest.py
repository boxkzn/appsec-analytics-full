from appsec_analytics.clients.zap import ZAP
from appsec_analytics.db.repository import upsert_vuln
from appsec_analytics.utils.logging import setup_logger

log = setup_logger("ingest.zap")

def run(target_baseurl: str, service: str) -> None:
    api = ZAP()
    data = api.alerts(baseurl=target_baseurl)
    for alert in data.get("alerts", []):
        risk = (alert.get("risk") or alert.get("riskcode") or "").lower()
        # map common ZAP risks to our enum
        if risk in ("0","informational","info"): sev = "low"
        elif risk in ("1","low"): sev = "low"
        elif risk in ("2","medium"): sev = "medium"
        elif risk in ("3","high"): sev = "high"
        else: sev = "medium"
        instances = alert.get("instances") or []
        url = instances[0]["uri"] if instances else None
        upsert_vuln({
            "source":"ZAP","service":service,
            "vuln_id": alert.get("pluginId"),
            "title": alert.get("alert"),
            "severity": sev,
            "discovered_at": "NOW()",
            "url": url,
            "raw": alert,
        })
    log.info("ZAP ingest: service=%s count=%d", service, len(data.get("alerts", [])))
