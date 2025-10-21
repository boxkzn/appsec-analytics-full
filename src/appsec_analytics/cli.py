import typer
from appsec_analytics.ingestion.snyk_ingest import run as snyk_ingest
from appsec_analytics.ingestion.zap_ingest import run as zap_ingest
from appsec_analytics.ingestion.sonar_ingest import run as sonar_ingest

app = typer.Typer(help="AppSec CLI")

@app.command()
def snyk(org: str, project: str, service: str):
    """Загрузить уязвимости из Snyk в БД."""
    snyk_ingest(org, project, service)

@app.command()
def zap(target: str, service: str):
    """Загрузить уязвимости из ZAP (по базе URL)."""
    zap_ingest(target, service)

@app.command()
def sonar(component_key: str, service: str):
    """Загрузить уязвимости из SonarQube в БД."""
    sonar_ingest(component_key, service)

if __name__ == "__main__":
    app()
