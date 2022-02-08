from PyQt5.QtCore import QDate, QTime, QDateTime, Qt, QLocale


print(1, QDate.currentDate())
print(2, QDate.currentDate().toString(Qt.DefaultLocaleLongDate))
print(3, QDateTime.currentDateTime().toString())
print(4, QDate(2002, 9, 12).dayOfWeek())
print(5, QDate.longDayName(5))

locale = QLocale(QLocale.English)
date_heure = QDateTime.currentDateTime()
print(6, locale.toString(date_heure, QLocale.LongFormat))