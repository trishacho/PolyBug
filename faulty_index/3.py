import unittest
from unittest.mock import patch, MagicMock
import numpy as np
import pandas as pd

# Example class definition for context
class DummyAggregator:
    def __init__(self, pxx, freq):
        self.pxx = pxx
        self.freq = freq

    def aggregate(self, dom_freq_func, dom_freq_func_kwargs, masks):
        self.dom_freq_func = dom_freq_func
        self.dom_freq_func_kwargs = dom_freq_func_kwargs
        self.masks = masks

        peak_idxs, _, _ = np.apply_along_axis(spectra_utils.find_dominant_peak, 0, self.pxx)
        self.peak_idxs = peak_idxs.astype(int)

        self.pxx_avg = aggregate_utils.average_spectra(self.pxx)
        self.pxx_avg_peak_idx, _, _ = spectra_utils.find_dominant_peak(self.pxx_avg)
        self.pxx_avg_peak = self.freq[self.pxx_avg_peak_idx]

        if masks is not None:
            pass

        agg_dict = {'avg_spectrum_peak': self.pxx_avg_peak}
        self.agg_df = pd.DataFrame(agg_dict, index=[0, 1])

        return self.agg_df, self.pxx_avg, self.pxx_avg_peak_idx

# The actual test
class TestAggregateMethod(unittest.TestCase):
    @patch('spectra_utils.find_dominant_peak')
    @patch('aggregate_utils.average_spectra')
    def test_aggregate(self, mock_avg_spectra, mock_find_dominant_peak):
        # Sample data
        pxx = np.array([[1, 2], [3, 4], [5, 6]])
        freq = np.array([10, 20, 30])
        dom_func = MagicMock()
        dom_kwargs = {'some_arg': 42}
        masks = None

        # Mocked return values
        mock_find_dominant_peak.side_effect = [(2, None, None), (1, None, None)]
        mock_avg_spectra.return_value = np.array([2, 3, 4])

        # Create instance and call method
        agg = DummyAggregator(pxx, freq)
        agg_df, avg, peak_idx = agg.aggregate(dom_func, dom_kwargs, masks)

        # Check output
        self.assertIsInstance(agg_df, pd.DataFrame)
        self.assertEqual(agg_df.shape[0], 2)
        self.assertEqual(agg_df['avg_spectrum_peak'][0], freq[1])  # peak_idx = 1
        self.assertTrue(np.array_equal(avg, np.array([2, 3, 4])))
        self.assertEqual(peak_idx, 1)

if __name__ == '__main__':
    unittest.main()
