import unittest
import numpy as np
from pad_to_polygon import pad_to_polygon, pad_to_polygon_fixed, DummySrc, DummyGeo

class TestPadToPolygon(unittest.TestCase):
    def test_buggy_vs_fixed_padding(self):
        masked_src = np.ones((10, 10))
        padded_bug, _ = pad_to_polygon(DummySrc(), DummyGeo(), masked_src)
        padded_fix, _ = pad_to_polygon_fixed(DummySrc(), DummyGeo(), masked_src)
        
        self.assertEqual(padded_bug.shape, (12, 12))
        self.assertEqual(padded_fix.shape, (10, 10))

if __name__ == '__main__':
    unittest.main()