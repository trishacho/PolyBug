const fs = require('fs');
const path = require('path');

// Mock dependencies
jest.mock('fs');
const hashString = jest.fn().mockResolvedValue('hashedPassword123');

const randomUUID = () => '123e4567-e89b-12d3-a456-426614174000';
const join = (...args) => path.join(...args);

describe('createUser', () => {
  const login = 'TestUser';  // Mixed case for testing
  const password = 'password123';
  const email = 'test@example.com';
  const normalizedLogin = login.toLowerCase(); // Lowercase version
  const userFilePath = join(process.cwd(), 'src', 'data', 'users', normalizedLogin, 'user.json');

  const createUser = async ({ login, password, email }) => {
    const normalizedLogin = login.toLowerCase(); // Convert to lowercase
    const userId = randomUUID();
    const folderPath = join(process.cwd(), 'src', 'data', 'users', normalizedLogin);
    const hashedPassword = await hashString(password);
    
    const user = {
      id: userId,
      login: normalizedLogin, // Store lowercase version
      email,
      password: hashedPassword,
    };

    if (fs.existsSync(userFilePath)) {
      throw new Error(`User with login: ${normalizedLogin} already exists`);
    }

    fs.mkdirSync(folderPath, { recursive: true });
    fs.writeFileSync(userFilePath, JSON.stringify(user));
    return user;
  };

  beforeEach(() => {
    jest.clearAllMocks();
  });

  it('should throw an error if user file already exists (case insensitive)', async () => {
    fs.existsSync.mockReturnValue(true);

    // Test with different case variations
    await expect(createUser({ login: 'TESTUSER', password, email }))
      .rejects
      .toThrow(`User with login: testuser already exists`);
    
    expect(fs.existsSync).toHaveBeenCalledWith(
      join(process.cwd(), 'src', 'data', 'users', 'testuser', 'user.json')
    );
  });

  it('should create user with lowercase login', async () => {
    fs.existsSync.mockReturnValue(false);
    
    const result = await createUser({ login: 'TestUser', password, email });
  
    // Verify the path uses lowercase
    expect(fs.mkdirSync).toHaveBeenCalledWith(
      join(process.cwd(), 'src', 'data', 'users', 'testuser'),
      { recursive: true }
    );
    
    // Verify stored login is lowercase
    expect(fs.writeFileSync).toHaveBeenCalledWith(
      join(process.cwd(), 'src', 'data', 'users', 'testuser', 'user.json'),
      JSON.stringify({
        id: '123e4567-e89b-12d3-a456-426614174000',
        login: 'testuser',  // Should be lowercase
        email,
        password: 'hashedPassword123'
      })
    );
    
    // Verify returned user has lowercase login
    expect(result).toEqual({
      id: '123e4567-e89b-12d3-a456-426614174000',
      login: 'testuser',
      email,
      password: 'hashedPassword123'
    });
  });

  it('should treat different cases as same user', async () => {
    // First create with one case
    fs.existsSync.mockReturnValueOnce(false);
    await createUser({ login: 'FirstUser', password, email });
    
    // Try to create with different case - should fail
    fs.existsSync.mockReturnValueOnce(true);
    await expect(createUser({ login: 'firstuser', password, email }))
      .rejects
      .toThrow('User with login: firstuser already exists');
  });
});