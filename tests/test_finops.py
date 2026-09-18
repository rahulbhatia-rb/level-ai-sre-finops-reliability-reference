import sys,unittest
sys.path.append("src")
from finops import Signal,assess
class T(unittest.TestCase):
 def test_budget_wins(self):self.assertEqual(assess(Signal(.9,.1,True)),"protect-reliability")
 def test_scale(self):self.assertEqual(assess(Signal(.9,.5,True)),"scale-with-guardrails")
 def test_bad_rate(self):
  with self.assertRaises(ValueError):assess(Signal(2,.5,False))
if __name__=="__main__":unittest.main()
