from PyQt5.QtCore import QDate, QTime, QDateTime, Qt

print(QDate.currentDate())
print(QDate.currentDate().toString(Qt.DefaultLocaleLongDate))
print(QDateTime.currentDateTime().toString())
print(QDate(2002, 9, 12).dayOfWeek())
print(QDate.longDayName(5))
