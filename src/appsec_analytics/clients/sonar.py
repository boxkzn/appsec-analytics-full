import httpx
from appsec_analytics.config import settings

class Sonar:
    def __init__(self):
        self._c = httpx.Client(timeout=60, auth=(settings.sonar_token, ""))
        self._base = settings.sonar_url.rstrip("/")

    def issues(self, component_key: str, severities: str = "BLOCKER,CRITICAL,MAJOR", statuses: str = "OPEN,REOPENED") -> dict:
        # SonarQube API: /api/issues/search
        params = {"componentKeys": component_key, "severities": severities, "statuses": statuses, "ps": 500}
        r = self._c.get(f"{self._base}/api/issues/search", params=params)
        r.raise_for_status()
        return r.json()
