from PyQt5.QtWidgets import QApplication

from system.window.login_page import LoginPage
from system.window.signup_page import SignupPage
from system.window.password_manager import PasswordManager
from system.window.password_generator import PasswordGenerator
from system.window.register import Register
from system.window.tray import Tray
from system.window.solo_window import SoloWindow
from system.window.window import GandalfWindow

from system.auto_installer import auto_install_package

def main():
    auto_install_package(["pyqt5", "beautifulsoup4", "requests", "pyperclip", "requests_html"])
    
    app = QApplication([])
    
    login = LoginPage()
    signup = SignupPage()
    pm = PasswordManager()
    pg = PasswordGenerator()
    register = Register()
    tray = Tray(login, pm, pg, register)
    solo_window = SoloWindow()
    main_window = GandalfWindow(login, tray)

    login.set_app_windows(main_window, login, signup, pm, pg, register, solo_window, tray)
    signup.set_app_windows(main_window, login, signup, pm, pg, register, solo_window, tray)
    pm.set_app_windows(main_window, login, signup, pm, pg, register, solo_window, tray)
    pg.set_app_windows(main_window, login, signup, pm, pg, register, solo_window, tray)
    register.set_app_windows(main_window, login, signup, pm, pg, register, solo_window, tray)
    solo_window.set_app_windows(main_window, login, signup, pm, pg, register, solo_window, tray)
    
    solo_window.create_widgets()
    
    main_window.modify_window(login.title, login.width, login.height)
    main_window.show()
    app.exec_()

if __name__ == "__main__":
    main()