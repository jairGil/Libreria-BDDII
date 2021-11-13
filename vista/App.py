from PyQt5.QtWidgets import QDesktopWidget, QStackedWidget, QWidget
from vista.Frames.FrmConexion import FrmConexion
from vista.Frames.FrmPrincipal.FrmPrincipal import FrmPrincipal


class App(QStackedWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setStyleSheet("""
                            QFrame {
                                background-color: #FFFFFF;
                            }""")

        self.frm2 = FrmConexion(self)
        self.addWidget(self.frm2)
        self.addWidget(FrmPrincipal(self))

        self.show()
        self.centrar_ventana()

    def centrar_ventana(self):
        # Obtener tamaño de pantalla
        pantalla = QDesktopWidget().screenGeometry()
        # Obtener el tamaño de la ventana
        ventana = self.geometry()
        # Mueva la ventana al centro de la pantalla
        self.move(int((pantalla.width() - ventana.width()) / 2), int((pantalla.height() - ventana.height()) / 2) - 30)


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication, QStackedWidget
    import sys

    app = QApplication(sys.argv)
    frm = App()
    sys.exit(app.exec_())