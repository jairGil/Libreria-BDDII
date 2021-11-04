from vista.FrmConexion import FrmConexion


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication, QStackedWidget
    import sys

    app = QApplication(sys.argv)
    frm = QStackedWidget()
    frm2 = FrmConexion(frm)
    frm.addWidget(frm2)
    frm.show()
    sys.exit(app.exec_())