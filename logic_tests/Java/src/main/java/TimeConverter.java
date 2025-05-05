import java.time.LocalDateTime;
import java.time.ZoneId;
import java.time.ZoneOffset;
import java.time.ZonedDateTime;
import java.time.format.DateTimeFormatter;

public class TimeConverter {
    public static String convertFromUtc(LocalDateTime utcTime, String timeZoneId, String format) {
        ZoneId zoneId = ZoneId.of(timeZoneId);
        
        ZonedDateTime zonedDateTime = utcTime.atZone(ZoneOffset.UTC);
        
        return zonedDateTime.format(DateTimeFormatter.ofPattern(format));
    }
}