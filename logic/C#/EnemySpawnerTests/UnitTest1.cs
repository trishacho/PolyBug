using System.Collections;
// Dummy SpawnEnemy for unit testing

public class EnemySpawnerTests
{
    [Test]
    public void SpawnEnemies_SpawnsExactlyNumEnemiesPlusOne()
    {
        // Arrange
        var spawner = new EnemySpawner();
        int numEnemies = 5;
        int enemyType = 1;
        float spawnDelay = 1.0f;
        
        var enumerator = spawner.SpawnEnemies(numEnemies, spawnDelay, enemyType);
        while (enumerator.MoveNext()) { }  // Run the coroutine to completion
        
        // Assert
        Assert.That(numEnemies, Is.EqualTo(spawner.numEnemiesSpawned));
    }
}