
import unittest
import numpy as np
import copy

# Assuming these units are defined as constants
unit_k = "1/m"
unit_omega = "rad/s"

def apply_custom_mask(fields: dict, mask: np.ndarray, overwrite_fields: bool = True) -> dict:
    if not overwrite_fields:
        fields = copy.deepcopy(fields)

    for field_name in fields.keys():
        assert fields[field_name]["axis_units"] == [
            unit_k,
            unit_k,
            unit_omega,
        ], "Field units must be [unit_k, unit_k, unit_omega]"

        if field_name.endswith("positive"):
            fields[field_name]["data"] *= mask[:, :, : mask.shape[2] // 2]
        elif field_name.endswith("negative"):
            fields[field_name]["data"] *= mask[:, :, mask.shape[2] // 2 :]
    return fields

class TestApplyCustomMask(unittest.TestCase):
    def setUp(self):
        self.mask = np.ones((4, 4, 6))
        self.mask[:, :, :3] = 2  # For positive
        self.mask[:, :, 3:] = 3  # For negative

        self.fields = {
            "velocity_positive": {
                "data": np.ones((4, 4, 3)),
                "axis_units": [unit_k, unit_k, unit_omega],
            },
            "velocity_negative": {
                "data": np.ones((4, 4, 3)),
                "axis_units": [unit_k, unit_k, unit_omega],
            },
        }

    def test_apply_custom_mask_in_place(self):
        result = apply_custom_mask(self.fields, self.mask, overwrite_fields=True)
        np.testing.assert_array_equal(result["velocity_positive"]["data"], np.ones((4, 4, 3)) * 2)
        np.testing.assert_array_equal(result["velocity_negative"]["data"], np.ones((4, 4, 3)) * 3)

    def test_apply_custom_mask_copy(self):
        original_fields = copy.deepcopy(self.fields)
        result = apply_custom_mask(self.fields, self.mask, overwrite_fields=False)
        # Check that original was not modified
        np.testing.assert_array_equal(self.fields["velocity_positive"]["data"], original_fields["velocity_positive"]["data"])
        # Check that result has modified values
        np.testing.assert_array_equal(result["velocity_positive"]["data"], np.ones((4, 4, 3)) * 2)

if __name__ == "__main__":
    unittest.main()
