package com.memory.leaks;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

import java.util.ArrayList;
import java.util.List;

import org.junit.Test;

public class ListClearTest {
    @Test
    public void testListClearPreventsLeak()
    {
        List<byte[]> list = new ArrayList<>();
        for (int i = 0; i < 10; i++) {
            list.add(new byte[1024 * 1024]);
        }
        assertFalse(list.isEmpty());

        list.clear(); // fix

        assertTrue(list.isEmpty());
    }
}
