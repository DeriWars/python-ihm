from PyQt5.QtWidgets import QApplication

from system.window.login_page import LoginPage
from system.window.signup_page import SignupPage
from system.window.password_manager import PasswordManager
from system.window.password_generator import PasswordGenerator
from system.window.register import Register
from system.window.tray import Tray

def main():
    app = QApplication([])
    
    login = LoginPage()
    signup = SignupPage()
    pm = PasswordManager()
    pg = PasswordGenerator()
    register = Register()
    tray = Tray(login, pm, pg, register)

    login.set_app_windows(login, signup, pm, pg, register, tray)
    signup.set_app_windows(login, signup, pm, pg, register, tray)
    pm.set_app_windows(login, signup, pm, pg, register, tray)
    pg.set_app_windows(login, signup, pm, pg, register, tray)
    register.set_app_windows(login, signup, pm, pg, register, tray)
    
    login.show()
    app.exec_()

if __name__ == "__main__":
    main()