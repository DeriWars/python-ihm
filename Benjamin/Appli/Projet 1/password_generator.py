from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

# create a class for our main window
class PasswordGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.create_window()
        self.create_widgets()
        
        self.password_length = 16
        self.generate_password_clicked()
    
    def create_window(self):
        self.setWindowTitle("Generator (Password manager - by Pékul)")
        width, height = 500, 120
        self.resize(width, height)
        self.setMinimumSize(width, height)
        self.setMaximumSize(width, height)
        self.setStyleSheet("font-size: 16px;")
    
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
        
        self.setLayout(layout)
    
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
    
    def test_btn(self):
        self.test.setText(self.test_text_2 if self.test.text() == self.test_text_1 else self.test_text_1)
