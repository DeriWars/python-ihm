from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from message_box import info_box, warn_box, error_box
from password_generator import PasswordGenerator

# create a class for our main window
class LoginPage(QWidget):
    def __init__(self, next_window=None):
        super().__init__()
        self.next_window = next_window
        self.create_window()
        self.create_widgets()

    def create_window(self):
        self.setWindowTitle("Login (Password manager - by Pékul)")
        width, height = 450, 220
        self.resize(width, height)
        self.setMinimumSize(width, height)
        self.setMaximumSize(width, height)
        self.setStyleSheet("font-size: 16px;")
    
    def create_widgets(self):
        layout = QFormLayout()
        
        title = QLabel("CONNEXION")
        self.error = QLabel()
        self.error.setStyleSheet("color: red;")
        
        self.user = QLineEdit()
        
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        
        submit = QPushButton("Connexion")
        submit.clicked.connect(self.submit_clicked)
        
        signup = QPushButton("Créer un compte")
        signup.clicked.connect(self.signup_clicked)
        
        layout.addRow(title)
        layout.addRow(self.error)
        layout.addRow("Nom d'utilisateur", self.user)
        layout.addRow("Mot de passe", self.password)
        layout.addRow(signup)
        layout.addRow(submit)
        
        layout.setSpacing(10)
        self.setLayout(layout)
    
    def submit_clicked(self):
        if self.user.text() == "admin" and self.password.text() == "admin":
            
            if self.next_window != None:
                self.hide()
                self.next_window.show()
            else:
                error_box("Erreur", "Aucune fenêtre de destination", details="Il n'y a pas de fenêtre de destination pour la connexion. Ce qui signifie que vous ne pouvez pas être rédirigé vers la page suivante.")
        else:
            self.error.setText("Nom d'utilisateur ou mot de passe incorrect")
    
    def signup_clicked(self):
        error_box("Erreur", "Fonctionnalité non implémentée", details="La fonctionnalité de création de compte n'est pas encore implémentée.")
        # self.hide()
        # Signup().show()


def main():
    app = QApplication([])
    password_generator = PasswordGenerator()
    login = LoginPage(password_generator)
    login.show()
    app.exec_()

main()
