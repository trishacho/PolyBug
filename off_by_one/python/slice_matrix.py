import numpy as np
from scipy.sparse import csr_matrix

class DummyClass:
    def __init__(self, bottom, right, top, left, lower_triangular=False):
        self._bottom_bound = bottom
        self._right_bound = right
        self._top_bound = top
        self._left_bound = left
        self.lower_triangular = lower_triangular

    def _slice_matrix_bug(self, I):
        if self.lower_triangular:
            rows = slice(0, self._bottom_bound)
            cols = slice(self._left_bound, self._right_bound)
            return I[rows, :].tocsc()[:, cols].toarray()
        rows = slice(self._top_bound, 5)
        cols = slice(self._left_bound, self._right_bound)
        return I[rows, :].tocsc()[:, cols].toarray()

    def _slice_matrix_fixed(self, I):
        if self.lower_triangular:
            rows = slice(0, self._bottom_bound)
            cols = slice(self._left_bound, self._right_bound)
            return I[rows, :].tocsc()[:, cols].toarray()

        rows = slice(self._top_bound, self._bottom_bound)  # changed from 5 to self._bottom_bound
        cols = slice(self._left_bound, self._right_bound)
        return I[rows, :].tocsc()[:, cols].toarray()