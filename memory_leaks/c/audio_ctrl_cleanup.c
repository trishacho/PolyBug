#include <assert.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// mock defs
#define PROFILE_HFP_AG 1
#define PROFILE_HFP_HF 2
#define AUDIO_TRANS_CH_ID_ALL 100
#define CONFIG_BLUETOOTH_AUDIO_TRANS_ID_HFP_CTRL 200

void* g_audio_ctrl_transport = NULL;
int last_closed_transport_flag = -1;

void audio_transport_close(void* transport, int flag) {
    // simulate freeing the transport and store flag used
    free(transport);
    last_closed_transport_flag = flag;
}

// actual fixed function
void audio_ctrl_cleanup(uint8_t profile_id)
{
    switch (profile_id) {
    case PROFILE_HFP_AG:
    case PROFILE_HFP_HF:
        if (g_audio_ctrl_transport) {
            audio_transport_close(g_audio_ctrl_transport, CONFIG_BLUETOOTH_AUDIO_TRANS_ID_HFP_CTRL); // fixed flag
        }
        break;
    default:
        printf("Warning: unknown profile id: %d\n", profile_id);
        break;
    }
    g_audio_ctrl_transport = NULL;
}

// test
void test_audio_ctrl_cleanup() {
    g_audio_ctrl_transport = malloc(sizeof(int));  // simulate allocated memory
    assert(g_audio_ctrl_transport != NULL);

    audio_ctrl_cleanup(PROFILE_HFP_AG);

    assert(g_audio_ctrl_transport == NULL);  // clean up
    assert(last_closed_transport_flag == CONFIG_BLUETOOTH_AUDIO_TRANS_ID_HFP_CTRL); // make sure flag is right

    printf("test_audio_ctrl_cleanup passed.\n");
}

int main() {
    test_audio_ctrl_cleanup();
    return 0;
}