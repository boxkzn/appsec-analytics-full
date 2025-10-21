FROM python:3.12-slim
ENV PIP_NO_CACHE_DIR=1
WORKDIR /app

RUN pip install poetry==1.8.3
COPY pyproject.toml poetry.lock* /app/
RUN poetry install --no-interaction --no-ansi

COPY src/ /app/src/
COPY sql/ /app/sql/
ENV PYTHONPATH=/app/src
EXPOSE 8080
CMD ["poetry","run","uvicorn","appsec_analytics.services.api:app","--host","0.0.0.0","--port","8080"]
