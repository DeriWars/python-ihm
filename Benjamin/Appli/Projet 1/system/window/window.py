from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from system.message_box import error_box

def get_stylesheet():
    with open("./stylesheet.css", "r", encoding="utf8") as f:
        return f.read()

class GandalfWindow(QMainWindow):
    def __init__(self, central_widget, tray):
        super().__init__()
        self.tray = tray
        self.central_widget = central_widget
        self.setCentralWidget(central_widget)
        self.create_menu()
        self.setStyleSheet(get_stylesheet())
        
    def create_menu(self):
        menu = self.menuBar()
        file_menu = menu.addMenu("&Fichier")
        file_menu.addAction("&Déconnexion", self.central_widget.disconnect)
        file_menu.addAction("&Quitter", QApplication.quit)
        manager_menu = menu.addMenu("&Gestionnaire")
        manager_menu.addAction("&Gérer", self.central_widget.show_manager)
        manager_menu.addAction("&Générer", self.central_widget.generate_password)
        manager_menu.addAction("&Enregistrer", self.central_widget.register_password)
    
    def modify_window(self, title, width, height):
        self.setWindowTitle(title)
        self.setParent(None)
        self.resize(width, height)
        self.setMinimumSize(width, height)
        self.setStyleSheet("font-size: 16px;")
        self.setWindowIcon(QIcon('./images/icon.png'))
    
    def show(self):
        if self.central_widget.tray is not None:
            self.central_widget.tray.setVisible(False)
            
        super().show()
    
    def closeEvent(self, event):
        if self.tray is not None:
            self.hide()
            self.tray.setVisible(True)
            event.ignore()
        else:
            event.accept()
            return super().closeEvent(event)

class Window(QWidget):
    def __init__(self, title, width, height, multiple_window=True):
        super().__init__()
        self.multiple_window = multiple_window
        self.title = title
        self.width = width
        self.height = height
        
        self.set_app_windows(None, None, None, None, None, None, None)
        self.set_user_name(None)
        self.setStyleSheet(get_stylesheet())
    
    def set_app_windows(self, main_window, login, signup, manager, generator, register, solo_window, tray=None):
        self.main_window = main_window
        self.login = login
        self.signup = signup
        self.manager = manager
        self.generator = generator
        self.register = register
        self.solo_window = solo_window
        self.tray = tray
    
    def disconnect(self):
        if self.login is not None:
            self.manager.set_user_name(None)
            self.register.set_user_name(None)
            self.tray.set_user_name(None)
            
            self.main_window.modify_window(self.login.title, self.login.width, self.login.height)
            self.main_window.setCentralWidget(self.login)
        else:
            error_box("Erreur",
                      "Impossible de vous rediriez vers la page de connexion.",
                      details="Aucune page de connexion trouvée.")
    
    def generate_password(self):
        if self.generator is not None:
            if self.multiple_window:
                self.main_window.modify_window(self.generator.title, self.generator.width, self.generator.height)
                self.main_window.setCentralWidget(self.generator)
            else:
                self.main_window.modify_window(self.solo_window.title, self.solo_window.width, self.solo_window.height)
                self.main_window.setCentralWidget(self.solo_window)
        else:
            error_box("Erreur",
                      "Impossible de vous rediriez vers la page de génération.",
                      details="Aucune page de génération trouvée.")
    
    def register_password(self):
        if self.register is not None:
            if self.multiple_window:
                self.main_window.modify_window(self.register.title, self.register.width, self.register.height)
                self.main_window.setCentralWidget(self.register)
            else:
                self.main_window.modify_window(self.solo_window.title, self.solo_window.width, self.solo_window.height)
                self.main_window.setCentralWidget(self.solo_window)
        else:
            error_box("Erreur",
                      "Impossible de vous rediriez vers la page d'enregistrement.",
                      details="Aucune page d'enregistrement trouvée.")
    
    def show_manager(self):
        if self.manager is not None:
            self.manager.update()
            
            if self.multiple_window:
                self.main_window.modify_window(self.manager.title, self.manager.width, self.manager.height)
                self.main_window.setCentralWidget(self.manager)
            else:
                self.main_window.modify_window(self.solo_window.title, self.solo_window.width, self.solo_window.height)
                self.main_window.setCentralWidget(self.solo_window)
        else:
            error_box("Erreur",
                      "Impossible de vous rediriez vers la page de gestion.",
                      details="Aucune page de gestion trouvée.")
    
    def signup_clicked(self):
        if self.signup is not None:
            self.main_window.modify_window(self.signup.title, self.signup.width, self.signup.height)
            self.main_window.setCentralWidget(self.signup)
        else:
            error_box("Erreur",
                      "Impossible de vous rediriez vers la page de création de compte.",
                      details="Aucune page de création de compte trouvée trouvée.")
    
    def set_user_name(self, username):
        self.username = username
    
    def closeEvent(self, event):
        if self.tray is not None:
            self.hide()
            self.tray.setVisible(True)
            event.ignore()
        else:
            event.accept()
            return super().closeEvent(event)