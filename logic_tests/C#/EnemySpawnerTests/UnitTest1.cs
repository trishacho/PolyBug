using System.Collections;
using NUnit.Framework;

// Dummy SpawnEnemy for unit testing
public class WaitForSeconds
{
    public float Duration { get; }
    public WaitForSeconds(float duration) => Duration = duration;
}
public class EnemySpawner
{
    public int numEnemiesSpawned = 0;
    
    public void SpawnEnemy(int enemyType){
        numEnemiesSpawned += 1;
    }

    public IEnumerator SpawnEnemies(int numEnemies, float timeToSpawn, int enemyType){
        for (int count = 1; count < numEnemies; count++) { 
            SpawnEnemy(enemyType);
            yield return new WaitForSeconds(timeToSpawn / count);
        }
        SpawnEnemy(enemyType);
    }
}

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