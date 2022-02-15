import json
from re import sub

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

from system.window.window import Window, get_stylesheet
from system.utils.message_box import info_box, error_box
from system.utils.strength_verificator import strength_level

class Register(Window):
    def __init__(self):
        super().__init__("Enregister", 550, 270)
        self.create_widget()
    
    def create_widget(self):
        layout = QFormLayout()
        
        title = QLabel("ENREGISTRER")
        title.setStyleSheet(get_stylesheet("title"))
        
        self.origin = QLineEdit()
        self.origin.setPlaceholderText("Site d'origine")
        self.origin.setToolTip("Site d'origine")
        
        self.username_if = QLineEdit()
        self.username_if.setPlaceholderText("Nom d'utilisateur")
        self.username_if.setMaxLength(50)
        self.username_if.setToolTip("Nom d'utilisateur")

        self.password = QLineEdit()
        self.password.setPlaceholderText("Mot de passe")
        self.password.setMaxLength(50)
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setToolTip("Mot de passe")
        self.password.returnPressed.connect(self.add_password)
        self.password.textChanged.connect(self.verify_password)
        
        self.password_strength = QLabel("Très faible")
        self.password_strength.setStyleSheet("color: #800;")
        
        h_layout = QHBoxLayout()
        
        cancel = QPushButton("Annuler")
        cancel.clicked.connect(self.reset)
        cancel.setIcon(QIcon("./images/cancel.png"))
        h_layout.addWidget(cancel)
        
        submit = QPushButton("Enregistrer")
        submit.clicked.connect(self.add_password)
        submit.setStyleSheet(get_stylesheet("validation_button"))
        submit.setIcon(QIcon("./images/save.png"))
        h_layout.addWidget(submit)
        
        layout.addRow(title)
        layout.addRow("Site d'origine", self.origin)
        layout.addRow("Nom d'utilisateur", self.username_if)
        layout.addRow("Mot de passe", self.password)
        layout.addRow("Force", self.password_strength)
        layout.addRow(h_layout)
        
        self.setLayout(layout)
    
    def verify_password(self):
        strength = strength_level(self.password.text())
        
        if strength <= 2:
            self.password_strength.setText("Très faible")
            self.password_strength.setStyleSheet("color: #B00;")
        elif strength <= 4:
            self.password_strength.setText("Faible")
            self.password_strength.setStyleSheet("color: #800;")
        elif strength <= 6:
            self.password_strength.setText("Moyen")
            self.password_strength.setStyleSheet("color: #000;")
        elif strength <= 8:
            self.password_strength.setText("Fort")
            self.password_strength.setStyleSheet("color: #090;")
        else:
            self.password_strength.setText("Très fort")
            self.password_strength.setStyleSheet("color: #090;")
    
    def add_password(self):
        if self.origin.text() == "" or self.username_if.text() == "" or self.password.text() == "":
            error_box("Erreur d'enregistrement", "Veuillez remplir tous les champs afin d'enregistrer un mot de passe.")
            return
        
        with open("./data/passwords.json", "r", encoding="utf8") as f:
            passwords = json.load(f)
            
        if passwords.get(self.username) is None:
            passwords[self.username] = []
        
        passwords[self.username].append({"origin": self.origin.text(), "username": self.username_if.text(), "password": str(self.windows.get('manager').fernet.encrypt(self.password.text(), self.key))})
        
        with open("./data/passwords.json", "w", encoding="utf8") as f:
            json.dump(passwords, f, indent=4)
        
        info_box("Mot de passe enregistré", "Votre nouveau mot de passe a été enregistré avec succès.")
        self.reset()
        self.switch_window("solo_window")
    
    def reset(self):
        self.password.setText("")
        self.origin.setText("")
        self.username_if.setText("")
