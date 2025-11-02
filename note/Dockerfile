FROM ghcr.io/astral-sh/uv:python3.11-bookworm-slim AS build

WORKDIR /app

ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

COPY pyproject.toml uv.lock README.md* ./

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project --no-editable

COPY . /app

ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8001

CMD ["uv", "run", "prod"]