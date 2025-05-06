import unittest
import numpy as np
import torch
from reverse_tensor import reverse_tensor

class TestNegativeStrideFix(unittest.TestCase):

    def test_negative_stride_handling(self):
        # Create a numpy array with values 0 through 9
        x = np.arange(10)

        # Apply the patch: ensure a copy is made for negative strides
        # Using np.copy to ensure we create a new copy of the reversed array
        reversed_tensor = reverse_tensor(x)
        
        # Verify that the tensor values are correctly reversed
        for i in range(len(reversed_tensor)):
            self.assertTrue(reversed_tensor[i] == x[len(reversed_tensor)-1-i])

if __name__ == '__main__':
    unittest.main()
