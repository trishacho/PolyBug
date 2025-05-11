
import unittest
from unittest.mock import patch, MagicMock
import numpy as np
import pathlib
import xarray as xr

from your_module import mass_weighted_mean  # Replace with actual module name

class TestMassWeightedMean(unittest.TestCase):
    @patch('your_module.xr.open_dataset')
    def test_mass_weighted_mean_full_region(self, mock_open_dataset):
        # Mock data
        species_data = np.ones((4, 5, 3))  # Shape: (lat, lon, level)
        thickness = np.array([2.0, 3.0, 5.0])  # len = 3 for the last dimension

        # Expected vertical_integral = sum across level axis: 1*2 + 1*3 + 1*5 = 10 for each (i,j)
        # So 4x5 grid of 10s, mean is 10
        expected_mean = 10.0

        # Setup mock
        mock_species = MagicMock()
        mock_species.to_numpy.return_value = species_data

        mock_ds = MagicMock()
        mock_ds.__enter__.return_value = { 'co2': mock_species }
        mock_ds.__getitem__.side_effect = lambda key: {'co2': mock_species}[key]
        mock_open_dataset.return_value = mock_ds

        result = mass_weighted_mean(
            file_name=pathlib.Path("dummy.nc"),
            species='co2',
            thickness=thickness,
            region_inds=None
        )

        self.assertAlmostEqual(result, expected_mean)

    @patch('your_module.xr.open_dataset')
    def test_mass_weighted_mean_region_slice(self, mock_open_dataset):
        species_data = np.ones((4, 5, 3))
        thickness = np.array([1.0, 2.0, 3.0])  # total weight = 6

        # Each value: 1*1 + 1*2 + 1*3 = 6
        # Mean of a 2x2 slice of 6s is 6
        expected_mean = 6.0

        mock_species = MagicMock()
        mock_species.to_numpy.return_value = species_data

        mock_ds = MagicMock()
        mock_ds.__enter__.return_value = { 'co2': mock_species }
        mock_ds.__getitem__.side_effect = lambda key: {'co2': mock_species}[key]
        mock_open_dataset.return_value = mock_ds

        result = mass_weighted_mean(
            file_name=pathlib.Path("dummy.nc"),
            species='co2',
            thickness=thickness,
            region_inds=((1, 1), (2, 2))  # 2x2 region
        )

        self.assertAlmostEqual(result, expected_mean)

if __name__ == '__main__':
    unittest.main()
