import httpx
from appsec_analytics.config import settings

class Jira:
    def __init__(self):
        self._c = httpx.Client(auth=(settings.jira_user, settings.jira_token), timeout=30)
        self._base = settings.jira_url.rstrip("/")

    def create_issue(self, summary: str, description: str, project: str = "SEC", issue_type: str = "Bug", priority: str = "High") -> str:
        payload = {
            "fields": {
                "project": {"key": project},
                "summary": summary,
                "description": description,
                "issuetype": {"name": issue_type},
                "priority": {"name": priority},
            }
        }
        r = self._c.post(f"{self._base}/rest/api/2/issue", json=payload)
        r.raise_for_status()
        return r.json()["key"]
