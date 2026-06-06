# syntax=docker/dockerfile:1

# Minimal image for a machineplay UCI engine.
#
#   docker build -t my-engine .
#   docker run --rm -i my-engine     # then type UCI commands (uci, position, go)
#
# machineplay runs the image as `docker run --rm -i --network none ... my-engine`
# and pipes the UCI protocol over stdin/stdout, so the container just needs to
# launch the engine and talk over stdio.

FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim

# UCI is a line-based protocol over stdio: never buffer output.
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install dependencies first so this layer is cached until the lockfile changes.
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev

# Then add the engine source.
COPY main.py ./

# Run the engine straight from the synced virtualenv. No uv at runtime keeps
# startup fast and works under `--network none`.
ENTRYPOINT [".venv/bin/python", "main.py"]
