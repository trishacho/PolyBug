import unittest
import torch
from torch import nn
from apply_quadratic_attention import apply_quadratic_attention

class TestApplyQuadraticAttention(unittest.TestCase):
    def test_dtype_conversion_back_to_bfloat16(self):
        # Create test tensors with compatible dimensions
        batch_size, seq_len, d_model = 8, 16, 64
        query = torch.rand(batch_size, seq_len, d_model, dtype=torch.bfloat16)  # (B, S, D)
        key = torch.rand(batch_size, seq_len, d_model, dtype=torch.bfloat16)  # (B, S, D)
        value = torch.rand(batch_size, seq_len, d_model, dtype=torch.bfloat16)  # (B, S, D)
        
        result = apply_quadratic_attention(query, key, value)
        
        self.assertEqual(result.dtype, torch.bfloat16)
        self.assertEqual(result.shape, (batch_size, seq_len, d_model))
    
    def test_dtypes_in_matmul(self):
        batch_size, seq_len, d_model, d_value = 4, 32, 128, 256
        query = torch.rand(batch_size, seq_len, d_model, dtype=torch.bfloat16)
        key = torch.rand(batch_size, seq_len, d_model, dtype=torch.bfloat16)
        value = torch.rand(batch_size, seq_len, d_value, dtype=torch.bfloat16)
        
        result = apply_quadratic_attention(query, key, value)
        
        self.assertEqual(result.dtype, torch.bfloat16)
        self.assertEqual(result.shape, (batch_size, seq_len, d_value))
    
    def test_attention_mask(self):
        batch_size, seq_len, d_model = 2, 10, 64
        query = torch.rand(batch_size, seq_len, d_model, dtype=torch.bfloat16)
        key = torch.rand(batch_size, seq_len, d_model, dtype=torch.bfloat16)
        value = torch.rand(batch_size, seq_len, d_model, dtype=torch.bfloat16)
        
        # Create a causal mask (upper triangular) to simulate autoregressive attention
        mask = torch.triu(torch.ones(seq_len, seq_len), diagonal=1).bool()
        mask = mask.to(query.device)
        
        # Test that applying a mask doesn't change output shape but affects values
        result_masked = apply_quadratic_attention(query, key, value, attention_mask=mask)
        result_unmasked = apply_quadratic_attention(query, key, value)
        
        self.assertEqual(result_masked.shape, result_unmasked.shape)
        self.assertFalse(torch.allclose(result_masked, result_unmasked, atol=1e-5))
    
    
    def test_numerical_stability(self):
        batch_size, seq_len, d_model = 2, 128, 64
        
        # Create extremely large values to test numerical stability
        query = (torch.rand(batch_size, seq_len, d_model) * 20 - 10).to(torch.bfloat16)
        key = (torch.rand(batch_size, seq_len, d_model) * 20 - 10).to(torch.bfloat16)
        value = torch.rand(batch_size, seq_len, d_model).to(torch.bfloat16)
        
        result = apply_quadratic_attention(query, key, value)
        
        # Check if result contains NaN values
        self.assertFalse(torch.isnan(result).any())
        # Check if result contains infinite values
        self.assertFalse(torch.isinf(result).any())


if __name__ == '__main__':
    unittest.main()
