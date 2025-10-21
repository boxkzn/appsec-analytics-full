.PHONY: fmt lint test api docker

fmt:
	poetry run black .
	poetry run ruff check . --fix

lint:
	poetry run black --check .
	poetry run ruff check .
	poetry run mypy src

test:
	poetry run pytest -q --disable-warnings --maxfail=1

api:
	poetry run uvicorn appsec_analytics.services.api:app --reload --port 8080

docker:
	docker build -t appsec-analytics:local -f docker/Dockerfile .
