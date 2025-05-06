import torch
from torch import nn

def apply_quadratic_attention(query: torch.Tensor, key: torch.Tensor, value: torch.Tensor) -> torch.Tensor:
    eps = 1e-6
    scores = torch.matmul(key, query.transpose(-1, -2))
    
    scores = scores.float()
    scores = scores / (torch.sum(scores, dim=-1, keepdim=True) + eps)
    
    value_float = value.float()
    hidden_states = torch.matmul(scores, value_float)
    
    return hidden_states.to(dtype=torch.bfloat16)