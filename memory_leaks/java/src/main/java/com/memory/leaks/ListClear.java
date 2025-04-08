package com.memory.leaks;

import java.util.ArrayList;
import java.util.List;

public class ListClear {
    public static void main( String[] args )
    {
        List<byte[]> list = new ArrayList<>();
        for (int i = 0; i < 10; i++) {
            list.add(new byte[1024 * 1024]);
        }
        list.clear(); // clear when done
    }
}
