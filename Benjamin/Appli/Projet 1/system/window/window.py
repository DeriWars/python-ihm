import json
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from system.utils.message_box import error_box

def get_stylesheet(stylesheet_name = "base"):
    with open(f"./css/{stylesheet_name}.css", "r", encoding="utf8") as f:
        return f.read()

class GandalfWindow(QStackedWidget):
    def __init__(self, tray):
        super().__init__()
        self.tray = tray
        self.width, self.height = 0, 0
        self.create_menu()
        self.windows = []
        
    def create_menu(self):
        menu = QMenuBar()
        file_menu = menu.addMenu("&Fichier")
        file_menu.addAction(QIcon("./images/logout.png"), "&Déconnexion", lambda: self.get_current_window().switch_window("login"))
        file_menu.addAction(QIcon("./images/quit.png"), "&Quitter", QApplication.quit)
        manager_menu = menu.addMenu("&Gestionnaire")
        manager_menu.addAction(QIcon("./images/cancel.png"), "&Réinitialiser", lambda: self.reset_manager())
        self.layout().setMenuBar(menu)
    
    def set_app_windows(self, windows):
        for window in windows:
            self.windows.append(window)
            self.addWidget(window)
        
        self.switch_window(windows[0])
    
    def modify_window(self, title, width, height):
        self.setWindowTitle(title)
        self.setParent(None)
        
        if self.width != width or self.height != height:
            self.width, self.height = width, height
            self.setMinimumSize(width, height)
            self.resize(width, height)
            
            
            rectangle = self.frameGeometry()
            centerPoint = QDesktopWidget().availableGeometry().center()
            rectangle.moveCenter(centerPoint)
            self.move(rectangle.topLeft())
            
        self.setWindowIcon(QIcon('./images/icon.png'))
        
        
    
    def switch_window(self, window):
        self.setCurrentWidget(window)
        self.modify_window(window.title, window.width, window.height)
    
    def get_current_window(self):
        return self.windows[self.currentIndex()]
    
    def reset_manager(self):
        if self.get_current_window().username is not None:
            with open("./data/passwords.json", "r", encoding="utf8") as f:
                data = json.load(f)
            
            if data.get(self.get_current_window().username, "") != "":
                del data[self.get_current_window().username]
                
                with open("./data/passwords.json", "w", encoding="utf8") as f:
                    json.dump(data, f, indent=4)
                
                self.currentWidget().update()
    
    def show(self):
        if self.tray is not None:
            self.tray.setVisible(False)
            
        super().show()
    
    def hide(self):
        if self.tray is not None:
            self.tray.setVisible(True)
            
        return super().hide()
    
    def closeEvent(self, event):
        if self.tray is not None:
            self.hide()
            event.ignore()
        else:
            event.accept()
            return super().closeEvent(event)

class Window(QWidget):
    def __init__(self, title, width, height):
        super().__init__()
                
        self.title = title + " (Gandalf • 2022.02.10 • par Pékul)"
        self.width = width
        self.height = height
        
        self.username = None
        
        self.set_app_windows(None, None, None, None, None, None, None)
        self.setStyleSheet(get_stylesheet())
    
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
    
    def reset_all(self):
        for name, window in self.windows.items():
            window.reset()
            window.set_username(None)
    
    def switch_window(self, window_name):
        next_window = self.windows.get(window_name, None) if window_name in 'login signup' else self.windows.get('solo_window', None)
        
        if next_window is self:
            return
        
        if next_window is not None:
            self.app.get_current_window().reset()
            
            next_window.update()
            self.app.switch_window(next_window)
            
            if window_name == 'login':
                self.reset_all()
        else:
            error_box("Erreur", f"Impossible de vous rediriez vers la fenêtre '{window_name}'.")
    
    def set_username(self, username):
        for name, window in self.windows.items():
            window.username = username
    
    def create_widgets(self):
        pass
    
    def reset(self):
        pass
    
    def update(self):
        pass
