from PyQt5.QtWidgets import QSizePolicy, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QStackedWidget, QSpacerItem
from controlador.Conexion import Conexion
from vista.Dialog.DlgAviso import DlgAviso


"""
    Variables globales
"""
line_edit_default = """
                    QLineEdit{
                        border: 1px solid #7a7a7a;
                        height: 20;
                    }
                    QLineEdit::hover{
                        border: 1px solid #000000;
                    }
                    QLineEdit::focus{
                        border: 1px solid #077cd8;
                    }"""

line_edit_error = """
                    QLineEdit{
                        border: 1px solid red;
                        height: 20;
                    }
                    QLineEdit::hover{
                        border: 1px solid #000000;
                    }
                    QLineEdit::focus{
                        border: 1px solid #077cd8;
                    }"""

class FrmConexion(QWidget):
    __con: Conexion
    estado_con: int

    def __init__(self, p: QStackedWidget):
        super().__init__(parent=p)
        self.layout = QGridLayout(self)
        self.lbl_db = QLabel("Base de Datos", self)
        self.txt_db = QLineEdit(self)
        self.lbl_host = QLabel("Host", self)
        self.txt_host = QLineEdit(self)
        self.lbl_puerto = QLabel("Puerto", self)
        self.txt_puerto = QLineEdit(self)
        self.lbl_usuario = QLabel("Usuario", self)
        self.txt_usuario = QLineEdit(self)
        self.lbl_contrasena = QLabel("Contraseña", self)
        self.txt_contrasena = QLineEdit(self)
        self.btn_conectar = QPushButton("Conectar", self)
        
        self.labels = [self.lbl_db, self.lbl_host, self.lbl_puerto, self.lbl_usuario, self.lbl_contrasena]
        self.txts = [self.txt_db, self.txt_host, self.txt_puerto, self.txt_usuario, self.txt_contrasena]

        self.setup_ui()

    def setup_ui(self):
        self.txt_contrasena.setEchoMode(QLineEdit.Password)

        # Añadiendo Spacers
        self.layout.addItem(QSpacerItem(20, 20, vPolicy=QSizePolicy.Expanding), 0, 1)        
        self.layout.addItem(QSpacerItem(20, 20, vPolicy=QSizePolicy.Expanding), 7, 1)
        self.layout.addItem(QSpacerItem(20, 20, hPolicy=QSizePolicy.Expanding), 1, 0)
        self.layout.addItem(QSpacerItem(20, 20, hPolicy=QSizePolicy.Expanding), 1, 3)

        for i, lbl in enumerate(self.labels):
            self.layout.addWidget(lbl, i + 1, 1)

        for i, txt in enumerate(self.txts):
            self.layout.addWidget(txt, i + 1, 2)
            txt.setStyleSheet(line_edit_default)
            
        self.layout.addWidget(self.btn_conectar, 6, 2)

        self.btn_conectar.clicked.connect(self.conectar)

    def conectar(self):
        campos_llenos = True
        campos_vacios = []
        txt_vacios = ""
        for i, txt in enumerate(self.txts):
            if txt.text() == "":
                campos_vacios.append(txt)
                txt_vacios += f"El campo {self.labels[i].text()} está vacio\n"
                campos_llenos = False

        if campos_llenos:
            for txt in self.txts:
                txt.setStyleSheet(line_edit_default)
            usuario = self.txt_usuario.text()
            contrasena = self.txt_contrasena.text()
            db = self.txt_db.text()
            puerto = self.txt_puerto.text()
            host = self.txt_host.text()

            self.__con = Conexion(db, usuario, contrasena, puerto, host)

            con, txt = self.__con.conectar()

            if con is None:
                DlgAviso(self, txt)
            else:
                self.parent().setCurrentIndex(1)
        else: 
            for txt in self.txts:
                txt.setStyleSheet(line_edit_default)
            for txt in campos_vacios:
                txt.setStyleSheet(line_edit_error)
            DlgAviso(self, txt_vacios)


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    frm = QStackedWidget()
    frm2 = FrmConexion(frm)
    frm.addWidget(frm2)
    frm.show()
    sys.exit(app.exec_())