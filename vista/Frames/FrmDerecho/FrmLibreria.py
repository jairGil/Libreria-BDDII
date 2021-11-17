from PyQt5.QtWidgets import QGridLayout, QTabWidget
from vista.Frames.FrmDerecho.Consulta import Consulta

from vista.Frames.FrmDerecho.Libreria.AltaLibreria import AltaLibreria
from vista.Frames.FrmDerecho.Libreria.BajaLibreria import BajaLibreria
from vista.Frames.FrmDerecho.Libreria.CambioLibreria import CambioLibreria
from vista.Frames.FrmDerecho.Libreria.ConsultaLibreria import ConsultaLibreria


class FrmLibreria(QTabWidget):
    def __init__(self, p):
        super().__init__(parent=p)
        self.alta = AltaLibreria(self)
        self.baja = BajaLibreria(self)
        self.cambio = CambioLibreria(self)
        self.consulta = ConsultaLibreria(self)
        self.reporte = Consulta()
        self.layout = QGridLayout(self)
        self.setup_ui()

    def setup_ui(self):
        self.addTab(self.alta, "Alta")
        self.addTab(self.baja, "Baja")
        self.addTab(self.cambio, "Cambio")
        self.addTab(self.consulta, "Consulta")
        self.addTab(self.reporte, "Reporte")
