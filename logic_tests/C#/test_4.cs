//dummy function to test
public class EnemySpawner(){
    int spawnCount;
    public EnemySpawner(){
        spawnCount = 0;
    }
    public void SpawnEnemies(int num){
        spawnCount += num;
    }
    
}


public class WaitForSeconds(int i){
    private int seconds;
    
    public WaitForSeconds(int i)
    {
        seconds = i;
    }
    
}

public class EnemySpawnerTests
{
    [Test]
    public void SpawnEnemies_SpawnsExactlyNumEnemies()
    {
        // Mock spawner (replace with your actual spawner class)
        var spawner = new EnemySpawner();
        int numEnemies = 5;
        float timeToSpawn = 1f;
        GameObject enemyType = new GameObject(); // Mock enemy prefab

        spawner.SpawnEnemies(numEnemies, timeToSpawn, enemyType);

        Assert.AreEqual(numEnemies, spawner.spawnCount, "Enemy spawned more or fewer times than expected.");
    }
}
