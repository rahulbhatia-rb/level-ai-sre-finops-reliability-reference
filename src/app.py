"""JSONL interface for hybrid GPU and Kubernetes capacity recommendations."""
import json
import sys
from src.finops import WorkloadSignal, assess


for line in sys.stdin:
    if line.strip():
        payload = json.loads(line)
        print(json.dumps({"workload": payload, "decision": assess(WorkloadSignal(**payload))}))
