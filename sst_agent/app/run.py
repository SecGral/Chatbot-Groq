"""Launcher for running SST Agent with configurable host and port."""

from __future__ import annotations

import argparse
import os

import uvicorn

from sst_agent.app.main import app


def _env_bool(name: str, default: bool = False) -> bool:
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the SST Agent API")
    parser.add_argument("--host", default=os.getenv("HOST", "0.0.0.0"))
    parser.add_argument("--port", type=int, default=int(os.getenv("CHATBOT_PORT", "8010")))
    parser.add_argument("--reload", action="store_true", default=_env_bool("RELOAD", False))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    uvicorn.run(
        "sst_agent.app.main:app",
        host=args.host,
        port=args.port,
        reload=args.reload,
    )


if __name__ == "__main__":
    main()