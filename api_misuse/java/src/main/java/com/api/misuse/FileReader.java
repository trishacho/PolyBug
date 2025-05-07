package com.api.misuse;
import java.io.FileInputStream;
import java.io.IOException;

public class FileReader {
    public void readFile(String filePath) throws IOException {
        try (FileInputStream fis = new FileInputStream(filePath)) {
            int data = fis.read();
        }
    }
}
