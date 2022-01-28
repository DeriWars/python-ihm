from PyQt5.QtWidgets import QApplication

from system.window.login_page import LoginPage
from system.window.signup_page import SignupPage
from system.window.password_manager import PasswordManager
from system.window.password_generator import PasswordGenerator
from system.window.register import Register

def main():
    app = QApplication([])
    
    login = LoginPage()
    signup = SignupPage()
    pm = PasswordManager()
    pg = PasswordGenerator()
    register = Register()

    login.set_app_windows(login, signup, pm, pg, register)
    signup.set_app_windows(login, signup, pm, pg, register)
    pm.set_app_windows(login, signup, pm, pg, register)
    pg.set_app_windows(login, signup, pm, pg, register)
    register.set_app_windows(login, signup, pm, pg, register)
    
    login.show()
    app.exec_()

if __name__ == "__main__":
    main()