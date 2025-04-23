#include <assert.h>
#include <string.h>
#include <stdbool.h>
#include <stdio.h>

#define MAX_ADV 5

struct bt_le_ext_adv {
    int dummy;
};

bool adv_called = false;
bool rpa_data_snapshot[MAX_ADV] = {false};

struct {
    size_t id_count;
} bt_dev = { .id_count = MAX_ADV };

struct bt_le_ext_adv adv_pool[MAX_ADV];

void adv_rpa_invalidate(struct bt_le_ext_adv *adv, void *data) {
    bool *rpa_data = data;
    memcpy(rpa_data_snapshot, rpa_data, sizeof(bool) * bt_dev.id_count);
    adv_called = true;
}

void bt_le_ext_adv_foreach(void (*func)(struct bt_le_ext_adv *adv, void *data), void *data) {
    for (size_t i = 0; i < bt_dev.id_count; i++) {
        func(&adv_pool[i], data);
    }
}

void le_rpa_invalidate_test() {
    bool rpa_expired_data[MAX_ADV] = {0};
    bt_le_ext_adv_foreach(adv_rpa_invalidate, &rpa_expired_data);
}

void setUp(void) {
    adv_called = false;
    memset(rpa_data_snapshot, 1, sizeof(rpa_data_snapshot));
}

void test_rpa_data_is_initialized(void) {
    setUp();
    le_rpa_invalidate_test();

    assert(adv_called && "adv_called should be true");

    for (size_t i = 0; i < bt_dev.id_count; i++) {
        assert(rpa_data_snapshot[i] == false && "rpa_data_snapshot should be false");
    }

    printf("test_rpa_data_is_initialized passed\n");
}

int main(void) {
    test_rpa_data_is_initialized();
    printf("All tests passed!\n");
    return 0;
}
