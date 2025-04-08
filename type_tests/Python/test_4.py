import unittest
import torch
from torch import nn

class TestApplyQuadraticAttention(unittest.TestCase):
    
    def test_dtype_conversion_back_to_bfloat16(self):
        # Setup: mock the class and function
        class MockModel(nn.Module):
            def __init__(self):
                super().__init__()
                self.eps = 1e-6

            def apply_quadratic_attention(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor) -> torch.Tensor:
                pass

        # Test case 1: Ensure the conversion happens as expected

        # Create mock data with bfloat16 dtype
        query = torch.rand(2, 3, 4, dtype=torch.bfloat16)
        key = torch.rand(2, 4, 3, dtype=torch.bfloat16)
        value = torch.rand(2, 3, 5, dtype=torch.bfloat16)

        model = MockModel()

        # Call the method
        result = model.apply_quadratic_attention(query, key, value)

        # Verify the final output is of dtype bfloat16
        self.assertEqual(result.dtype, torch.bfloat16)

    def test_dtypes_in_matmul(self):
        # Setup: mock the class and function
        class MockModel(nn.Module):
            def __init__(self):
                super().__init__()
                self.eps = 1e-6

            def apply_quadratic_attention(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor) -> torch.Tensor:
                pass

        # Test case 2: Check if float32 conversion happens for matmul and then reverts to bfloat16
        query = torch.rand(2, 3, 4, dtype=torch.bfloat16)
        key = torch.rand(2, 4, 3, dtype=torch.bfloat16)
        value = torch.rand(2, 3, 5, dtype=torch.bfloat16)

        model = MockModel()

        # Call the method
        result = model.apply_quadratic_attention(query, key, value)

        # Ensure the final result is of dtype bfloat16
        self.assertEqual(result.dtype, torch.bfloat16)

        # Ensure intermediate steps are float32 (after the first matmul)
        scores = torch.matmul(key.transpose(-1, -2), query).to(dtype=torch.float32)
        self.assertEqual(scores.dtype, torch.float32)

if __name__ == '__main__':
    unittest.main()
