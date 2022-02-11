from system.window.window import Window
from PyQt5.QtWidgets import *

class SoloWindow(Window):
    def __init__(self):
        super().__init__("Manager", 1100, 600)
    
    def create_widgets(self):
        h_layout = QHBoxLayout()
        h_layout.addWidget(self.windows.get('manager'))
        
        v_layout = QVBoxLayout()
        v_layout.addWidget(self.windows.get('register'))
        v_layout.addWidget(self.windows.get('generator'))
        
        h_layout.addLayout(v_layout)
        self.setLayout(h_layout)
    
    def update(self):
        self.windows.get('manager').update()
        self.windows.get('register').update()
        self.windows.get('generator').update()