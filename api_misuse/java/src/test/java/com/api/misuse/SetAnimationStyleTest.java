package com.api.misuse;
import org.junit.Test;
import static org.junit.Assert.*;
import com.api.misuse.BuggyDialog;
import com.api.misuse.FixedDialog;

public class SetAnimationStyleTest {

    @Test
    public void testBuggyVersionThrowsNPE() {
        BuggyDialog dialog = new BuggyDialog();

        try {
            dialog.setAnimationStyle(123);
            fail("Expected NullPointerException");
        } catch (NullPointerException e) {
            // test passes
        }
    }

    @Test
    public void testFixedVersionDoesNotThrow() {
        FixedDialog dialog = new FixedDialog();

        try {
            dialog.setAnimationStyle(123);
        } catch (Exception e) {
            fail("Should not throw exception, but got: " + e);
        }
    }
}