.PHONY: install run test docker lint

install:
	uv sync

run:
	uv run flask run --host=0.0.0.0 --port=$${PORT:-5000}

test:
	uv run pytest

docker:
	docker compose up -d --build
