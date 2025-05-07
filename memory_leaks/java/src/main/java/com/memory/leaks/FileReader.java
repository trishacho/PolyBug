package com.memory.leaks;
import java.io.FileInputStream;
import java.io.IOException;

public class FileReader 
{
    public void readFile(String filePath) throws IOException {
        try (FileInputStream fis = new FileInputStream(filePath)) {
            int data = fis.read();
        }
    }
    
    public static void main( String[] args )
    {
        System.out.println( "Hello World!" );
    }
}
