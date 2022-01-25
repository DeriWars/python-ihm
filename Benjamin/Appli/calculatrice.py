from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

CSS = """
QLabel
{
    font-size: 30px;
}

QLineEdit
{
    font-size: 70px;
    margin: 0;
    margin-bottom: 25px;
}

QPushButton
{
    font-size: 35px;
}
"""
# create a class for our main window
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.create_window()
        self.create_widgets()
        
        self.calcul = ""
        self.setStyleSheet(CSS)
        self.show()
    
    def create_window(self):
        self.setWindowTitle("Calculatrice - by Pékul")
        width, heigth = 400, 580
        self.setGeometry(100, 100, width, heigth)
        self.setMinimumSize(width, heigth)
    
    def create_widgets(self):
        main_layout = QFormLayout()
        
        self.calcul_label = QLabel("")
        self.calcul_label.setAlignment(Qt.AlignRight)
        
        self.input_field = QLineEdit()
        self.input_field.setAlignment(Qt.AlignRight)
        self.input_field.textEdited.connect(self.register_calcul)
        
        row1 = self.create_row("sqrt", "cos", "sin", "tan")
        row2 = self.create_row("%", "^", "ln", "exp")
        row3 = self.create_row("AC", "(", ")", "/")
        row4 = self.create_row("7", "8", "9", "*")
        row5 = self.create_row("4", "5", "6", "-")
        row6 = self.create_row("1", "2", "3", "+")
        row7 = self.create_row("0", ".", "del", "=")
        
        main_layout.addRow(self.calcul_label)
        main_layout.addRow(self.input_field)
        main_layout.addRow(row1)
        main_layout.addRow(row2)
        main_layout.addRow(row3)
        main_layout.addRow(row4)
        main_layout.addRow(row5)
        main_layout.addRow(row6)
        main_layout.addRow(row7)
        
        self.setLayout(main_layout)
    
    def create_row(self, btn_1, btn_2, btn_3, btn_4):
        row = QHBoxLayout()
        button_1 = QPushButton(btn_1)
        button_1.clicked.connect(lambda: self.append_to_calculator(btn_1))
        row.addWidget(button_1)
        
        button_2 = QPushButton(btn_2)
        button_2.clicked.connect(lambda: self.append_to_calculator(btn_2))
        row.addWidget(button_2)
        
        button_3 = QPushButton(btn_3)
        button_3.clicked.connect(lambda: self.append_to_calculator(btn_3))
        row.addWidget(button_3)
        
        button_4 = QPushButton(btn_4)
        button_4.clicked.connect(lambda: self.append_to_calculator(btn_4))
        row.addWidget(button_4)
        
        return row
    
    def register_calcul(self):
        self.calcul = self.input_field.text()
    
    def append_to_calculator(self, expression: str):
        if expression == "AC":
            self.calcul = ""
        elif expression == "del":
            self.calcul = self.calcul[:-1]
        elif expression == "=":
            self.calcul_label.setText(self.calcul + "=")
            self.result = ""
            
            try:
                from math import sqrt, log, sin, cos, tan, exp
                self.result = str(eval(self.calcul.replace("^", "**").replace("ln", "log")))
                self.calcul = self.result
            except:
                self.result = "ERROR"
            
            self.input_field.setText(self.result)
            return
        else:
            self.calcul += expression
            
        self.input_field.setText(self.calcul)

# create an instance of our main window
def main():
    app = QApplication([])
    window = MainWindow()
    app.exec_()
    
main()