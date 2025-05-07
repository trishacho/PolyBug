package com.api.misuse;

public class FixedDialog {
    public Window getWindow() {
        return null; // simulate null case
    }

    public void setAnimationStyle(int animRes) {
        Window window = getWindow();
        if (window != null) {
            window.setWindowAnimations(animRes);
        }
    }
}
