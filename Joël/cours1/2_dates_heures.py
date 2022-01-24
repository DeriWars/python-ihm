from PyQt5.QtCore import QDate, QTime, QDateTime, Qt

### date ####

print(QDate.currentDate())

print(QDate.currentDate().year())
print(QDate.currentDate().month())
print(QDate.currentDate().day())


print( QDate.currentDate().toString( Qt.ISODate))

print(QDate.currentDate().toString(Qt.DefaultLocaleLongDate))

print(QDateTime.currentDateTime())

print(QDate.currentDate().toString(Qt.ISODate))

print(QDateTime.currentDateTime().toString(Qt.DefaultLocaleLongDate))


### heure ####

print(QTime.currentTime())
print(QTime.currentTime().toString( Qt.ISODate))
print(QTime.currentTime().toString(Qt.DefaultLocaleLongDate))


### Récupérer de l'information ####

print(QDate(2002, 6, 7).daysInMonth())
print(QDate(2002, 6, 7).daysInYear())

print(QDate(2000, 6, 7).dayOfYear())
print(QDate(2000, 6, 7).day())
print(QDate(2000, 6, 7).dayOfWeek()) # lundi = 1
print(QDate.currentDate().dayOfWeek())
print(QDate(2000, 6, 7).daysTo(QDate(2000, 8, 23)))
print(QDate(2000, 6, 8).longDayName(1)) # attention
# longDayName est une méthode de classe : elle n'a pas


#### à voir après QLineEdit.py ###

from PyQt5.QtCore import QLocale

locale = QLocale(QLocale.French)

date_heure = QDateTime.currentDateTime()
print(locale.toString(date_heure, QLocale.LongFormat))

# attention, ce format va devenir obsolète
# il vaut utiliser

print(QLocale().toString(date_heure, QLocale.LongFormat))
print(QLocale(QLocale.French).toString(date_heure, QLocale.LongFormat))
print(QLocale(QLocale.Chinese).toString(date_heure, QLocale.LongFormat))
print(QLocale(QLocale.Portuguese).toString(date_heure, QLocale.LongFormat))


