FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app
COPY calculator ./calculator
COPY tests ./tests

# Default: run the CLI, e.g. `docker run calculator add 2 3`
ENTRYPOINT ["python", "-m", "calculator"]
