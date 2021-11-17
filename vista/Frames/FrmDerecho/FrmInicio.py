from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGridLayout, QLabel, QWidget


class FrmInicio(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QGridLayout(self)
        self.lbl = QLabel(self)
        self.lbl.setPixmap(QPixmap('vista/img/img.png'))
        self.layout.addWidget(self.lbl, 0, 0)