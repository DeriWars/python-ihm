from PyQt5.QtWidgets import *

from system.window.window import Window
from system.message_box import error_box
from system.sql import UserDatabase
from system.window.style import Style

USERS = UserDatabase("./data/users.db")

# create a class for our main window
class LoginPage(Window):
    def __init__(self):
        super().__init__("Login (by Pékul)", 550, 190, False)
        self.create_widgets()
    
    def create_widgets(self):
        layout = QFormLayout()
        
        title = QLabel("CONNEXION")
        
        self.user = QLineEdit()
        self.user.setStyleSheet(Style.QLineEdit)
        self.user.setMaxLength(20)
        self.user.setPlaceholderText("Nom d'utilisateur")
        self.user.setToolTip("Nom d'utilisateur")
        
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setStyleSheet(Style.QLineEdit)
        self.password.setMaxLength(30)
        self.password.returnPressed.connect(self.submit_clicked)
        self.password.setPlaceholderText("Mot de passe")
        
        submit = QPushButton("Connexion")
        submit.clicked.connect(self.submit_clicked)
        
        signup_btn = QPushButton("Créer un compte")
        signup_btn.clicked.connect(self.signup_clicked)
        
        layout.addRow(title)
        layout.addRow("Nom d'utilisateur", self.user)
        layout.addRow("Mot de passe", self.password)
        layout.addRow(signup_btn)
        layout.addRow(submit)
        
        layout.setSpacing(5)
        self.central_widget.setLayout(layout)
    
    def submit_clicked(self):
        if USERS.is_valid_user(self.user.text(), self.password.text()):
            self.set_user_name(self.user.text())
            self.manager.set_user_name(self.user.text())
            self.register.set_user_name(self.user.text())
            self.password.setText("")
            self.show_manager()
        else:
            error_box("Nom d'utilisateur ou mot de passe incorrect", "Veuillez vérifier votre nom d'utilisateur et votre mot de passe.")
    
    def signup_clicked(self):
        self.hide()
        self.signup.show()