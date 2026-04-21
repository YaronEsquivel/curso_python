FROM python:3.12-slim

RUN useradd -m appuser

WORKDIR /app

ENV PYTHONPATH=/app/src

COPY pyproject.toml poetry.lock ./

RUN pip install poetry

COPY . .

RUN poetry install

RUN chown -R appuser:appuser /app

USER appuser

CMD ["poetry", "run", "python", "-m", "app"]