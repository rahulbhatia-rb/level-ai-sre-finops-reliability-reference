import unittest

from src.finops import WorkloadSignal, assess


class FinopsTests(unittest.TestCase):
    def test_right_sizes_overprovisioned_kubernetes_requests(self):
        signal = WorkloadSignal(.48, .42, .62, 20, .70, .18, .10, True, True)
        self.assertEqual("right-size-kubernetes-requests", assess(signal)["recommendation"])

    def test_scales_gpu_throughput_under_sustained_queue(self):
        signal = WorkloadSignal(.88, .82, .94, 180, .70, .10, .10, True, True)
        self.assertEqual("scale-gpu-throughput", assess(signal)["recommendation"])

    def test_error_budget_takes_priority(self):
        signal = WorkloadSignal(.70, .68, .80, 90, .08, .10, .10, True, True)
        self.assertEqual("protect-reliability", assess(signal)["recommendation"])
