import org.junit.jupiter.api.Test;
import java.time.*;
import java.time.format.DateTimeFormatter;
import static org.junit.jupiter.api.Assertions.*;

public class DateTimeConversionTest {
    
    @Test
    public void verifyUtcToLocalTimeConversion_withSpecificTimeZone() {
        // Arrange
        String targetZone = "America/Chicago";
        String outputPattern = "MM/dd/yyyy HH:mm:ss z";
        LocalDateTime sourceDateTime = LocalDateTime.of(2025, 5, 15, 18, 30, 45, 0);
        ZonedDateTime utcZoned = sourceDateTime.atZone(ZoneOffset.UTC);
        
        // Expected conversion result - what we expect from our conversion method
        ZonedDateTime expectedZonedResult = utcZoned.withZoneSameInstant(ZoneId.of(targetZone));
        String expectedOutput = expectedZonedResult.format(DateTimeFormatter.ofPattern(outputPattern));
        
        // Act
        String actualOutput = TimeConverter.convertFromUtc(sourceDateTime, targetZone, outputPattern);
        
        // Assert
        assertEquals(expectedOutput, actualOutput, 
                    "UTC time conversion to " + targetZone + " should match expected format and offset");
    }
}
