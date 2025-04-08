package com.api.misuse;
import org.junit.Test;
import java.io.FileInputStream;
import java.io.FileWriter;
import java.io.IOException;

public class FileReaderTest {
    @Test(expected = IOException.class)
    public void testReadFileClosesStream() throws IOException {
        FileWriter writer = new FileWriter("testfile.txt");
        writer.write("Hello");
        writer.close();

        FileReader reader = new FileReader();
        reader.readFile("testfile.txt");
    }
}