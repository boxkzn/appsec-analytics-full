import httpx
from appsec_analytics.config import settings

class Snyk:
    def __init__(self):
        self._c = httpx.Client(headers={"Authorization": f"token {settings.snyk_token}"}, timeout=60)

    def list_vulns(self, org_id: str, project_id: str) -> dict:
        url = f"https://api.snyk.io/rest/orgs/{org_id}/projects/{project_id}/issues?version=2024-08-01"
        r = self._c.get(url)
        r.raise_for_status()
        return r.json()
