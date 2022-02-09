from system.window.window import Window
from PyQt5.QtWidgets import *

class SoloWindow(Window):
    def __init__(self):
        super().__init__("Gandalf (by Pékul)", 1000, 500)
    
    def create_widgets(self):
        h_layout = QHBoxLayout()
        h_layout.addWidget(self.manager)
        
        v_layout = QVBoxLayout()
        v_layout.addWidget(self.register)
        v_layout.addWidget(self.generator)
        
        h_layout.addLayout(v_layout)
        self.setLayout(h_layout)