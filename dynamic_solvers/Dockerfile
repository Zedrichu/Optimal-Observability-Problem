FROM python:3.13.7-bookworm

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /oop
COPY uv.lock pyproject.toml ./
COPY dynamic_solvers/ ./dynamic_solvers/

RUN uv sync

# Add venv bin to PATH so python/pip always point to it
ENV PATH="/oop/.venv/bin:$PATH"
