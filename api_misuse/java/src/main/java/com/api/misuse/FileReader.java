package com.api.misuse;

public class FileReader {
    public void readFile(String filePath) throws IOException {
        try (FileInputStream fis = new FileInputStream(filePath)) {
            int data = fis.read();
        }
    }
}
