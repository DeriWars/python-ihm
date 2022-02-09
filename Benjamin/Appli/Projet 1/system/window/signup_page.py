from PyQt5.QtWidgets import *

from system.window.window import Window
from system.message_box import error_box
from system.sql import UserDatabase

USERS = UserDatabase("./data/users.db")

# create a class for our main window
class SignupPage(Window):
    def __init__(self):
        super().__init__("Gandalf - Création de compte (by Pékul)", 550, 280)
        self.create_widgets()
    
    def create_widgets(self):
        layout = QFormLayout()
        
        title = QLabel("CREER UN COMPTE")
        
        self.user = QLineEdit()
        self.user.setMaxLength(20)
        self.user.setPlaceholderText("Nom d'utilisateur")
        self.user.setToolTip("Nom d'utilisateur")
        
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setMaxLength(30)
        self.password.setPlaceholderText("Mot de passe")
        self.password.setToolTip("Mot de passe")
        
        self.confirm_password = QLineEdit()
        self.confirm_password.setEchoMode(QLineEdit.Password)
        self.confirm_password.setMaxLength(30)
        self.confirm_password.setPlaceholderText("Confirmer le mot de passe")
        self.confirm_password.setToolTip("Confirmer le mot de passe")
        self.confirm_password.returnPressed.connect(self.submit_clicked)
        
        submit = QPushButton("Créer un compte")
        submit.clicked.connect(self.submit_clicked)
        
        login_btn = QPushButton("Se connecter")
        login_btn.clicked.connect(self.login_clicked)
        
        layout.addRow(title)
        layout.addRow("Nom d'utilisateur", self.user)
        layout.addRow("Mot de passe", self.password)
        layout.addRow("Confirmer", self.confirm_password)
        layout.addRow(login_btn)
        layout.addRow(submit)
        
        layout.setSpacing(5)
        self.setLayout(layout)
    
    def submit_clicked(self):
        if USERS.get_user(self.user.text()) != None:
            error_box("Nom d'utilisateur déjà utilisé", "Ce nom d'utilisateur est déjà utilisé par un autre compte.")
            return
        
        if self.password.text() != self.confirm_password.text():
            error_box("Mot de passe incorrect", "Les mots de passe ne correspondent pas.")
            return
        
        USERS.add_user(self.user.text(), self.password.text())        
        self.login_clicked()
        
    def login_clicked(self):
        self.reset()
        self.switch_window("login")
        
    def reset(self):
        self.password.setText("")
        self.confirm_password.setText("")
        self.user.setText("")