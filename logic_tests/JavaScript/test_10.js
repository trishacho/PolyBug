async function testFallsBackToDefaultWhenPathsDontExist() {
    const result = await rresolvePath(
        ['non/existent/path'],  // paths
        undefined,               // currentPath
        'default/path'           // defaultPath
    );
    assert.equal(result, 'default/path');  // Original would return 'non/existent/path'
}