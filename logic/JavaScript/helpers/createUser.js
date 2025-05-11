// src/data/users/createUser.js
const fs = require('fs');
const path = require('path');
const { randomUUID } = require('crypto');
const hashString = jest.fn().mockResolvedValue('hashedPassword123');

const createUser = async ({ login, password, email }) => {
    const userId = randomUUID();
    const folderPath = path.join(process.cwd(), 'src', 'data', 'users', login);
    const hashedPassword = await hashString(password);
    
    const user = {
        id: userId,
        login,
        email,
        password: hashedPassword,
    };

    try {
        fs.mkdirSync(folderPath);
    } catch {
        throw new Error(`User with login: ${login} already exists`);
    }

    const userFilePath = path.join(folderPath, 'user.json');
    // (Assuming there would be file writing logic here)
    fs.writeFileSync(userFilePath, JSON.stringify(user));
    return user;
};

module.exports = createUser;