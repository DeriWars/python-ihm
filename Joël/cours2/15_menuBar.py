import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


############### fonction ###########

def quitapp():
    app.quit()


##############################
app = QApplication(sys.argv)

window = QMainWindow()
barre_menu = window.menuBar()
barre_menu.addMenu('toto')

# Pour mac os, il faut rajouter la ligne suivante :
# barre_menu.setNativeMenuBar(False)

####################################################

premier = barre_menu.addMenu("Premier")
deuxieme = barre_menu.addMenu("Deuxieme")

premier.addMenu("Créer un fichier")
premier.addMenu("Créer un dossier")
premier.addMenu("Enregistrer")

saveas = premier.addMenu("Enregistrer sous...")
saveas.addAction("format png")
saveas.addAction("format jpg")


quitter = QAction("Quitter")
premier.addAction(quitter)
premier.triggered[QAction].connect(quitapp)


window.show()
sys.exit(app.exec())
