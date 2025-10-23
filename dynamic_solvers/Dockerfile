FROM python:3.13.8-slim

WORKDIR /oop

COPY --from=ghcr.io/astral-sh/uv:0.9.5 /uv /uvx /bin/

ENV UV_LINK_MODE=copy

COPY uv.lock pyproject.toml ./

RUN --mount=type=cache,target=/Users/$USER/.cache/uv \
    uv venv --relocatable && \
    uv sync --frozen && \
    uv cache clean

# Add venv bin to PATH so python/pip always point to it
ENV VIRTUAL_ENV=/app/.venv
ENV PATH="/oop/.venv/bin:$PATH"

COPY dynamic_solvers ./dynamic_solvers
COPY dynamic_solvers/configs /configs

ENTRYPOINT ["/bin/bash", "-c"]
CMD ["python3 -m dynamic_solvers.benchmark \"$CONFIG_CSV\" --output \"$OUTPUT_CSV\" $VERBOSE $ENCODING -bf $BF"]
