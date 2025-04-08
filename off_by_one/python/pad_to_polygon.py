import numpy as np
from types import SimpleNamespace
import sys
import rasterio as rio
from rasterio.mask import mask

def pad_to_polygon(src, geometry, masked_src):
    """""Pads masked_src to the extent of geometry if it is smaller"""""

    if not rio.coords.disjoint_bounds(src.bounds, geometry.total_bounds):
        left_pad = int(np.ceil((src.bounds[0] - geometry.total_bounds[0]) / src.res[0]))
        left_pad = int(max(left_pad, 0))
        bottom_pad = int(np.ceil((src.bounds[1] - geometry.total_bounds[1]) / src.res[1]))
        bottom_pad = int(max(bottom_pad, 0))
        right_pad = int(np.ceil((geometry.total_bounds[2] - src.bounds[2]) / src.res[0]))
        right_pad = int(max(right_pad, 0))
        top_pad = int(np.ceil((geometry.total_bounds[3] - src.bounds[3]) / src.res[1]))
        top_pad = int(max(top_pad, 0))

        if left_pad + bottom_pad + right_pad + top_pad == 0:
            return masked_src, False
        else:
            print(f"Padding {masked_src.shape} by {[top_pad, bottom_pad, left_pad, right_pad]}")
            padded_src  = np.pad(masked_src, pad_width=((top_pad, bottom_pad), (left_pad, right_pad)), mode='constant', constant_values=np.nan)
            return padded_src, True
    else:
        print("ERROR: The polygon and the source raster do not overlap.")
        sys.exit(1)

def pad_to_polygon_fixed(src, geometry, masked_src):
    """Pads masked_src to the extent of geometry if it is smaller"""

    if not rio.coords.disjoint_bounds(src.bounds, geometry.total_bounds):
        left_pad = int(np.round((src.bounds[0] - geometry.total_bounds[0]) / src.res[0]))
        left_pad = int(max(left_pad, 0))
        bottom_pad = int(np.round((src.bounds[1] - geometry.total_bounds[1]) / src.res[1]))
        bottom_pad = int(max(bottom_pad, 0))
        right_pad = int(np.round((geometry.total_bounds[2] - src.bounds[2]) / src.res[0]))
        right_pad = int(max(right_pad, 0))
        top_pad = int(np.round((geometry.total_bounds[3] - src.bounds[3]) / src.res[1]))
        top_pad = int(max(top_pad, 0))

        if left_pad + bottom_pad + right_pad + top_pad == 0:
            return masked_src, False
        else:
            print(f"Padding {masked_src.shape} by {[top_pad, bottom_pad, left_pad, right_pad]}")
            padded_src  = np.pad(masked_src, pad_width=((top_pad, bottom_pad), (left_pad, right_pad)), mode='constant', constant_values=np.nan)
            return padded_src, True
    else:
        print("ERROR: The polygon and the source raster do not overlap.")
        sys.exit(1)

class DummySrc:
    bounds = (0, 0, 10, 10)
    res = (1, 1)

class DummyGeo:
    total_bounds = (-0.4, -0.4, 10.4, 10.4)  # slightly larger than src