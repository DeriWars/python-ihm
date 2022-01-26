from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from message_box import info_box, warn_box, error_box
from password_generator import PasswordGenerator
from sql import UserDatabase

USERS = UserDatabase("users.db")

# create a class for our main window
class SignupPage(QWidget):
    def __init__(self, next_window=None):
        super().__init__()
        self.next_window = next_window
        self.create_window()
        self.create_widgets()

    def create_window(self):
        self.setWindowTitle("Signup (Password manager - by Pékul)")
        width, height = 450, 260
        self.resize(width, height)
        self.setMinimumSize(width, height)
        self.setMaximumSize(width, height)
        self.setStyleSheet("font-size: 16px;")
    
    def create_widgets(self):
        layout = QFormLayout()
        
        title = QLabel("CREER UN COMPTE")
        self.error = QLabel()
        self.error.setStyleSheet("color: red;")
        
        self.user = QLineEdit()
        
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        
        self.confirm_password = QLineEdit()
        self.confirm_password.setEchoMode(QLineEdit.Password)
        
        submit = QPushButton("Créer un compte")
        submit.clicked.connect(self.submit_clicked)
        
        login = QPushButton("Se connecter")
        login.clicked.connect(self.login_clicked)
        
        layout.addRow(title)
        layout.addRow(self.error)
        layout.addRow("Nom d'utilisateur", self.user)
        layout.addRow("Mot de passe", self.password)
        layout.addRow("Confirmer Mot de passe", self.confirm_password)
        layout.addRow(login)
        layout.addRow(submit)
        
        layout.setSpacing(10)
        self.setLayout(layout)
    
    def submit_clicked(self):
        if USERS.get_user(self.user.text()) != None:
            self.error.setText("Ce nom d'utilisateur est déjà utilisé.")
            return
        
        if self.password.text() != self.confirm_password.text():
            self.error.setText("Les mots de passe ne correspondent pas.")
            return
        
        USERS.add_user(self.user.text(), self.password.text())
        self.error.setText("")
        
        self.login_clicked()
        
    def login_clicked(self):
        if self.next_window != None:
            self.hide_and_reset()
            self.next_window.show()
        else:
            error_box("Erreur", "Aucune fenêtre de destination", details="Il n'y a pas de fenêtre de destination pour la connexion. Ce qui signifie que vous ne pouvez pas être rédirigé vers la page suivante.")
    
    def hide_and_reset(self):
        self.hide()
        self.password.setText("")
        self.confirm_password.setText("")
        self.user.setText("")