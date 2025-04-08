package com.off.by.one;
import org.junit.Test;
import static org.junit.Assert.assertEquals;
import java.util.List;

public class ProcessResultsTest {
    @Test
    public void testBuggyAndFixedLineOffset() {
        ProcessResults processor = new ProcessResults();
        String fakeLink = "somePrefix testMethod someSuffix";

        MockStatus buggy = processor.processAmbiguousResults(List.of("match1"), "SomeType", 42, fakeLink, false);
        MockStatus fixed = processor.processAmbiguousResults(List.of("match1"), "SomeType", 42, fakeLink, true);

        assertEquals(42, buggy.line);  // buggy: unchanged
        assertEquals(43, fixed.line);  // fixed: line++
    }
}

