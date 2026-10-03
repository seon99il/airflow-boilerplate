FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

ENV UV_SYSTEM_PYTHON=1 \
    UV_LINK_MODE=copy \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

ARG DEPS_GROUP=common

RUN --mount=type=bind,source=pyproject.toml,target=/tmp/project/pyproject.toml \
    uv pip install --group /tmp/project/pyproject.toml:${DEPS_GROUP}

WORKDIR /app
