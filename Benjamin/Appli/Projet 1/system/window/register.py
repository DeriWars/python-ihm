import json

from PyQt5.QtWidgets import *

from system.window.window import Window
from system.message_box import info_box, error_box

class Register(Window):
    def __init__(self):
        super().__init__("Gandalf - Enregister (by Pékul)", 550, 270)
        self.create_widget()
    
    def create_widget(self):
        layout = QFormLayout()
        
        title = QLabel("ENREGISTRER")
        
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
        
        submit = QPushButton("Enregistrer")
        submit.clicked.connect(self.add_password)
        
        cancel = QPushButton("Annuler")
        cancel.clicked.connect(self.reset)
        
        layout.addRow(title)
        layout.addRow("Site d'origine", self.origin)
        layout.addRow("Nom d'utilisateur", self.username_if)
        layout.addRow("Mot de passe", self.password)
        layout.addRow(submit)
        layout.addRow(cancel)
        
        self.setLayout(layout)
    
    def add_password(self):
        if self.origin.text() == "" or self.username_if.text() == "" or self.password.text() == "":
            error_box("Erreur d'enregistrement", "Veuillez remplir tous les champs afin d'enregistrer un mot de passe.")
            return
        
        with open("./data/passwords.json", "r", encoding="utf8") as f:
            passwords = json.load(f)
            
        if passwords.get(self.username) is None:
            passwords[self.username] = []
        
        passwords[self.username].append({"origin": self.origin.text(), "username": self.username_if.text(), "password": str(self.windows.get('manager').fernet.encrypt(self.password.text()))})
        
        with open("./data/passwords.json", "w", encoding="utf8") as f:
            json.dump(passwords, f, indent=4)
        
        info_box("Mot de passe enregistré", "Votre nouveau mot de passe a été enregistré avec succès.")
        self.reset()
        self.switch_window("solo_window")
    
    def reset(self):
        self.password.setText("")
        self.origin.setText("")
        self.username_if.setText("")