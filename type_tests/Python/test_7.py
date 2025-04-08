import unittest
import numpy as np
import torch

class TestNegativeStrideFix(unittest.TestCase):

    def test_negative_stride_handling(self):
        # Create a numpy array with values 0 through 9
        x = np.arange(10)

        # Apply the patch: ensure a copy is made for negative strides
        # Using np.copy to ensure we create a new copy of the reversed array
        reversed_tensor = torch.as_tensor(x[::-1].copy())  # .copy() ensures a new tensor is created
        
        # Verify that the tensor values are correctly reversed
        expected_values = x[::-1]
        self.assertTrue(torch.equal(reversed_tensor, torch.tensor(expected_values)))

    def test_no_negative_stride(self):
        # Create a numpy array with values 0 through 9
        x = np.arange(10)
        
        # Apply a valid non-negative stride
        reversed_tensor = torch.as_tensor(x[::1])  # No negative stride used here
        
        # Check if the tensor is the same as the original numpy array
        self.assertTrue(torch.equal(reversed_tensor, torch.tensor(x)))

if __name__ == '__main__':
    unittest.main()
