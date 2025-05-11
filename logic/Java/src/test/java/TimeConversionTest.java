import org.junit.jupiter.api.Test;
import java.time.*;
import java.time.format.DateTimeFormatter;
import static org.junit.jupiter.api.Assertions.*;

public class TimeConversionTest {
    @Test
    public void testConvertFromUtc_withCorrectUtcOffset() {
        String timeZoneId = "America/New_York";
        String format = "yyyy-MM-dd HH:mm:ss Z";

        OffsetDateTime utcTime = OffsetDateTime.of(2025, 4, 1, 12, 0, 0, 0, ZoneOffset.UTC);
        OffsetDateTime expectedLocalTime = utcTime.atZoneSameInstant(ZoneId.of(timeZoneId)).toOffsetDateTime();
        
        String result = TimeConverter.convertFromUtc(utcTime.toLocalDateTime(), timeZoneId, format);
        String expectedFormattedTime = expectedLocalTime.format(DateTimeFormatter.ofPattern(format));

        assertEquals(expectedFormattedTime, result);
    }
}