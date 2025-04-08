import { TextEncoder } from 'util';

// fake environment switch
function inNodeEnv() {
  return true;
}

// buggy version
function buggy_getByteArrayValue(strValue: string): ArrayBuffer | undefined {
  if (strValue && strValue.length > 0) {
    return inNodeEnv() ? Buffer.from(strValue, "base64").buffer : new TextEncoder().encode(strValue);
  }
  return undefined;
}

// corrected version
function fixed_getByteArrayValue(strValue: string): ArrayBuffer | undefined {
  if (strValue && strValue.length > 0) {
    return inNodeEnv()
      ? new Uint8Array(Buffer.from(strValue, "base64")).buffer
      : new TextEncoder().encode(strValue);
  }
  return undefined;
}

// tests
test('Buggy version leaks underlying buffer memory', () => {
  const input = 'aGVsbG8='; // base64 for "hello"
  const result = buggy_getByteArrayValue(input) as ArrayBuffer;
  const uint8 = new Uint8Array(result);

  // expect only 5 bytes ("hello"), but may be more
  expect(uint8.length).toBeGreaterThan(5);
});

test('Fixed version returns correct-sized buffer', () => {
  const input = 'aGVsbG8='; // base64 for "hello"
  const result = fixed_getByteArrayValue(input) as ArrayBuffer;
  const uint8 = new Uint8Array(result);

  expect(uint8.length).toBe(5);
  expect(new TextDecoder().decode(uint8)).toBe('hello');
});
