#ifndef BT_RPA_FUNCTIONS_H
#define BT_RPA_FUNCTIONS_H

#include <stdbool.h>

/* Define the structure */
struct bt_le_ext_adv {
    int flags;
};

/* Function declarations */
void bt_le_ext_adv_foreach(void (*func)(struct bt_le_ext_adv *adv, void *data), void *data);
void adv_rpa_invalidate(struct bt_le_ext_adv *adv, void *data);
void le_rpa_invalidate(void); /* Exported function */

#endif /* BT_RPA_FUNCTIONS_H */