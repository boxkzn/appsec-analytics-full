import httpx
from appsec_analytics.config import settings

class ZAP:
    def __init__(self):
        self._c = httpx.Client(timeout=60)
        self._base = settings.zap_api.rstrip("/")

    def alerts(self, baseurl: str = None, start: int = 0, count: int = 9999) -> dict:
        # ZAP JSON API: /JSON/core/view/alerts/
        params = {"apikey": settings.zap_token, "start": start, "count": count}
        if baseurl:
            params["baseurl"] = baseurl
        r = self._c.get(f"{self._base}/JSON/core/view/alerts/", params=params)
        r.raise_for_status()
        return r.json()
