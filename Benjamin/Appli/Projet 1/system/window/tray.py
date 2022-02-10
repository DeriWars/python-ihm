from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 

from system.utils.message_box import error_box

class Tray(QSystemTrayIcon):
    def __init__(self):
        super().__init__()
        self.setIcon(QIcon("./images/icon.png"))
        self.setVisible(False)
        self.window = {}
        
        menu = QMenu()
        menu.addAction("Gandalf (2022.02.10)")
        menu.addAction("par Pékul")
        menu.addSeparator()
        menu.addAction(QIcon("./images/manage.png"), "&Manager", lambda: self.switch_window("solo_window"))
        menu.addAction(QIcon("./images/logout.png"), "&Déconnexion", lambda: self.switch_window("login"))
        menu.addAction(QIcon("./images/quit.png"), "&Quitter", QApplication.quit)
        
        self.showMessage("Hey!", "Le programme travaille en arrière plan.", QIcon("./images/icon.png"), 2000)
        self.setToolTip("Gandal • par Pékul")
        
        self.setContextMenu(menu)
        self.set_user_name(None)
    
    def set_user_name(self, username):
        self.username = username
    
    def set_app_windows(self, main_window, login, signup, manager, generator, register, solo_window):
        self.app = main_window
        self.windows = {
            'login': login,
            'signup': signup,
            'manager': manager,
            'generator': generator,
            'register': register,
            'solo_window': solo_window
        }
    
    def switch_window(self, window_name):
        if self.windows.get(window_name).username is not None:
            self.app.switch_window(self.windows.get(window_name))
        else:
            self.app.switch_window(self.windows.get('login'))
            
        self.app.show()
