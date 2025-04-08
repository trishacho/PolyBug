using System.Collections;
using NUnit.Framework;
using UnityEngine;
using UnityEngine.TestTools;

public class EnemySpawnerTests
{
    [UnityTest]
    public IEnumerator SpawnEnemies_SpawnsExactlyNumEnemies()
    {
        var spawnerGO = new GameObject();
        var spawner = spawnerGO.AddComponent<EnemySpawner>();

        int numEnemies = 5;
        float timeToSpawn = 1f;
        string enemyType = "Goblin";

        yield return spawner.StartCoroutine(spawner.SpawnEnemies(numEnemies, timeToSpawn, enemyType));

        Assert.AreEqual(numEnemies, spawner.spawnCount, "Enemy spawned more or fewer times than expected.");
    }
}
