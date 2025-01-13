# Base image
FROM python:3.11-slim AS base

RUN apt update && \
    apt install --no-install-recommends -y build-essential gcc && \
    apt clean && rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt
COPY pyproject.toml pyproject.toml
COPY src/ src/
COPY data/ data/
COPY models/ models/
COPY reports/ reports/
RUN --mount=type=cache,target=~/pip/.cache pip install -r requirements.txt --no-cache-dir --timeout=120 --index-url https://pypi.org/simple
RUN pip install . --no-deps --no-cache-dir --verbose

ENTRYPOINT ["python", "-u", "src/project1/evaluate.py"]
