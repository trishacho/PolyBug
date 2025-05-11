// tests/createUser.test.js
const fs = require('fs');
const path = require('path');
const createUser = require('./helpers/createUser');

// Mock dependencies
jest.mock('fs');

// Mock crypto.randomUUID
jest.mock('crypto', () => ({
  randomUUID: () => '123e4567-e89b-12d3-a456-426614174000'
}));

describe('createUser', () => {
  const login = 'TestUser';
  const password = 'password123';
  const email = 'test@example.com';
  const normalizedLogin = login.toLowerCase();
  const userFilePath = path.join(process.cwd(), 'src', 'data', 'users', normalizedLogin, 'user.json');

  beforeEach(() => {
    jest.clearAllMocks();
  });

  it('should throw an error if user file already exists (case insensitive)', async () => {
    fs.existsSync.mockReturnValue(true);

    await expect(createUser({ login: 'TESTUSER', password, email }))
      .rejects
      .toThrow(`User with login: testuser already exists`);
    
    expect(fs.existsSync).toHaveBeenCalledWith(userFilePath);
  });

  it('should create user with lowercase login', async () => {
    fs.existsSync.mockReturnValue(false);
    
    const result = await createUser({ login, password, email });
  
    expect(fs.mkdirSync).toHaveBeenCalledWith(
      path.join(process.cwd(), 'src', 'data', 'users', 'testuser'),
      { recursive: true }
    );
    
    expect(fs.writeFileSync).toHaveBeenCalledWith(
      userFilePath,
      JSON.stringify({
        id: '123e4567-e89b-12d3-a456-426614174000',
        login: 'testuser',
        email,
        password: 'hashedPassword123'
      })
    );
    
    expect(result).toEqual({
      id: '123e4567-e89b-12d3-a456-426614174000',
      login: 'testuser',
      email,
      password: 'hashedPassword123'
    });
  });

  it('should treat different cases as same user', async () => {
    fs.existsSync.mockReturnValueOnce(false);
    await createUser({ login: 'FirstUser', password, email });
    
    fs.existsSync.mockReturnValueOnce(true);
    await expect(createUser({ login: 'firstuser', password, email }))
      .rejects
      .toThrow('User with login: firstuser already exists');
  });
});