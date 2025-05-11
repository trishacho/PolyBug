using System.Collections;

public class WaitForSeconds
{
    public float Duration { get; }
    public WaitForSeconds(float duration) => Duration = duration;
}

public class EnemySpawner
{
    public int numEnemiesSpawned = 0;
    
    public void SpawnEnemy(int enemyType)
    {
        numEnemiesSpawned += 1;
    }
    
    public IEnumerator SpawnEnemies(int numEnemies, float timeToSpawn, int enemyType)
    {
        for (int count = 1; count < numEnemies; count++)
        {
            SpawnEnemy(enemyType);
            yield return new WaitForSeconds(timeToSpawn / count);
        }
        SpawnEnemy(enemyType);
    }
}