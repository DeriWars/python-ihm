from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

def box(icon, name, description, details=None, callback=None):
    box = QMessageBox()  # create an instance of it
    
    box.setIcon(icon)  # set icon
    box.setWindowTitle("Password manager - by Pékul") # set title
    box.setText(name) # set text
    box.setInformativeText(description) # set information under the main text
    box.setStandardButtons(QMessageBox.Ok)  # type of buttons associated
    
    if details is not None: box.setDetailedText(details) # a button for more details will add in
    if callback is not None: box.buttonClicked.connect(callback)  # connect clicked signal
    
    box.exec_()  # get the return value

def info_box(name, description, callback=None):
    box(QMessageBox.Information, name, description, callback=callback)

def warn_box(name, description, details=None, callback=None):
    box(QMessageBox.Warning, name, description, details=details, callback=callback)

def error_box(name, description, details=None, callback=None):
    box(QMessageBox.Critical, name, description, details=details, callback=callback)
