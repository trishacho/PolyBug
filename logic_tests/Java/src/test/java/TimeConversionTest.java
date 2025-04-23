import org.junit.jupiter.api.Test;
import java.time.*;
import static org.junit.jupiter.api.Assertions.*;
import java.time.format.DateTimeFormatter;

public class TimeConversionTest {

    @Test
    public void testConvertFromUtc_withCorrectUtcOffset() {
        String timeZoneId = "America/New_York";  // Use a timezone with daylight savings
        String format = "yyyy-MM-dd HH:mm:ss Z"; // Include UTC offset in format

        OffsetDateTime utcTime = OffsetDateTime.of(2025, 4, 1, 12, 0, 0, 0, ZoneOffset.UTC);

        OffsetDateTime expectedLocalTime = utcTime.atZoneSameInstant(ZoneId.of(timeZoneId)).toOffsetDateTime();

        String result = convertFromUtc(utcTime.toLocalDateTime(), timeZoneId, format);

        String expectedFormattedTime = expectedLocalTime.format(DateTimeFormatter.ofPattern(format));

        assertEquals(expectedFormattedTime, result, "Time conversion with UTC offset should be correct.");
    }

    public String convertFromUtc(LocalDateTime utcTime, String timeZoneId, String format) {
        ZoneId zoneId = ZoneId.of(timeZoneId);
        ZonedDateTime zonedDateTime = utcTime.atZone(ZoneOffset.UTC).withZoneSameInstant(zoneId);
        return zonedDateTime.format(DateTimeFormatter.ofPattern(format));
    }
}
