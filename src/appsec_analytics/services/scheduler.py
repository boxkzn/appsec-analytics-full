from apscheduler.schedulers.background import BackgroundScheduler
from appsec_analytics.ingestion.snyk_ingest import run as snyk_run
from appsec_analytics.ingestion.zap_ingest import run as zap_run
from appsec_analytics.ingestion.sonar_ingest import run as sonar_run

sched = BackgroundScheduler()

# Примеры расписаний (замените на свои параметры)
sched.add_job(lambda: snyk_run("orgX","projectY","billing-api"), "cron", minute=0)
sched.add_job(lambda: zap_run("https://app.dev","billing-api"), "cron", minute=15)
sched.add_job(lambda: sonar_run("org.app:billing-api","billing-api"), "cron", minute=30)

def start():
    sched.start()
