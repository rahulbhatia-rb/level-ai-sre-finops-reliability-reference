from dataclasses import dataclass
@dataclass(frozen=True)
class Signal: utilization:float; error_budget:float; pending_capacity:bool
def assess(s:Signal)->str:
 if not 0<=s.utilization<=1 or not 0<=s.error_budget<=1: raise ValueError("rates must be 0..1")
 if s.error_budget<.15:return "protect-reliability"
 if s.utilization>.85 and s.pending_capacity:return "scale-with-guardrails"
 return "right-size-and-monitor"
