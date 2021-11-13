from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QDialog, QGridLayout, QLabel, QPushButton, QWidget


class DlgAviso(QDialog):
    def __init__(self,p: QWidget, s: str):
        super().__init__(parent=p)
        self.gridLayout = QGridLayout(self)
        self.lbl_error = QLabel(s, self)
        self.btn_cerrar = QPushButton("Cerrar", self)

        self.setup_ui()
        self.show()

    def setup_ui(self):
        self.resize(350, 250)
        self.setWindowTitle("Informe")
        self.lbl_error.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.lbl_error.setWordWrap(True)
        self.lbl_error.setMargin(30)

        self.setStyleSheet("""
                              QWidget {
                                  background-color: white;
                              }                                        
                              QPushButton {
                                  color: #FFEBEE;
                                  background-color: #D50000;
                                  height: 30;
                              }
                              QPushButton::hover {
                                  color: #FFEBEE;
                                  background-color: #B71C1C;
                                  height: 30;
                              }""")

        font = QFont()
        font.setBold(True)
        font.setWeight(11)
        font.setFamily("Cantarell")
        self.btn_cerrar.setFont(font)

        self.gridLayout.addWidget(self.lbl_error, 0, 0)
        self.gridLayout.addWidget(self.btn_cerrar, 1, 0)

        self.btn_cerrar.clicked.connect(self.cerrar_dlg)

    def cerrar_dlg(self):
        self.close()


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication, QMainWindow
    import sys

    app = QApplication(sys.argv)
    frm = QMainWindow()
    frm.show()
    st = "Este es un mensaje de prueba del texto de la ventana"
    dlg = DlgAviso(st)
    sys.exit(app.exec_())