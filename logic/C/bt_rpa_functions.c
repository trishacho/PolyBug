#include "bt_rpa_functions.h"
#include <stdio.h>
#include <stddef.h>
#include <string.h>

/* Mock necessary functions */
#define ARRAY_SIZE(arr) (sizeof(arr) / sizeof((arr)[0]))

/* Mock for atomic operations */
#define atomic_test_bit(flags, bit) ((flags) & (1 << (bit)))
#define atomic_clear_bit(flags, bit) ((flags) &= ~(1 << (bit)))

/* Define the constants */
#define BT_ADV_CREATED 0
#define BT_DEV_SCAN_LIMITED 1
#define BT_DEV_RPA_VALID 2

/* External references to variables defined in the main file */
extern struct {
    int flags;
    int id_count;
} bt_dev;

extern struct bt_le_ext_adv adv_pool[3];

/* External references to config variables */
extern int CONFIG_BT_EXT_ADV_ENABLED;
extern int CONFIG_BT_BROADCASTER_ENABLED;

/* The functions to test */
void bt_le_ext_adv_foreach(void (*func)(struct bt_le_ext_adv *adv, void *data),
                          void *data)
{
    if (CONFIG_BT_EXT_ADV_ENABLED) {
        for (size_t i = 0; i < ARRAY_SIZE(adv_pool); i++) {
            if (atomic_test_bit(adv_pool[i].flags, BT_ADV_CREATED)) {
                func(&adv_pool[i], data);
            }
        }
    } else {
        // This branch not used in our test
        printf("Non-EXT_ADV branch would be used here\n");
    }
}

/* Mock for the adv_rpa_invalidate function */
void adv_rpa_invalidate(struct bt_le_ext_adv *adv, void *data)
{
    bool *rpa_expired = (bool *)data;
    
    /* Print values to see if they're initialized */
    printf("rpa_expired value: %d\n", rpa_expired[0]);
    
    /* Attempting to use the value might cause issues if uninitialized */
    if (rpa_expired[0]) {
        printf("RPA expired flag is set\n");
    } else {
        printf("RPA expired flag is not set\n");
    }
}

/* Exported non-static function */
void le_rpa_invalidate(void)
{
    /* Invalidate RPA */
    if (!(CONFIG_BT_EXT_ADV_ENABLED &&
        atomic_test_bit(bt_dev.flags, BT_DEV_SCAN_LIMITED))) {
        atomic_clear_bit(bt_dev.flags, BT_DEV_RPA_VALID);
    }
    if (CONFIG_BT_BROADCASTER_ENABLED) {
        if (bt_dev.id_count == 0) {
            return;
        }
        /* Now declare the uninitialized variable which will likely get the garbage values */
        bool rpa_expired_data[bt_dev.id_count]; /* BUG: Array is not initialized */
        bt_le_ext_adv_foreach(adv_rpa_invalidate, rpa_expired_data);
    }
}