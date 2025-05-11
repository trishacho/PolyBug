const PathResolver = require('./helpers/resolvePath');

describe('resolvePath', () => {
    let resolver;
    
    beforeEach(() => {
        resolver = new PathResolver();
        // Mock locateFile before each test
        resolver.locateFile = jest.fn();
    });

    test('returns currentPath when provided', async () => {
        const result = await resolver.resolvePath(['any'], 'current', 'default');
        expect(result).toBe('current');
    });

    test('returns located path when file is found', async () => {
        // Mock locateFile to return a found path
        resolver.locateFile.mockResolvedValue('found/path');
        const result = await resolver.resolvePath(['a'], undefined, 'default');
        expect(result).toBe('found/path');
    });

    test('returns defaultPath when file not found', async () => {
        // Mock locateFile to return null (not found)
        resolver.locateFile.mockResolvedValue(null);
        const result = await resolver.resolvePath(['bad/path'], undefined, 'default/path');
        expect(result).toBe('default/path'); // Now passes with correct implementation
    });

    test('returns defaultPath when paths empty and file not found', async () => {
        resolver.locateFile.mockResolvedValue(null);
        const result = await resolver.resolvePath([], undefined, 'default/path');
        expect(result).toBe('default/path'); // Now passes with correct implementation
    });
});