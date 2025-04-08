#include <QtTest/QtTest>
#include <QFile>
#include <QByteArray>
#include <QStringList>
#include <QRegularExpression>
#include <QIODevice>

class FileTest : public QObject
{
    Q_OBJECT

private slots:
    void testSplitUsingRegularExpression();

};

void FileTest::testSplitUsingRegularExpression()
{
    QByteArray content = "eth0: 1000 2000 3000 4000 5000 6000 7000 8000 9000\n"; 


    // Paste Code here
    QRegularExpression re("\\s{1,}"); // Match 1 or more spaces
    QStringList list = QString(content).split(re);

    QVERIFY(list.size() == 9); // It should split into 9 parts

    QCOMPARE(list.at(0), QString("eth0:"));
    
    QCOMPARE(list.at(1), QString("1000"));
}

QTEST_MAIN(FileTest)
#include "filetest.moc"
