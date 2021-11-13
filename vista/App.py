from PyQt5.QtWidgets import QStackedWidget
from vista.Frames.FrmConexion import FrmConexion


class App(QStackedWidget):
    def __init__(self) -> None:
        super().__init__()
        self.frm2 = FrmConexion(self)
        self.addWidget(self.frm2)
        self.show()

        self.setStyleSheet("""
                            QFrame {
                                background-color: #FFFFFF;
                            }""")


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication, QStackedWidget
    import sys

    app = QApplication(sys.argv)
    frm = App()
    sys.exit(app.exec_())