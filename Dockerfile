FROM python:3.12-slim

RUN pip install uv

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev

COPY gta/ ./gta/

EXPOSE 5000

CMD ["uv", "run", "gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "--timeout", "120", "gta.main:app"]
