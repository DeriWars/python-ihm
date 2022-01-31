import json

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from system.window.window import Window
from system.message_box import info_box

from system.window.style import Style

# create a class for our main window
class PasswordManager(Window):
    def __init__(self):
        super().__init__("Gandalf (by Pékul)", 1000, 550)
        self.create_widget()
        self.update()

    def create_widget(self):
        layout = QFormLayout()
        layout.setSpacing(10)
        
        title = QLabel("Gestionnaire de mots de passe")
        layout.addRow(title)
        
        self.scroll_bar = QScrollArea()
        self.scroll_area_widget = QWidget()
        self.scroll_area = QFormLayout()
        
        self.scroll_bar.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll_bar.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_bar.setWidgetResizable(True)
        layout.addRow(self.scroll_bar)
        
        self.scroll_area.setSpacing(30)
        
        self.scroll_area_widget.setLayout(self.scroll_area)
        self.scroll_bar.setWidget(self.scroll_area_widget)
        
        self.central_widget.setLayout(layout)
 
    def update(self):
        with open("./data/passwords.json", "r", encoding="utf8") as f:
            data = json.load(f)
            passwords = data.get(self.username, [])
            self.clear_layout(self.scroll_area)
            
            for password in passwords:
                row = self.create_password_item(password["origin"], password["username"], password["password"])
                row.setStyleSheet(Style.QRadioButton + Style.QLineEdit + Style.QLabel)
                self.scroll_area.addRow(row)
    
    def clear_layout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            
            if child.widget() is not None:
                child.widget().close()
                layout.removeWidget(child.widget())
            elif child.layout() is not None:
                self.clear_layout(child.layout())
    
    def create_password_item(self, identifier, username, password):
        widget = QWidget()
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
        
        widget.setLayout(layout)
        return widget
    
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
    
    def delete_password(self, identifier, username, password):
        with open("./data/passwords.json", "r", encoding="utf8") as f:
            passwords = json.load(f)
            
        del passwords[self.username][passwords[self.username].index({"origin": identifier, "username": username, "password": password})]
        
        with open("./data/passwords.json", "w", encoding="utf8") as f:
            json.dump(passwords, f, indent=4)
        
        self.update()
