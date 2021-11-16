from PyQt5.QtWidgets import QDesktopWidget, QStackedWidget, QWidget
from vista.Frames.FrmConexion import FrmConexion
from vista.Frames.FrmPrincipal.FrmPrincipal import FrmPrincipal
from controlador.Conexion import Conexion


class App(QStackedWidget):
    conexion: Conexion

    def __init__(self) -> None:
        super().__init__()
        self.conexion = None
        self.setWindowTitle("GestLib")
        self.setStyleSheet("""
                            QFrame {
                                background-color: #FFFFFF;
                            }""")

        self.frm_conexion = FrmConexion(self)
        self.addWidget(self.frm_conexion)
        self.frm_principal = None

        self.show()
        self.centrar_ventana()

    def centrar_ventana(self):
        # Obtener tamaño de pantalla
        pantalla = QDesktopWidget().screenGeometry()
        # Obtener el tamaño de la ventana
        ventana = self.geometry()
        # Mueva la ventana al centro de la pantalla
        self.move(int((pantalla.width() - ventana.width()) / 2), int((pantalla.height() - ventana.height()) / 2) - 30)
    
    def set_conexion(self, conexion: Conexion):
        self.conexion = conexion
        self.frm_principal = FrmPrincipal(self.conexion, self)
        self.addWidget(self.frm_principal)
        self.setCurrentIndex(1)
        self.centrar_ventana()


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication, QStackedWidget
    import sys

    app = QApplication(sys.argv)
    frm = App()
    sys.exit(app.exec_())