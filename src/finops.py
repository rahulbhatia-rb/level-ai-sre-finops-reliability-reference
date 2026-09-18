"""FinOps and reliability policy for hybrid Kubernetes and GPU inference workloads."""
from dataclasses import dataclass


@dataclass(frozen=True)
class WorkloadSignal:
    cpu_request_utilization: float
    memory_request_utilization: float
    gpu_utilization: float
    gpu_queue_depth: int
    error_budget_remaining: float
    cost_per_request_usd: float
    target_cost_per_request_usd: float
    telemetry_complete: bool
    workload_identity_enabled: bool


def assess(signal: WorkloadSignal) -> dict:
    """Recommend a responsible GPU/Kubernetes action with specific findings."""
    for rate in (signal.cpu_request_utilization, signal.memory_request_utilization, signal.gpu_utilization, signal.error_budget_remaining):
        if not 0 <= rate <= 1:
            raise ValueError("utilization and error-budget rates must be 0..1")
    findings = []
    if not signal.telemetry_complete:
        findings.append("cost-or-reliability-telemetry-incomplete")
    if not signal.workload_identity_enabled:
        findings.append("workload-identity-missing")
    if signal.error_budget_remaining < 0.15:
        return {"recommendation": "protect-reliability", "findings": findings + ["error-budget-low"]}
    if signal.gpu_queue_depth > 100 and signal.gpu_utilization > 0.85:
        return {"recommendation": "scale-gpu-throughput", "findings": findings}
    if signal.cost_per_request_usd > signal.target_cost_per_request_usd and signal.cpu_request_utilization < 0.55 and signal.memory_request_utilization < 0.55:
        return {"recommendation": "right-size-kubernetes-requests", "findings": findings}
    if signal.gpu_utilization < 0.35:
        return {"recommendation": "profile-batching-and-kv-cache", "findings": findings}
    return {"recommendation": "monitor-and-tune", "findings": findings}
