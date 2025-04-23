import pytest
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
        # FIXME: use scipy's lazywhere to suppress warnings on inf
        out = xp.abs(a - b) <= (atol + rtol * xp.abs(b))
        out = xp.where(xp.isinf(a) & xp.isinf(b), xp.sign(a) == xp.sign(b), out)
        if equal_nan:
            out = xp.where(xp.isnan(a) & xp.isnan(b), xp.asarray(True), out)
        return out
    if xp.isdtype(a.dtype, "bool") or xp.isdtype(b.dtype, "bool"):
        if atol >= 1 or rtol >= 1:
            return xp.ones_like(a == b)
        return a == b
    # integer types
    atol = int(atol)
    if rtol == 0:
        return xp.abs(a - b) <= atol
    nrtol = int(1.0 / rtol)

    return xp.abs(a - b) <= (atol + xp.abs(b) // nrtol)


# Test for isClose() function: https://github.com/data-apis/array-api-extra/pull/130/commits/2bce6142051699da9dffd2b7ab5a3c948a1c37d9
def test_isclose_handles_integer_overflow():
    class FakeXP:
        def abs(self, x):
            return np.abs(x)

        def isdtype(self, dtype, kind):
            return dtype == bool if kind == "bool" else False

        def ones_like(self, x):
            return np.ones_like(x)

        def sign(self, x):
            return np.sign(x)

        def isinf(self, x):
            return np.isinf(x)

        def where(self, cond, x, y):
            return np.where(cond, x, y)

        def isnan(self, x):
            return np.isnan(x)

        def asarray(self, val):
            return np.asarray(val)

    xp = FakeXP()
    a = np.array([1, 2, 3])
    b = np.array([1, 2, 4])  # differs in last value

    try:
        # Use an extremely small rtol that would cause 1.0 / rtol to overflow
        result = isclose(a, b, rtol=1e-300, atol=0, xp=xp)
    except OverflowError:
        pytest.fail("OverflowError was not handled properly")

    # The fallback comparison should behave like np.abs(a - b) <= atol
    expected = np.abs(a - b) <= 0
    assert np.array_equal(result, expected)