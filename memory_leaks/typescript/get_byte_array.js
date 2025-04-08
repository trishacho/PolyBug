"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var util_1 = require("util");
// Fake environment switch
function inNodeEnv() {
    return true;
}
// Buggy version
function buggy_getByteArrayValue(strValue) {
    if (strValue && strValue.length > 0) {
        return inNodeEnv() ? Buffer.from(strValue, "base64").buffer : new util_1.TextEncoder().encode(strValue);
    }
    return undefined;
}
// Corrected version
function fixed_getByteArrayValue(strValue) {
    if (strValue && strValue.length > 0) {
        return inNodeEnv()
            ? new Uint8Array(Buffer.from(strValue, "base64")).buffer
            : new util_1.TextEncoder().encode(strValue);
    }
    return undefined;
}
// ---- TEST ----
test('Buggy version leaks underlying buffer memory', function () {
    var input = 'aGVsbG8='; // base64 for "hello"
    var result = buggy_getByteArrayValue(input);
    var uint8 = new Uint8Array(result);
    // Expect only 5 bytes ("hello"), but may be more
    expect(uint8.length).toBeGreaterThan(5);
});
test('Fixed version returns correct-sized buffer', function () {
    var input = 'aGVsbG8='; // base64 for "hello"
    var result = fixed_getByteArrayValue(input);
    var uint8 = new Uint8Array(result);
    expect(uint8.length).toBe(5);
    expect(new TextDecoder().decode(uint8)).toBe('hello');
});
