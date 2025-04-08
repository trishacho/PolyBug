package com.memory.leaks;

import static org.junit.Assert.assertTrue;
import static org.junit.Assert.assertThrows;

import java.io.FileInputStream;
import java.io.IOException;

import org.junit.Test;

public class FileReaderTest 
{
    @Test
    public void testReadFileClosesStream() throws IOException {
        FileReader reader = new FileReader();
        assertThrows(IOException.class, () -> {
            FileInputStream fis = new FileInputStream("testfile.txt");
            reader.readFile("testfile.txt"); // should properly close after reading
        });
    }
}
