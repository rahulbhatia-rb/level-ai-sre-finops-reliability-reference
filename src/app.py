"""JSONL interface for a reliability-aware capacity recommendation."""
import json
import sys
from src.finops import Signal, assess


def evaluate(payload: dict) -> dict:
    return {"input": payload, "recommendation": assess(Signal(**payload))}


def main() -> None:
    for line in sys.stdin:
        if line.strip():
            print(json.dumps(evaluate(json.loads(line))))


if __name__ == "__main__":
    main()
