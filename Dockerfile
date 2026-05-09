FROM python:3.12-slim

RUN pip install uv

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev

COPY gta/ ./gta/

EXPOSE 5000

CMD ["uv", "run", "flask", "run", "--host=0.0.0.0", "--port=5000"]
