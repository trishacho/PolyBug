#include <QtTest>
#include <QFile>
#include <QByteArray>
#include <QStringList>
#include <QRegularExpression>
#include <QRegExp> 
#include <QIODevice>

QStringList changeRegex(QFile tempFile) {
    QByteArray l = tempFile.readLine();
    QRegularExpression re("\\s+");
    QStringList list = QString(l).split(re);
    return list;
}