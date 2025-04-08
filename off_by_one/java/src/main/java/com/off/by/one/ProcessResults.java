package com.off.by.one;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class ProcessResults {
    private static final String REGEX_FOR_NORMAL = "(.*)(testMethod)(.*)";

    public MockStatus processAmbiguousResults(List<String> matches, String typeName, int line, String link, boolean isFixed) {
        Pattern pattern = Pattern.compile(REGEX_FOR_NORMAL);
        Matcher matcher = pattern.matcher(link);
        String methodSignature = null;
        if (matcher.find()) {
            methodSignature = matcher.group(2) + "(params)";
        }

        if (methodSignature == null) {
            return new MockStatus(line); // simulate openClipboard
        }

        boolean hasExactMatches = true; // mock logic
        if (hasExactMatches) {
            return new MockStatus(isFixed ? line + 1 : line); // this is what we're testing!
        } else {
            return new MockStatus(isFixed ? line + 1 : line);
        }
    }
}