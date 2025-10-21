from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseModel):
    jira_url: str = os.getenv("JIRA_URL", "")
    jira_user: str = os.getenv("JIRA_USER", "")
    jira_token: str = os.getenv("JIRA_TOKEN", "")
    snyk_token: str = os.getenv("SNYK_TOKEN", "")
    gitlab_url: str = os.getenv("GITLAB_URL", "")
    gitlab_token: str = os.getenv("GITLAB_TOKEN", "")
    sonar_url: str = os.getenv("SONAR_URL", "")
    sonar_token: str = os.getenv("SONAR_TOKEN", "")
    zap_api: str = os.getenv("ZAP_API", "http://localhost:8090")
    zap_token: str = os.getenv("ZAP_TOKEN", "")
    pg_dsn: str = os.getenv("PG_DSN", "")

settings = Settings()
