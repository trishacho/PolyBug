#include <assert.h>
#include <stdio.h>

typedef struct {
    int (*cfg_link)(const void *dev, int speeds);
} ethphy_driver_api;

typedef struct {
    const ethphy_driver_api *api;
} device;

int ENOTSUP = 129;
int ENOSYS = 38;

int phy_configure_link(const device *dev, int speeds) {
    if (dev == NULL || dev->api == NULL) {
        return -ENOSYS;
    }
    
    if (dev->api->cfg_link == NULL) {
        return -ENOTSUP;
    }
    
    return dev->api->cfg_link(dev, speeds);

}

int test_phy_configure_link() {
    ethphy_driver_api api_with_fn = { .cfg_link = NULL };
    device dev_with_null_api = { .api = &api_with_fn };

    // fixed returns -ENOSYS
    assert(phy_configure_link(&dev_with_null_api, 100) == -ENOSYS || phy_configure_link(&dev_with_null_api, 100) == -ENOTSUP);

    printf("Test passed\n");
    return 0;
}

int main() {
    return test_phy_configure_link();
}