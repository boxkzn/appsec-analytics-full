# 🧩 AppSec Analytics

[![Python 3.12](https://img.shields.io/badge/python-3.12-blue?logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-async%20web%20framework-009688?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Poetry](https://img.shields.io/badge/deps-managed%20by%20Poetry-60A5FA?logo=poetry)](https://python-poetry.org/)
[![SQLAlchemy](https://img.shields.io/badge/ORM-SQLAlchemy-red)](https://www.sqlalchemy.org/)
[![Docker](https://img.shields.io/badge/Docker-ready-2496ED?logo=docker)](https://www.docker.com/)
[![CI /CD](https://img.shields.io/badge/GitLab%20CI-enabled-orange?logo=gitlab)](https://docs.gitlab.com/ee/ci/)

---

## 🇷🇺 Описание проекта

**AppSec Analytics** — шаблон для системных аналитиков и инженеров AppSec/DevSecOps.  
Собирает результаты (**SAST / DAST / SCA**) из **Snyk**, **OWASP ZAP** и **SonarQube**,  
сохраняет их в **PostgreSQL**, строит метрики (MTTR, SLA, risk-score) и отдаёт API.

Используется для дашбордов (Grafana/Power BI), отчётности и авто-тикетов в Jira.

---

## 🇬🇧 Project Overview

**AppSec Analytics** is a template for System Analysts and AppSec/DevSecOps engineers.  
It ingests **SAST / DAST / SCA** results from **Snyk**, **OWASP ZAP**, and **SonarQube**,  
stores them in **PostgreSQL**, computes metrics (MTTR, SLA, risk-score), and exposes an API.

Built for dashboards (Grafana/Power BI), reports, and automatic Jira tickets.

---

## ⚙️ Технологии / Tech Stack

| Категория / Category | Технологии / Technologies |
|:-----------|:------------|
| Язык / Language | 🐍 Python 3.12 |
| API / Web | ⚡ FastAPI + Uvicorn |
| ORM / DB | 🧱 SQLAlchemy + PostgreSQL |
| Integrations | 🌐 httpx + Pydantic |
| Security | 🧰 Snyk, OWASP ZAP, SonarQube |
| Metrics | 📊 Grafana, Power BI |
| Containerization | 🐳 Docker |
| CI/CD | 🔁 GitLab CI + pre-commit (Black + Ruff + Mypy) |

---

## 🚀 Быстрый старт / Quick Start

```bash
# 1) Dependencies
pip install poetry
poetry install

# 2) Env
cp .env.example .env

# 3) DB schema
psql $PG_DSN -f sql/schema.sql

# 4) Run API
poetry run uvicorn appsec_analytics.services.api:app --reload --port 8080

# 5) CLI
poetry run appsec --help
```

---

## 📊 Метрики / Metrics

| Metric | Meaning |
|:------|:--------|
| **MTTR** | Mean Time To Remediate |
| **SLA Compliance** | Fixed on time ratio |
| **Open Vulns** | Count of active vulnerabilities |
| **Security Coverage** | CI/CD coverage by checks |
| **AppSec Maturity** | SAMM / BSIMM level |

---

## 🧰 Docker

```bash
docker compose up -d
# API: http://localhost:8080
# Postgres: localhost:5432 (user: postgres, pass: postgres, db: appsec)
```

---

## 🔄 CI/CD

GitLab CI stages: setup → test → security → build.

---

## 🧭 Roadmap

- [x] Snyk ingestion
- [x] OWASP ZAP ingestion
- [x] SonarQube ingestion
- [x] Dev Containers (VS Code)
- [ ] SLA gates in CI
- [ ] Prometheus metrics export
- [ ] RBAC & API tokens
- [ ] Helm chart for K8s deploy

---

## 👤 Author

**Евгений Акимов (Evgenii Akimov)** — System Analyst (AppSec & Cloud Solutions)  
[Telegram](https://t.me/akimov_ev) • [GitHub](https://github.com/portfolio_akimov_e)
