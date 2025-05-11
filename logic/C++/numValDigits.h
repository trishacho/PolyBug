#ifndef NUM_VAL_DIGITS_H
#define NUM_VAL_DIGITS_H

#include <type_traits>
#include <cstdlib>

template <typename T>
static constexpr int numValDigits(const T& value)
{
    using U = std::make_unsigned_t<T>;
    if (value == 0) return 0;
    int digitCount = 0;
    U locVal = value;
    while (locVal >>= 1) ++digitCount;
    return digitCount;
}

#endif