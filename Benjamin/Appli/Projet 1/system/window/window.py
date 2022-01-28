from PyQt5.QtWidgets import QWidget, QMainWindow
from PyQt5.QtGui import QIcon
from system.message_box import error_box

class Window(QMainWindow):
    def __init__(self, title, width, height, with_menu=True):
        super().__init__()
        self.create_window(title, width, height)
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.set_app_windows(None, None, None, None, None)
        if with_menu: self.create_menu()
        self.set_user_name(None)
    
    def create_window(self, title, width, height):
        self.setWindowTitle(title)
        self.resize(width, height)
        self.setMinimumSize(width, height)
        self.setStyleSheet("font-size: 16px;")
        self.setWindowIcon(QIcon('./images/icon.png'))
    
    def set_app_windows(self, login, signup, manager, generator, register):
        self.login = login
        self.signup = signup
        self.manager = manager
        self.generator = generator
        self.register = register
        
    def create_menu(self):
        menu = self.menuBar()
        file_menu = menu.addMenu("&Fichier")
        file_menu.addAction("&Déconnexion", self.disconnect)
        file_menu.addAction("&Quitter", self.close)
        manager_menu = menu.addMenu("&Gestionnaire")
        manager_menu.addAction("&Gérer", self.show_manager)
        manager_menu.addAction("&Générer", self.generate_password)
        manager_menu.addAction("&Enregistrer", self.register_password)
    
    def disconnect(self):
        if self.login is not None:
            self.hide()
            self.login.show()
        else:
            error_box("Erreur",
                      "Impossible de vous rediriez vers la page de connexion.",
                      details="Aucune page de connexion trouvée.")
    
    def generate_password(self):
        if self.generator is not None:
            self.hide()
            self.generator.show()
        else:
            error_box("Erreur",
                      "Impossible de vous rediriez vers la page de génération.",
                      details="Aucune page de génération trouvée.")
    
    def register_password(self):
        if self.register is not None:
            self.hide()
            self.register.show()
        else:
            error_box("Erreur",
                      "Impossible de vous rediriez vers la page d'enregistrement.",
                      details="Aucune page d'enregistrement trouvée.")
    
    def show_manager(self):
        if self.manager is not None:
            self.hide()
            self.manager.update()
            self.manager.show()
        else:
            error_box("Erreur",
                      "Impossible de vous rediriez vers la page de gestion.",
                      details="Aucune page de gestion trouvée.")
    
    def set_user_name(self, username):
        self.username = username