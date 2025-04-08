#include <assert.h>
#include <stdio.h>

#define ENOSYS -38
#define EIO -5

typedef struct {
    int (*get_link)(const void *dev, void *state);
} ethphy_driver_api;

typedef struct {
    const ethphy_driver_api *api;
} device;

int phy_get_link_state(const device *dev, void *state) {
    if (dev->api->get_link == NULL) {
        return ENOSYS; // return -ENOSYS instead of crashing
    }
    return dev->api->get_link(dev, state);
}

int mock_get_link(const void *dev, void *state) {
    return 0; // simulates successful retrieval of link state
}

void test_phy_get_link_state() {
    ethphy_driver_api api_with_null = { .get_link = NULL };
    device dev_with_null_api = { .api = &api_with_null };

    ethphy_driver_api api_with_valid_func = { .get_link = mock_get_link };
    device dev_with_valid_api = { .api = &api_with_valid_func };

    // correct version should return NULL if get_link not present and 0 (success) if present
    assert(phy_get_link_state(&dev_with_null_api, NULL) == ENOSYS);
    assert(phy_get_link_state(&dev_with_valid_api, NULL) == 0);

    printf("All test cases passed.\n");
}

int main() {
    test_phy_get_link_state();
    return 0;
}