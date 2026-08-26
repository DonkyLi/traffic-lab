from __future__ import annotations

import argparse

from .config import Config
from .service import Orchestrator
from .server import serve
from .runner import TaskWorker


def main() -> None:
    parser = argparse.ArgumentParser(description="Traffic Lab agent orchestrator")
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("status")
    subparsers.add_parser("serve")
    worker = subparsers.add_parser("worker")
    worker.add_argument("--role", default="director")
    ingest = subparsers.add_parser("ingest")
    ingest.add_argument("text")
    ingest.add_argument("--event-id", default="local-event")
    args = parser.parse_args()
    orchestrator = Orchestrator(Config.from_env())
    if args.command == "status":
        print(orchestrator.status_text())
    elif args.command == "serve":
        serve(Config.from_env())
    elif args.command == "worker":
        result = TaskWorker(Config.from_env()).process_one(args.role)
        print(result if result else "no ready task")
    else:
        print(orchestrator.ingest_feishu_text(args.text, args.event_id))


if __name__ == "__main__":
    main()
