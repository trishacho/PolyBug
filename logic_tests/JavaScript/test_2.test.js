// Import the actual FetchWrapper to mock it
const { FetchWrapper } = require('./helpers/fetch_wrapper');

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

const registerUser = async (email, password, role) => {
  let userName = email.split('@')[0].toLowerCase();
  const object = {
    email,
    password,
    role,
    username: userName,
  };

  const response = await new FetchWrapper(
    'https://example.com/users/register',
    {
      method: 'POST',
      body: JSON.stringify(object),
    }
  );
  return response;
};

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