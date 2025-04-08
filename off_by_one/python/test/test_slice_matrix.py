import unittest
import numpy as np
from scipy.sparse import csr_matrix
from slice_matrix import DummyClass

class TestSliceMatrix(unittest.TestCase):
    def test_buggy_vs_fixed_shape(self):
        I = csr_matrix(np.arange(25).reshape(5, 5))
        dummy = DummyClass(3, 3, 1, 1)

        buggy = dummy._slice_matrix_bug(I)
        fixed = dummy._slice_matrix_fixed(I)

        self.assertEqual(buggy.shape, (4, 2))  # Buggy
        self.assertEqual(fixed.shape, (2, 2))  # Fixed

if __name__ == '__main__':
    unittest.main()