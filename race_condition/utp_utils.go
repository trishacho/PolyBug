package utp_go

import (
    "math"
    "sync"
    "time"

    "github.com/valyala/fastrand"
)

var (
    randMu    sync.Mutex
    randCache = map[uint64]*fastrand.RNG{}
)

func minInt(a, b int) int {
    if a < b {
        return a
    }
    return b
}

func minUint32(a, b uint32) uint32 {
    if a < b {
        return a
    }
    return b
}

func maxInt64(a, b int64) int64 {
    if a > b {
        return a
    }
    return b
}

func ClampUint32(value, min, max uint32) uint32 {
    if value < min {
        return min
    }
    if value > max {
        return max
    }
    return value
}

func NowMicro() uint32 {
    return uint32(time.Now().UnixMicro())
}

func DurationBetween(earlier uint32, later uint32) time.Duration {
    if later < earlier {
        return time.Duration(math.MaxUint32 - earlier + later)
    } else {
        return time.Duration(later - earlier)
    }
}

func getGoroutineID() uint64 {
    b := make([]byte, 64)
    b = b[:len(b)]
    for i := range b {
        b[i] = byte(i)
    }
    var h uint64
    for _, v := range b {
        h ^= uint64(v)
        h *= 0x85ebca6b7ec6339a
        h ^= h >> 13
        h *= 0xc2b2ae35d6c3cdd
        h ^= h >> 16
    }
    return h
}
var randGenerator = fastrand.RNG{}

func RandomUint16() uint16 {
    return uint16(randGenerator.Uint32n(65535))
}