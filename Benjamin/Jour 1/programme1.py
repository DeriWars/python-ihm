from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class StyleSheet:
    QLABEL = """
            QLabel
            {
                font-size: 18px;
                color: #FFF;
            }"""
    
    QPUSHBUTTON = """
                QPushButton
                {
                    font-size: 18px;
                    background-color: #F0F0F0;
                    color: #000000;
                    border-radius: 5px;
                    border: 1px solid #000000;
                }"""
    
    QWINDOW = """
            QMainWindow
            {
                font-size: 18px;
                font-family: Arial;
                background-color: #440000;
            }"""
    
    QSLIDER = """
            QSlider
            {
                border-radius: 30px;
            }
            
            QSlider::handle:horizontal
            {
                background-color:#AA0000;
                width: 10%;
                border-radius: 30px;
            }"""

# create a class for our main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.create_window()
        self.create_menu()
        self.create_widgets()
        
        self.password_length = 16
        self.generate_password_clicked()
        
        self.show()
    
    def create_window(self):
        self.setWindowTitle("Password manager")
        width, heigth = 1000, 500
        self.setGeometry(100, 100, width, heigth)
        self.setMinimumSize(width, heigth)
        self.setMaximumSize(width, heigth)
        self.setStyleSheet(StyleSheet.QLABEL + StyleSheet.QPUSHBUTTON + StyleSheet.QWINDOW + StyleSheet.QSLIDER)
    
    def create_menu(self):
        self.menuBar = QMenuBar(self)
        self.menu = QMenu("Fichier", self.menuBar)
        self.menu_generate = self.menu.addAction("Générer")
        self.menu_manager = self.menu.addAction("Manager")
        self.menu.addSeparator()
        self.menu_exit = self.menu.addAction("Quitter")
        self.menuBar.addMenu(self.menu)
        self.setMenuBar(self.menuBar)
    
    def create_widgets(self):
        self.title = QLabel("Mot de passe", self)
        self.title.setGeometry(25, 25, 450, 30)
        
        self.generated_password = QLabel("", self)
        self.generated_password.setGeometry(25, 60, 450, 30)
        
        self.change_length = QSlider(Qt.Horizontal, self)
        self.change_length.setGeometry(25, 95, 370, 20)
        self.change_length.setMinimum(4)
        self.change_length.setMaximum(24)
        self.change_length.setSingleStep(1)
        self.change_length.setValue(16)
        self.change_length.valueChanged.connect(self.change_length_value)
        
        self.length = QLabel("16", self)
        self.length.setGeometry(400, 95, 75, 20)
        
        self.generate_password = QPushButton("Générer le mot de passe", self)
        self.generate_password.setGeometry(25, 120, 370, 60)
        self.generate_password.clicked.connect(self.generate_password_clicked)
        
        self.copy_password = QPushButton("Copier", self)
        self.copy_password.setGeometry(400, 120, 75, 60)
        self.copy_password.clicked.connect(self.copy_password_clicked)
        
        self.test_text_1 = "Lorem ipsum"
        self.test_text_2 = """ Lorem ipsum dolor sit amet,
        consectetur adipiscing elit.
        Sed non risus. Suspendisse lectus tortor,
        dignissim sit amet, adipiscing nec,
        ultricies sed, dolor. Cras elementum ultrices
        diam. Maecenas ligula massa, varius
        a, semper congue, euismod non, mi. Proin
        porttitor, orci nec nonummy molestie,
        enim est eleifend mi, non fermentum diam
        nisl sit amet erat. Duis semper. Duis
        arcu massa, scelerisque vitae, consequat in,
        pretium a, enim. Pellentesque congue."""
        
        self.test = QPushButton(self.test_text_1, self)
        self.test.setGeometry(500, 50, 200, 300)
        self.test.clicked.connect(self.test_btn)
    
    def generate_password_clicked(self):
        from random import choices
        from string import ascii_uppercase, ascii_lowercase, digits, punctuation
        CHARACTERS = ascii_uppercase + ascii_lowercase + digits + punctuation
        self.password = "".join(choices(CHARACTERS, k=self.password_length))
        self.generated_password.setText(self.password)

    def copy_password_clicked(self):
        from pyperclip import copy
        copy(self.password)
    
    def change_length_value(self):
        self.password_length = self.change_length.value()
        self.length.setText(str(self.password_length))
    
    def test_btn(self):
        self.test.setText(self.test_text_2 if self.test.text() == self.test_text_1 else self.test_text_1)

# create an instance of our main window
def main():
    app = QApplication([])
    window = MainWindow()
    app.exec_()
    
main()