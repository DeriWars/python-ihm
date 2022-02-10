from PyQt5.QtWidgets import QApplication

from system.window.login_page import LoginPage
from system.window.signup_page import SignupPage
from system.window.password_manager import PasswordManager
from system.window.password_generator import PasswordGenerator
from system.window.register import Register
from system.window.tray import Tray
from system.window.solo_window import SoloWindow
from system.window.window import GandalfWindow

from system.utils.auto_installer import auto_install_package

import sys

def main():
    try: auto_install_package(["pyqt5", "pyperclip"])
    except Exception as e: print(e)
    
    app = QApplication([])
    
    login = LoginPage()
    signup = SignupPage()
    pm = PasswordManager()
    pg = PasswordGenerator()
    register = Register()
    tray = Tray()
    solo_window = SoloWindow()
    main_window = GandalfWindow(tray)

    login.set_app_windows(main_window, login, signup, pm, pg, register, solo_window)
    signup.set_app_windows(main_window, login, signup, pm, pg, register, solo_window)
    pm.set_app_windows(main_window, login, signup, pm, pg, register, solo_window)
    pg.set_app_windows(main_window, login, signup, pm, pg, register, solo_window)
    register.set_app_windows(main_window, login, signup, pm, pg, register, solo_window)
    solo_window.set_app_windows(main_window, login, signup, pm, pg, register, solo_window)
    main_window.set_app_windows([login, signup, solo_window])
    tray.set_app_windows(main_window, login, signup, pm, pg, register, solo_window)
    
    solo_window.create_widgets()
    
    main_window.modify_window(login.title, login.width, login.height)
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()