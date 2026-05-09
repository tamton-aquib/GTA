.PHONY: install run test docker deploy

install:
	uv sync

run:
	uv run flask run --host=0.0.0.0 --port=$${PORT:-5000}

deploy:
	uv run gunicorn -w 2 -b 0.0.0.0:$${PORT:-5000} --timeout 120 gta.main:app

test:
	uv run pytest

docker:
	docker compose up -d --build
