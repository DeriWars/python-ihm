from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from system.window.window import Window
from system.message_box import error_box

# create a class for our main window
class PasswordGenerator(Window):
    def __init__(self):
        super().__init__("Générateur (by Pékul)", 500, 180)
        self.create_widgets()
        
        self.password_length = 16
        self.generate_password_clicked()
    
    def create_widgets(self):
        layout = QFormLayout()
         
        self.generated_password = QLineEdit("")
        self.generated_password.setReadOnly(True)
        layout.addRow("Mot de passe", self.generated_password)
        
        h_layout = QHBoxLayout()
        self.change_length = QSlider(Qt.Horizontal)
        self.change_length.setMinimum(4)
        self.change_length.setMaximum(24)
        self.change_length.setSingleStep(1)
        self.change_length.setValue(16)
        self.change_length.valueChanged.connect(self.change_length_value)
        
        self.length = QLabel("16")
        h_layout.addWidget(self.change_length)
        h_layout.addWidget(self.length)
        layout.addRow("Longueur du mot de passe", h_layout)
        
        h_layout = QHBoxLayout()
        generate_password = QPushButton("Générer le mot de passe")
        generate_password.clicked.connect(self.generate_password_clicked)
        
        copy_password = QPushButton("Copier")
        copy_password.clicked.connect(self.copy_password_clicked)
        
        h_layout.addWidget(generate_password)
        h_layout.addWidget(copy_password)
        layout.addRow(h_layout)
        
        back_button = QPushButton("Retour")
        back_button.clicked.connect(self.back)
        layout.addRow(back_button)
        
        self.central_widget.setLayout(layout)
    
    def generate_password_clicked(self):
        from random import choices
        from string import ascii_uppercase, ascii_lowercase, digits, punctuation
        CHARACTERS = ascii_uppercase + ascii_lowercase + digits + punctuation
        self.password = "".join(choices(CHARACTERS, k=self.password_length))
        self.generated_password.setText(self.password)

    def copy_password_clicked(self):
        from pyperclip import copy
        copy(self.password)
    
    def change_length_value(self):
        self.password_length = self.change_length.value()
        self.length.setText(str(self.password_length))
    
    def back(self):
        if self.manager is not None:
            self.hide()
            self.manager.show()
        else:
            error_box("Erreur", "Aucune fenêtre de gestion n'est disponible.")
