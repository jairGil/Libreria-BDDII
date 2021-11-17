from PyQt5.QtWidgets import QFrame, QGridLayout, QSpacerItem, QSizePolicy, QStackedWidget, QLabel, QWidget
from controlador.Conexion import Conexion
from controlador.DML import DML
from vista.Frames.FrmDerecho.Consulta import Consulta

from vista.Frames.FrmDerecho.FrmConsultaFechas import FrmConsultaFechas
from vista.Frames.FrmDerecho.FrmFacturas import FrmFacturas


class PnlPrincipalDer(QFrame):
    def __init__(self, conexion: Conexion, p):
        super().__init__(parent=p)
        self.grid_layout = QGridLayout(self)
        self.stack = QStackedWidget(self)
        self.conex = conexion
        dml = DML(self.conex)
        self.pagina_inicio = QWidget()
        self.pagina_reportes = FrmConsultaFechas()
        self.pagina_facturacion = FrmFacturas(self)
        self.pagina_librerias = Consulta()
        self.pagina_libros = Consulta()
        self.pagina_encargados = Consulta()
        self.setup_ui()

    def setup_ui(self):
        self.setStyleSheet("QFrame{background-color: #ECEFF1;}")

        self.stack.setMinimumSize(900, 600)
        self.stack.addWidget(self.pagina_inicio) # Reportes semanales
        self.stack.addWidget(self.pagina_reportes) # Reportes personalizados
        self.stack.addWidget(self.pagina_facturacion) # Facturacion
        self.stack.addWidget(self.pagina_librerias) # Cambio de precios de los libros
        self.stack.addWidget(self.pagina_libros)
        self.stack.addWidget(self.pagina_encargados)
        self.grid_layout.addWidget(self.stack,0, 0)


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    frm = PnlPrincipalDer()
    frm.show()
    sys.exit(app.exec_())