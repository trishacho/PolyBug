#include <stdio.h>

typedef struct {
    int index;
} VTermColor;

typedef struct {
    VTermColor colors[16];
} VTermState;

void vterm_state_set_palette_color_bug(VTermState *state, int index, const VTermColor *col) {
    if (index >= 0 && index < 16) {
        state->colors[index] = *col;
        state->colors[index].index = index + 1;  // bug: extra +1
    }
}

void vterm_state_set_palette_color_fixed(VTermState *state, int index, const VTermColor *col) {
    if(index >= 0 && index < 16)
   {
     state->colors[index] = *col;
     state->colors[index].index = index;  // keep index consistent
   }
}

int main() {
    VTermState state;
    VTermColor col = {0};

    vterm_state_set_palette_color_bug(&state, 5, &col);
    printf("Buggy index: %d (Expected: 5)\n", state.colors[5].index);  // buggy: prints 6

    vterm_state_set_palette_color_fixed(&state, 5, &col);
    printf("Fixed index: %d (Expected: 5)\n", state.colors[5].index);  // correct: prints 5

    return 0;
}