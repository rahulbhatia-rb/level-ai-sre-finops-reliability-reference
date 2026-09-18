# SRE FinOps Reliability Reference

Role-focused reference for Level AI's Senior SRE opening. It models a practical decision point for Kubernetes operations: use measurable utilisation and error-budget state to choose between scaling, investigation, and release restraint.

`assess()` keeps cost and reliability evidence together. A production version would source metrics from Prometheus/Grafana and cloud billing, attach results to Terraform/GitOps changes, and route the outcome to service owners.

## Run the POC

```bash
python3 -m unittest discover -s tests -v
python3 -m src.app < examples/capacity.jsonl
```

The first example returns `scale-with-guardrails`; the second returns
`protect-reliability`, because preserving the error budget takes precedence
over capacity expansion.

## Operational flow

1. A collector normalizes utilization, capacity demand, and SLO budget state.
2. The policy returns a deterministic recommendation in JSONL.
3. A change controller records it, applies approved scaling, and routes unsafe
   outcomes to the incident workflow.

The project is a personal demonstration—not a claim of access to Level AI systems or production GPU/GCP clusters. It reflects my AWS, automation, and GenAI/RAG deployment work and focuses on transparent SRE and FinOps decisioning.

[LinkedIn](https://www.linkedin.com/in/rahul-h-bhatia/) · [Portfolio](https://rahulhbhatia.vercel.app) · [Credly](https://www.credly.com/users/rahul-h-bhatia/badges)
