#include <gtest/gtest.h>
#include <cstdint>
#include <cstdlib>
#include "numValDigits.h"

TEST(NumValDigitsTest, HandlesZero) {
    EXPECT_EQ(numValDigits(0), 0);
}

TEST(NumValDigitsTest, HandlesPositiveValues) {
    EXPECT_EQ(numValDigits(1), 0);        // 2^0
    EXPECT_EQ(numValDigits(2), 1);        // 2^1
    EXPECT_EQ(numValDigits(15), 3);       // 2^4 - 1
    EXPECT_EQ(numValDigits(16), 4);       // 2^4
}

TEST(NumValDigitsTest, HandlesNegativeValues) {
    EXPECT_EQ(numValDigits(-1), 0);
    EXPECT_EQ(numValDigits(-2), 1);
    EXPECT_EQ(numValDigits(-15), 3);
    EXPECT_EQ(numValDigits(-16), 4);
}
