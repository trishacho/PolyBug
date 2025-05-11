import unittest
import torch
from torch import nn
from apply_quadratic_attention import apply_quadratic_attention

class TestApplyQuadraticAttention(unittest.TestCase):
    
    def test_dtype_conversion_back_to_bfloat16(self):
        # Create test tensors with compatible dimensions
        query = torch.rand(2, 3, 4, dtype=torch.bfloat16)  # (B, S, D)
        key = torch.rand(2, 3, 4, dtype=torch.bfloat16)    # (B, S, D)
        value = torch.rand(2, 3, 5, dtype=torch.bfloat16)  # (B, S, D')
        result = apply_quadratic_attention(query, key, value)
        
        assert result.dtype == torch.bfloat16

    def test_dtypes_in_matmul(self):
        query = torch.rand(2, 4, 3, dtype=torch.bfloat16)
        key = torch.rand(2, 4, 3, dtype=torch.bfloat16)
        value = torch.rand(2, 4, 5, dtype=torch.bfloat16)

        result = apply_quadratic_attention(query, key, value)
        assert result.dtype == torch.bfloat16

if __name__ == '__main__':
    unittest.main()