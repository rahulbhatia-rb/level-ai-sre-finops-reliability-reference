# Level AI Senior SRE — FinOps and GPU Reliability Reference POC

A runnable decision engine for a hybrid Kubernetes and GPU inference platform. It connects cost per request, Kubernetes right-sizing, GPU throughput, SLOs, and safe platform controls. This is a personal demonstration project, not a representation of Level AI production systems.

## What it demonstrates

Level AI’s Senior SRE role is at the intersection of backend enablement, FinOps, reliability instrumentation, on-prem GPU experimentation, and GCP/Kubernetes operations. The POC makes those trade-offs explicit instead of treating cost, performance, and reliability as separate dashboards.

| Role area | Evidence and decision |
| --- | --- |
| Kubernetes overprovisioning | CPU/memory request utilisation plus cost per request → right-size requests |
| GPU throughput | GPU utilization and queue depth → scale throughput or profile batching/KV cache |
| Reliability | Error budget overrides cost or scaling changes when it is low |
| Team enablement | A deterministic recommendation can be exposed through dashboards/CLI for service owners |
| Instrumentation | Missing cost/reliability telemetry is an explicit finding |
| Security baseline | Workload identity is required for automated actions |

## Decision flow

```text
GKE + on-prem GPU metrics + billing telemetry
                    ↓
        FinOps / reliability policy
  ├─ right-size Kubernetes requests
  ├─ scale GPU throughput
  ├─ profile batching + KV cache
  └─ protect reliability when SLO budget is low
```

## Run it

```bash
python3 -m unittest discover -s tests -v
python3 -m src.app < examples/capacity.jsonl
```

The examples demonstrate right-sizing overprovisioned requests, scaling a saturated GPU queue, and protecting reliability when error budget is low.

## Production path

I would wire this into a GCP/GKE and on-prem collector using OpenTelemetry, Prometheus, and cloud billing exports. Backend service owners would receive a service-level recommendation in their own dashboard and PR/CI workflow, preserving their ownership of cost and reliability budgets. Terraform, Karpenter/Cast AI, HPA/VPA, and GPU-scheduler configuration would be controlled by approved actions, not an opaque autonomous scaler.

For GPU experiments, each trial would record model/inference-server version, batch size, concurrency, KV-cache setting, GPU type, requests/sec, latency distribution, utilization, and cost per request. That creates a reproducible throughput optimisation loop while safety gates preserve SLOs and workload identity.

## Candidate

- LinkedIn: https://www.linkedin.com/in/rahul-h-bhatia/
- Portfolio: https://rahulhbhatia.vercel.app
- Credly: https://www.credly.com/users/rahul-h-bhatia/badges
