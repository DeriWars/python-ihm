from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

from system.window.window import Window, get_stylesheet
from system.utils.message_box import error_box
from system.utils.sql import UserDatabase

USERS = UserDatabase("./data/users.db")

# create a class for our main window
class LoginPage(Window):
    def __init__(self):
        super().__init__("Connexion", 550, 230)
        self.create_widgets()
    
    def create_widgets(self):
        layout = QFormLayout()
        
        title = QLabel("CONNEXION")
        title.setStyleSheet(get_stylesheet("title"))
        
        self.user = QLineEdit()
        self.user.setMaxLength(20)
        self.user.setPlaceholderText("Nom d'utilisateur")
        self.user.setToolTip("Nom d'utilisateur")
        
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setMaxLength(30)
        self.password.returnPressed.connect(self.submit_clicked)
        self.password.setPlaceholderText("Mot de passe")
        
        h_layout = QHBoxLayout()
        
        signup_btn = QPushButton("Créer un compte")
        signup_btn.clicked.connect(lambda: self.switch_window("signup"))
        h_layout.addWidget(signup_btn)
        
        submit = QPushButton("Connexion")
        submit.clicked.connect(self.submit_clicked)
        submit.setStyleSheet(get_stylesheet("validation_button"))
        submit.setIcon(QIcon("./images/login.png"))
        h_layout.addWidget(submit)
        
        layout.addRow(title)
        layout.addRow("Nom d'utilisateur", self.user)
        layout.addRow("Mot de passe", self.password)
        layout.addRow(h_layout)
        
        layout.setSpacing(5)
        self.setLayout(layout)
    
    def submit_clicked(self):
        if USERS.is_valid_user(self.user.text(), self.password.text()):
            self.set_username(self.user.text())
            print(self.username)
            self.switch_window("manager")
        else:
            self.reset()
            error_box("Nom d'utilisateur ou mot de passe incorrect", "Veuillez vérifier votre nom d'utilisateur et votre mot de passe.")

    def reset(self):
        self.user.setText("")
        self.password.setText("")
