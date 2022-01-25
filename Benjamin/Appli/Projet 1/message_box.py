from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

def info_box(name, description, callback=None):
    info = QMessageBox()  # create an instance of it
    
    info.setIcon(QMessageBox.Information)  # set icon
    info.setWindowTitle("Password manager - by Pékul") # set title
    info.setText(name) # set text
    info.setInformativeText(description) # set information under the main text
    info.setStandardButtons(QMessageBox.Ok) # type of buttons associated
    
    if callback is not None: info.buttonClicked.connect(callback)  # connect clicked signal
    info.exec_() # get the return value

def warn_box(name, description, details=None, callback=None):
    info = QMessageBox()  # create an instance of it
    
    info.setIcon(QMessageBox.Warning) # set icon
    info.setWindowTitle("Password manager - by Pékul") # set title
    info.setText(name) # set text
    info.setInformativeText(description) # set information under the main text
    info.setStandardButtons(QMessageBox.Ok) # type of buttons associated
    
    if details is not None: info.setDetailedText(details) # a button for more details will add in
    if callback is not None: info.buttonClicked.connect(callback)  # connect clicked signal
    
    info.exec_() # get the return value

def error_box(name, description, details=None, callback=None):
    info = QMessageBox()  # create an instance of it
    
    info.setIcon(QMessageBox.Critical)  # set icon
    info.setWindowTitle("Password manager - by Pékul") # set title
    info.setText(name) # set text
    info.setInformativeText(description) # set information under the main text
    info.setStandardButtons(QMessageBox.Ok) # type of buttons associated
    
    if details is not None: info.setDetailedText(details) # a button for more details will add in
    if callback is not None: info.buttonClicked.connect(callback)  # connect clicked signal
    
    info.exec_() # get the return value
