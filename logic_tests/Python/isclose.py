import numpy as np
from types import ModuleType

def isclose(
    a,
    b,
    *,
    rtol: float = 1e-05,
    atol: float = 1e-08,
    equal_nan: bool = False,
    xp: ModuleType,
):
    """See docstring in array_api_extra._delegation."""
    a_inexact = xp.isdtype(a.dtype, ("real floating", "complex floating"))
    b_inexact = xp.isdtype(b.dtype, ("real floating", "complex floating"))
    if a_inexact or b_inexact:
        out = xp.abs(a - b) <= (atol + rtol * xp.abs(b))
        out = xp.where(xp.isinf(a) & xp.isinf(b), xp.sign(a) == xp.sign(b), out)
        if equal_nan:
            out = xp.where(xp.isnan(a) & xp.isnan(b), xp.asarray(True), out)
        return out
    if xp.isdtype(a.dtype, "bool") or xp.isdtype(b.dtype, "bool"):
        if atol >= 1 or rtol >= 1:
            return xp.ones_like(a == b)
        return a == b
    atol = int(atol)
    if rtol == 0:
        return xp.abs(a - b) <= atol
    nrtol = np.array(int(1.0 / rtol), dtype=np.int8)[0]
    return xp.abs(a - b) <= (atol + xp.abs(b) // nrtol)