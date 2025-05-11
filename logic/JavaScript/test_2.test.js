// Import the actual FetchWrapper to mock it
const { FetchWrapper } = require('./helpers/fetch_wrapper');
const { registerUser } = require('./helpers/registerUser'); // Import from the separate file

// Mock the FetchWrapper
jest.mock('./helpers/fetch_wrapper', () => {
  return {
    FetchWrapper: jest.fn().mockImplementation(() => ({
      then: jest.fn().mockImplementation((callback) => {
        return callback({ success: true });
      })
    }))
  };
});

describe('registerUser', () => {
  beforeEach(() => {
    // Clear all mock calls between tests
    FetchWrapper.mockClear();
  });

  it('should convert email username to lowercase before registering', async () => {
    const testEmail = 'JohnDoe@EXAMPLE.com';
    const expectedUsername = 'johndoe';
    const password = 'secret';
    const role = 'user';

    const result = await registerUser(testEmail, password, role);

    // Verify FetchWrapper was called with correct arguments
    expect(FetchWrapper).toHaveBeenCalledTimes(1);
    expect(FetchWrapper).toHaveBeenCalledWith(
      'https://example.com/users/register',
      {
        method: 'POST',
        body: JSON.stringify({
          email: testEmail,
          password,
          role,
          username: expectedUsername
        })
      }
    );

    // Verify the response
    expect(result).toEqual({ success: true });
  });
});