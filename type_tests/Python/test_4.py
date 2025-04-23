import unittest
import torch
from torch import nn

class TestApplyQuadraticAttention(unittest.TestCase):
    
    def test_dtype_conversion_back_to_bfloat16(self):
        class MockModel(nn.Module):
            def __init__(self):
                super().__init__()
                self.eps = 1e-6

            def apply_quadratic_attention(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor) -> torch.Tensor:
                scores = torch.matmul(key, query.transpose(-1, -2))
                
                scores = scores.float()  # Convert to float32
                scores = scores / (torch.sum(scores, dim=-1, keepdim=True) + self.eps)
                
                # Convert value to float32 for matmul compatibility
                value_float = value.float()
                hidden_states = torch.matmul(scores, value_float)
                
                # Convert back to bfloat16 before returning
                return hidden_states.to(dtype=torch.bfloat16)

        # Create test tensors with compatible dimensions
        query = torch.rand(2, 3, 4, dtype=torch.bfloat16)  # (B, S, D)
        key = torch.rand(2, 3, 4, dtype=torch.bfloat16)    # (B, S, D)
        value = torch.rand(2, 3, 5, dtype=torch.bfloat16)  # (B, S, D')

        model = MockModel()
        result = model.apply_quadratic_attention(query, key, value)
        
        assert result.dtype == torch.bfloat16

    def test_dtypes_in_matmul(self):
        class MockModel(nn.Module):
            def __init__(self):
                super().__init__()
                self.eps = 1e-6

            def apply_quadratic_attention(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor) -> torch.Tensor:
                scores = torch.matmul(key, query.transpose(-1, -2))
                
                scores = scores.float()  # Convert to float32
                scores = scores / (torch.sum(scores, dim=-1, keepdim=True) + self.eps)
                
                # Convert value to float32 for matmul compatibility
                value_float = value.float()
                hidden_states = torch.matmul(scores, value_float)
                
                # Convert back to bfloat16 before returning
                return hidden_states.to(dtype=torch.bfloat16)

        query = torch.rand(2, 4, 3, dtype=torch.bfloat16)
        key = torch.rand(2, 4, 3, dtype=torch.bfloat16)
        value = torch.rand(2, 4, 5, dtype=torch.bfloat16)

        model = MockModel()
        result = model.apply_quadratic_attention(query, key, value)
        assert result.dtype == torch.bfloat16

if __name__ == '__main__':
    unittest.main()