from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QStackedWidget, QWidget, QHBoxLayout, QFrame, QSplitter
from vista.Frames.FrmPrincipal.PnlDerecho import PnlPrincipalDer
from vista.Frames.FrmPrincipal.PnlIzquierdo import PnlPrincipalIzq


class FrmPrincipal(QWidget):
    def __init__(self, p: QStackedWidget):
        super().__init__(parent=p)
        self.layout = QHBoxLayout(self)
        self.pnl_izquierdo = PnlPrincipalIzq(p)
        self.pnl_derecho = PnlPrincipalDer()
        self.splitter = QSplitter(Qt.Horizontal, parent=p)

        self.init_ui()

    def init_ui(self):
        self.pnl_izquierdo.setFrameShape(QFrame.StyledPanel)
        self.pnl_izquierdo.setMaximumWidth(250)
        self.pnl_izquierdo.setMinimumWidth(150)

        self.splitter.addWidget(self.pnl_izquierdo)
        self.splitter.addWidget(self.pnl_derecho)

        self.layout.addWidget(self.splitter)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(self.layout)