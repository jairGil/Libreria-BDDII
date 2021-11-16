from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QStackedWidget, QWidget, QHBoxLayout, QFrame, QSplitter
from controlador.Conexion import Conexion
from vista.Frames.FrmPrincipal.PnlDerecho import PnlPrincipalDer
from vista.Frames.FrmPrincipal.PnlIzquierdo import PnlPrincipalIzq


class FrmPrincipal(QWidget):
    def __init__(self, conexion: Conexion, p: QStackedWidget):
        super().__init__(parent=p)

        self.conexion = conexion

        self.layout = QHBoxLayout(self)
        self.pnl_izquierdo = PnlPrincipalIzq(p)
        self.pnl_derecho = PnlPrincipalDer(self.conexion, p)
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

        self.set_acciones()

    
    def set_acciones(self):
        for btn in self.pnl_izquierdo.buttons:
            btn.clicked.connect(self.cambio_pagina)
        self.pnl_izquierdo.btn_salir.clicked.connect(self.btn_salir_click)

    def cambio_pagina(self):
        if self.pnl_izquierdo.btn_inicio.isChecked():
            self.pnl_derecho.stack.setCurrentIndex(0)
        if self.pnl_izquierdo.btn_reportes.isChecked():
            self.pnl_derecho.stack.setCurrentIndex(1)
        if self.pnl_izquierdo.btn_facturacion.isChecked():
            self.pnl_derecho.stack.setCurrentIndex(2)
        if self.pnl_izquierdo.btn_librerias.isChecked():
            self.pnl_derecho.stack.setCurrentIndex(3)
        if self.pnl_izquierdo.btn_libros.isChecked():
            self.pnl_derecho.stack.setCurrentIndex(4)
        if self.pnl_izquierdo.btn_encargados.isChecked():
            self.pnl_derecho.stack.setCurrentIndex(5)
    
    def btn_salir_click(self):
        self.parent().setCurrentIndex(0)