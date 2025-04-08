import fs from 'fs';
import path from 'path';
import { createUser } from './userService';  // Assuming the function is in userService.js

jest.mock('fs');

describe('createUser', () => {
    const login = 'testUser';
    const password = 'password123';
    const email = 'test@example.com';

    const userFilePath = path.join(process.cwd(), 'src', 'data', 'users', login, 'user.json');

    beforeEach(() => {
        jest.clearAllMocks();
    });

    it('should throw an error if user file already exists', async () => {
        fs.existsSync.mockReturnValue(true);

        await expect(createUser({ login, password, email })).rejects.toThrowError(
            `User with login: ${login} already exists`
        );
    });

    it('should create the folder and user file if the file does not exist', async () => {
        fs.existsSync.mockReturnValue(false);

        fs.mkdirSync.mockImplementation(() => {});
        fs.writeFileSync.mockImplementation(() => {});

        await createUser({ login, password, email });

        expect(fs.mkdirSync).toHaveBeenCalledWith(path.join(process.cwd(), 'src', 'data', 'users', login), { recursive: true });

        expect(fs.writeFileSync).toHaveBeenCalledWith(userFilePath, expect.any(String));

        expect(fs.existsSync).toHaveBeenCalledWith(userFilePath);
    });
});
