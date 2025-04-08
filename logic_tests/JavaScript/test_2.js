// Mock the FetchWrapper
jest.mock('./yourModule', () => {
  const original = jest.requireActual('./yourModule');
  return {
    ...original,
    FetchWrapper: jest.fn(),
  };
});

import { FetchWrapper } from './yourModule';

describe('registerUser', () => {
  it('should convert email username to lowercase before registering', async () => {
    const testEmail = 'JohnDoe@EXAMPLE.com';
    const expectedUsername = 'johndoe';
    const password = 'secret';
    const role = 'user';

    // Mock response from the FetchWrapper
    FetchWrapper.mockResolvedValue({ success: true });

    await registerUser(testEmail, password, role);

    // Capture the call to FetchWrapper
    expect(FetchWrapper).toHaveBeenCalledTimes(1);
    const [, options] = FetchWrapper.mock.calls[0];
    const requestBody = JSON.parse(options.body);

    expect(requestBody.username).toBe(expectedUsername);
  });
});