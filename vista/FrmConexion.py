from PyQt5.QtWidgets import QWidget, QFormLayout, QLabel, QLineEdit, QPushButton, QStackedWidget
from controlador.Conexion import Conexion


class FrmConexion(QWidget):
    __con: Conexion
    estado_con: int

    def __init__(self, p: QStackedWidget):
        super().__init__(parent=p)
        self.form_layout = QFormLayout(self)
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

        self.setup_ui()

    def setup_ui(self):
        self.txt_contrasena.setEchoMode(QLineEdit.Password)

        self.form_layout.setWidget(0, QFormLayout.LabelRole, self.lbl_db)
        self.form_layout.setWidget(0, QFormLayout.FieldRole, self.txt_db)
        self.form_layout.setWidget(1, QFormLayout.LabelRole, self.lbl_host)
        self.form_layout.setWidget(1, QFormLayout.FieldRole, self.txt_host)
        self.form_layout.setWidget(2, QFormLayout.LabelRole, self.lbl_puerto)
        self.form_layout.setWidget(2, QFormLayout.FieldRole, self.txt_puerto)
        self.form_layout.setWidget(3, QFormLayout.LabelRole, self.lbl_usuario)
        self.form_layout.setWidget(3, QFormLayout.FieldRole, self.txt_usuario)
        self.form_layout.setWidget(4, QFormLayout.LabelRole, self.lbl_contrasena)
        self.form_layout.setWidget(4, QFormLayout.FieldRole, self.txt_contrasena)
        self.form_layout.setWidget(5, QFormLayout.FieldRole, self.btn_conectar)

        self.btn_conectar.clicked.connect(self.conectar)

    def conectar(self):
        usuario = self.txt_usuario.text()
        contrasena = self.txt_contrasena.text()
        db = self.txt_db.text()
        puerto = self.txt_puerto.text()
        host = self.txt_host.text()

        self.__con = Conexion(db, usuario, contrasena, puerto, host)

        self.__con.conectar()


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    frm = QStackedWidget()
    frm2 = FrmConexion(frm)
    frm.addWidget(frm2)
    frm.show()
    sys.exit(app.exec_())