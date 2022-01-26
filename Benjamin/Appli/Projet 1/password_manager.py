import json

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from message_box import info_box, warn_box, error_box
from password_generator import PasswordGenerator
from login_page import LoginPage
from signup_page import SignupPage

# create a class for our main window
class PasswordManager(QWidget):
    def __init__(self, login=None, generator=None):
        super().__init__()
        self.login = login
        self.generator = generator
        self.create_window()
        self.update()

    def create_window(self):
        self.setWindowTitle("Password manager - by Pékul")
        width, height = 700, 350
        self.resize(width, height)
        self.setMinimumSize(width, height)
        self.setStyleSheet("font-size: 16px;")
        
        layout = QFormLayout()
        layout.setSpacing(10)
        
        h_layout = QHBoxLayout()
        title = QLabel("Gestionnaire de mots de passe")
        
        generator_button = QPushButton("Générer")
        generator_button.clicked.connect(self.generate_password)
        
        register_button = QPushButton("Enregistrer")
        register_button.clicked.connect(self.register_password)
        
        disconnect_button = QPushButton("Déconnexion")
        disconnect_button.clicked.connect(self.disconnect)
        
        h_layout.addWidget(title)
        h_layout.addWidget(generator_button)
        h_layout.addWidget(register_button)
        h_layout.addWidget(disconnect_button)
        
        layout.addRow(h_layout)
        
        self.scrollBar = QScrollArea()
        self.scrollAreaWidget = QWidget()
        self.scrollArea = QFormLayout()
        
        self.scrollBar.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollBar.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollBar.setWidgetResizable(True)
        layout.addRow(self.scrollBar)
        
        self.scrollArea.setSpacing(30)
        
        self.scrollAreaWidget.setLayout(self.scrollArea)    
        self.scrollBar.setWidget(self.scrollAreaWidget)
        
        self.setLayout(layout)
    
    def update(self):
        with open("passwords.json", "r", encoding="utf8") as f:
            passwords = json.load(f)
            self.clear_layout(self.scrollArea)
            
            for password in passwords:
                self.scrollArea.addRow(self.create_password_item(password["identifier"], password["username"], password["password"]))
    
    def clear_layout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            
            if child.widget() is not None:
                child.widget().close()
                layout.removeWidget(child.widget())
            elif child.layout() is not None:
                self.clear_layout(child.layout())
    
    def create_password_item(self, identifier, username, password):
        layout = QFormLayout()
        
        identifier_field = QLineEdit()
        identifier_field.setText(identifier)
        identifier_field.setReadOnly(True)
        layout.addRow("Origine", identifier_field)
        
        h_layout = QHBoxLayout()
        
        username_field = QLineEdit()
        username_field.setText(username)
        username_field.setReadOnly(True)
        
        copy_username = QPushButton("Copier")
        copy_username.clicked.connect(lambda: self.copy_username(username))
        
        h_layout.addWidget(username_field)
        h_layout.addWidget(copy_username)
        layout.addRow("Utilisateur", h_layout)
        
        h_layout = QHBoxLayout()
        
        password_field = QLineEdit()
        password_field.setText(password)
        password_field.setReadOnly(True)
        password_field.setEchoMode(QLineEdit.Password)
        
        copy_password = QPushButton("Copier")
        copy_password.clicked.connect(lambda: self.copy_password(password))
        
        show_password = QRadioButton("Afficher")
        show_password.clicked.connect(lambda: self.show_password(show_password, password_field))
        
        h_layout.addWidget(password_field)
        h_layout.addWidget(show_password)
        h_layout.addWidget(copy_password)
        
        delete_password = QPushButton("Supprimer")
        delete_password.clicked.connect(lambda: self.delete_password(identifier, username, password))
        
        layout.addRow("Mot de passe", h_layout)
        layout.addRow(delete_password)
        
        layout.setVerticalSpacing(2)
        layout.setHorizontalSpacing(10)
        return layout
    
    def copy_username(self, password):
        from pyperclip import copy
        copy(password)
        info_box("Nom d'utilisateur copié !", "Le nom d'utilisateur a été copier dans le presse papier.")
    
    def copy_password(self, password):
        from pyperclip import copy
        copy(password)
        info_box("Mot de passe copié !", "Le mot de passe a été copier dans le presse papier.")
    
    def show_password(self, button, password_field):
        password_field.setEchoMode(QLineEdit.Normal if password_field.echoMode() == QLineEdit.Password else QLineEdit.Password)
    
    def register_password(self):
        pass
    
    def generate_password(self):
        if self.generator is not None:
            self.hide()
            self.generator.show()
        else:
            error_box("Erreur", "Aucune fenêtre de génération n'est disponible.")
    
    def disconnect(self):
        if self.login is not None:
            self.hide()
            self.login.show()
        else:
            error_box("Erreur", "Aucune fenêtre de connexion n'est disponible.")
    
    # def create_password(self):
        # if self.generator == None:
            # self.generator = PasswordGenerator()
        # self.generator.show()
        # self.generator.generate_password.connect(self.add_password)
    
    # def add_password(self, password):
        # with open("passwords.json", "r", encoding="utf8") as f:
            # passwords = json.load(f)
        # passwords.append(password)
        # with open("passwords.json", "w", encoding="utf8") as f:
            # json.dump(passwords, f, indent=4)
        # self.update()
    
    def delete_password(self, identifier, username, password):
        with open("passwords.json", "r", encoding="utf8") as f:
            passwords = json.load(f)
            
        del passwords[passwords.index({"identifier": identifier, "username": username, "password": password})]
        
        with open("passwords.json", "w", encoding="utf8") as f:
            json.dump(passwords, f, indent=4)
        
        self.update()


def main():
    app = QApplication([])
    login = LoginPage()
    signup = SignupPage()
    pg = PasswordGenerator()
    pm = PasswordManager(login, pg)
    
    signup.login = login
    login.signup = signup
    login.next_window = pm
    pg.manager = pm
    
    pm.show()
    app.exec_()

main()
