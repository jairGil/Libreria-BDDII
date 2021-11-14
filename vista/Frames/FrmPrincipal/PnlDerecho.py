from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFrame, QGridLayout, QSpacerItem, QSizePolicy, QStackedWidget, QLabel, QWidget

from vista.Frames.FrmDerecho.FrmConsultaFechas import FrmConsultaFechas


class PnlPrincipalDer(QFrame):
    def __init__(self):
        super().__init__()
        self.grid_layout = QGridLayout(self)
        self.stack = QStackedWidget(self)

        self.setup_ui()

    def setup_ui(self):
        self.setStyleSheet("QFrame{background-color: #ECEFF1;}")

        self.grid_layout.addItem(QSpacerItem(20, 5, vPolicy=QSizePolicy.Minimum), 0, 1)
        self.grid_layout.addItem(QSpacerItem(20, 5, vPolicy=QSizePolicy.Minimum), 2, 1)
        self.grid_layout.addItem(QSpacerItem(5, 5, hPolicy=QSizePolicy.Expanding), 1, 0)
        self.grid_layout.addItem(QSpacerItem(5, 20, hPolicy=QSizePolicy.Expanding), 1, 2)
        self.grid_layout.addWidget(self.stack, 1, 1)

        self.stack.setMinimumSize(900, 600)
        """
        lbl = QLabel("Aqui estoy", self.stack)
        lbl.setAlignment(Qt.AlignCenter)
        """
        self.stack.addWidget(QWidget()) # Reportes semanales
        self.stack.addWidget(FrmConsultaFechas()) # Reportes personalizados
        self.stack.addWidget(QWidget()) # Facturacion
        self.stack.addWidget(QWidget()) # Cambio de precios de los libros


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    frm = PnlPrincipalDer()
    frm.show()
    sys.exit(app.exec_())