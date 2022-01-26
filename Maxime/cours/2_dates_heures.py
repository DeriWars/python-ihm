from PyQt5.QtCore import QDate, QTime, QDateTime, Qt, QLocale


print(QDate.currentDate())
print(QDate.currentDate().toString(Qt.DefaultLocaleLongDate))
print(QDateTime.currentDateTime().toString())
print(QDate(2002, 9, 12).dayOfWeek())
print(QDate.longDayName(5))

locale = QLocale(QLocale.English)
date_heure = QDateTime.currentDateTime()
print(locale.toString(date_heure, QLocale.LongFormat))