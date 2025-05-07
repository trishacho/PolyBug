package com.api.misuse;

public class BuggyDialog {
    public Window getWindow() {
        return null; // simulate null case
    }

    public void setAnimationStyle(int animRes) {
        Window window = getWindow();
        window.setWindowAnimations(animRes); // crashes if window is null
    }
}
