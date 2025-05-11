#include <QtTest>
#include <QFile>
#include <QByteArray>
#include <QStringList>
#include <QRegularExpression>
#include <QRegExp>
#include <QIODevice>
#include "reg.h"

class NetworkStatParserTest : public QObject
{
    Q_OBJECT

private slots:
    // Test the corrected implementation
    void testFixedImplementation()
    {
        QTemporaryFile tempFile;
        tempFile.open();
        tempFile.write("eth0: 1000 2000 3000\n");
        tempFile.seek(0);

        QStringList list = changeRegex(tempFile);
        // Verify it works correctly
        QCOMPARE(list.size(), 4);
        QCOMPARE(list[0], QString("eth0:"));
        QCOMPARE(list[1], QString("1000"));
    }

    // Test with actual /proc/net/dev format
    void testRealWorldFormat()
    {
        QTemporaryFile tempFile;
        tempFile.open();
        tempFile.write("eth0: 123456 7890 123 456 789 012 345 678 901 23456\n");
        tempFile.seek(0);

        QStringList list = changeRegex(tempFile);
        
        // Typical /proc/net/dev has 17 entries (interface + 16 numbers)
        QCOMPARE(list.size(), 17);
        QVERIFY(list.first().endsWith(":"));
    }
};

QTEST_MAIN(NetworkStatParserTest)
#include "networkstatparsertest.moc"