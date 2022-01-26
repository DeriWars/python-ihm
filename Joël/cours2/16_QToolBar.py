import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


################# Fonctions ################

def fermer():
    app.quit()

##########################################

app = QApplication(sys.argv)

window = QMainWindow()
toolbar = QToolBar("Fichier")
window.addToolBar(Qt.BottomToolBarArea,toolbar)

# Qt.BottomToolBarArea est optionnel
# Qt.RightToolBarArea
# Qt.LeftToolBarArea

# pour fixer la  taille :
toolbar.setFixedHeight(25)

###############################################
# ne marche qu'avec des .png
sauvegarde = QAction(QIcon("../images/sensei.png"), 'enregistrer')
sortir = QAction(QIcon("../images/Etoiles.png"), 'sortir')

toolbar.addAction(sauvegarde)
toolbar.addAction(sortir)

#############################################

"""
si on met :
toolbar.actionTriggered[QAction].connect(fermer)
toutes les icones vont faire la même action
il faut faire icones par icones
"""

sortir.triggered.connect(fermer)

###### bloquer/libérer la toolbar #######
toolbar.setMovable(False)

window.show()
sys.exit(app.exec())