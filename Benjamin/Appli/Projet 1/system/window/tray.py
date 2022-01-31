from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 

from system.message_box import error_box

class Tray(QSystemTrayIcon):
    def __init__(self, login, manager, generator, register):
        super().__init__()
        icon = QIcon("./images/icon.png")
        self.setIcon(icon)
        self.setVisible(False)
        
        self.login = login
        self.manager = manager
        self.generator = generator
        self.register = register
        
        menu = QMenu()
        menu.addAction("Gandalf (v1.0)", lambda: print("Gandalf"))
        menu.addAction("by Pékul", lambda: print("Gandalf"))
        menu.addSeparator()
        menu.addAction("Gé&rer", self.show_manager)
        menu.addAction("&Générer", self.generate_password)
        menu.addAction("&Enregistrer", self.register_password)
        menu.addSeparator()
        menu.addAction("&Déconnexion", self.disconnect)
        menu.addAction("&Quitter", QApplication.quit)
        
        self.setContextMenu(menu)
        self.set_user_name(None)
        
    def set_user_name(self, username):
        self.username = username
    
    def hide_all_windows(self):
        if self.login is not None: self.login.hide()
        if self.manager is not None: self.manager.hide()
        if self.generator is not None: self.generator.hide()
        if self.register is not None: self.register.hide()
    
    def disconnect(self):
        if self.login is not None:
            self.hide_all_windows()
            self.login.show()
            self.setVisible(False)
        else:
            error_box("Erreur",
                      "Impossible de vous rediriez vers la page de connexion.",
                      details="Aucune page de connexion trouvée.")
    
    def generate_password(self):
        if self.username is None:
            error_box("Erreur", "Vous devez être connecté pour générer un mot de passe.")
            self.disconnect()
            return
        
        if self.generator is not None:
            self.hide_all_windows()
            self.generator.show()
            self.setVisible(False)
        else:
            error_box("Erreur",
                      "Impossible de vous rediriez vers la page de génération.",
                      details="Aucune page de génération trouvée.")
    
    def register_password(self):
        if self.username is None:
            error_box("Erreur", "Vous devez être connecté pour enregistrer un mot de passe.")
            self.disconnect()
            return
        
        if self.register is not None:
            self.hide_all_windows()
            self.register.show()
            self.setVisible(False)
        else:
            error_box("Erreur",
                      "Impossible de vous rediriez vers la page d'enregistrement.",
                      details="Aucune page d'enregistrement trouvée.")
    
    def show_manager(self):
        if self.username is None:
            error_box("Erreur", "Vous devez être connecté pour gérer vos mots de passe.")
            self.disconnect()
            return
        
        if self.manager is not None:
            self.hide_all_windows()
            self.manager.update()
            self.manager.show()
            self.setVisible(False)
        else:
            error_box("Erreur",
                      "Impossible de vous rediriez vers la page de gestion.",
                      details="Aucune page de gestion trouvée.")