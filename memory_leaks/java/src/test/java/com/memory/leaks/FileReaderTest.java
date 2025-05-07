package com.memory.leaks;
import java.io.IOException;
import org.junit.Test;

public class FileReaderTest 
{
    @Test(expected = IOException.class)
    public void testReadFileClosesStream() throws IOException {
        FileReader reader = new FileReader();
        reader.readFile("testfile.txt");
    }
}
