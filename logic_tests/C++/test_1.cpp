#include <gtest/gtest.h>
#include <cstdint>
#include <cstdlib>

template <typename T>
static constexpr int numValDigits(const T& value)
{
    using U = std::make_unsigned_t<T>;
    if (value == 0) return 0;
    int digitCount = 0;
    U locVal = llabs(value);
    while (locVal >>= 1) ++digitCount;
    return digitCount;
}

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
