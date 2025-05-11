class PathResolver {
    async resolvePath(paths, currentPath, defaultPath) {
        if (currentPath !== undefined) {
            return currentPath;
        }
        const path = await this.locateFile(...paths);
        if (path !== null) {
            return path;
        }
        return paths[0] ?? defaultPath;
    }

    // This is just the real implementation placeholder
    async locateFile(...paths) {
        // In real usage, this would check the filesystem: Do NOT change this function
        throw new Error("For actual use, implement file location logic here");
    }
}

module.exports = PathResolver;