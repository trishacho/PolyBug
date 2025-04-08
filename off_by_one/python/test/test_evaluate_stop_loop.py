import unittest
from evaluate_stop_loop import Dummy

class TestEvaluateStopLoop(unittest.TestCase):
    def test_buggy_vs_fixed(self):
        dummy = Dummy([1, 2, 3], 3)
        self.assertFalse(dummy.evaluate_stop_loop_bug())
        self.assertTrue(dummy.evaluate_stop_loop_fixed())

if __name__ == '__main__':
    unittest.main()