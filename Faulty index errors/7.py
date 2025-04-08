
import unittest
from unittest.mock import patch, MagicMock
import numpy as np
import pandas as pd
import os
import xarray as xr

# Assume this is imported from your actual module
# from your_module import create_from_GLORYS

class TestCreateFromGLORYS(unittest.TestCase):

    @patch('your_module.os.makedirs')
    @patch('your_module.xr.Dataset.to_netcdf')
    @patch('your_module.load_GLORYS')
    def test_create_from_GLORYS_all_vars(self, mock_load, mock_to_netcdf, mock_makedirs):
        # Create mock data
        time_data = pd.date_range("2023-01-01", periods=3)
        grid_shape = (3, 10, 10)
        lon = np.linspace(-30, 10, 10)
        lat = np.linspace(35, 65, 10)

        mock_salt = MagicMock()
        mock_temp = MagicMock()
        mock_zeta = MagicMock()
        mock_u = MagicMock()
        mock_v = MagicMock()

        mock_salt.data = np.random.rand(*grid_shape)
        mock_temp.data = np.random.rand(*grid_shape)
        mock_zeta.data = np.random.rand(*grid_shape)
        mock_u.data = np.random.rand(*grid_shape)
        mock_v.data = np.random.rand(*grid_shape)

        mock_salt.__getitem__.return_value = mock_salt.data
        mock_temp.__getitem__.return_value = mock_temp.data
        mock_zeta.__getitem__.return_value = mock_zeta.data

        mock_load.return_value = (
            mock_salt,
            mock_temp,
            mock_zeta,
            mock_u,
            mock_v,
            lon,
            lat,
            None, None
        )

        with patch('your_module.pd.to_datetime', return_value=time_data):
            create_from_GLORYS('mock_data.nc', variables='all')

        self.assertTrue(mock_makedirs.called)
        self.assertTrue(mock_to_netcdf.called)
        self.assertEqual(mock_to_netcdf.call_count, 4)  # One file per box

if __name__ == '__main__':
    unittest.main()
