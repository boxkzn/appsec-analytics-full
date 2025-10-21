from appsec_analytics.db.repository import upsert_vuln

def test_upsert_smoke(monkeypatch):
    class Dummy:
        def __enter__(self): return self
        def __exit__(self, *a): return False
        def execute(self, *a, **k): return None
        def commit(self): return None
    from appsec_analytics.db import repository
    monkeypatch.setattr(repository, "SessionLocal", lambda: Dummy())
    upsert_vuln({
        "source":"SNYK","service":"billing","vuln_id":"CVE-1","title":"t",
        "severity":"high","discovered_at":"2024-01-01T00:00:00Z","url":"u","raw":{}
    })
