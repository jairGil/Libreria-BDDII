from PyQt5.QtWidgets import QDesktopWidget, QFrame, QPushButton, QStackedLayout, QStackedWidget, QVBoxLayout, QSpacerItem, QSizePolicy


class PnlPrincipalIzq(QFrame):
    def __init__(self, p: QStackedWidget):
        super().__init__(parent=p)
        self.layout = QVBoxLayout(self)
        self.btn_inicio = QPushButton("Inicio", self)
        self.btn_reportes = QPushButton("Reportes", self)
        self.btn_facturacion = QPushButton("Facturacion", self)
        self.btn_librerias = QPushButton("Librerias", self)
        self.btn_precios = QPushButton("Precios", self)
        self.btn_salir = QPushButton("Salir", self)
        self.spacer = QSpacerItem(20, 40, vPolicy=QSizePolicy.Expanding)

        self.buttons = [self.btn_inicio, self.btn_reportes, self.btn_facturacion,  self.btn_librerias, self.btn_precios]

        self.setup_ui()

    def setup_ui(self):
        self.layout.setContentsMargins(0, 0, 0, 0)

        for btn in self.buttons:
            self.layout.addWidget(btn)

        self.layout.addItem(self.spacer)
        self.layout.addWidget(self.btn_salir)

        for btn in self.buttons:
            btn.setAutoExclusive(True)

        for btn in self.buttons:
            btn.setCheckable(True)

        self.setStyleSheet("""
            QFrame {
                background-color: #00ACC1;
            }
            
            QPushButton {
                border: none;
                background-color: none;
                color: #E0F7FA;
                height: 30px;
                text-align: left;
                padding: 5px 10px 5px 10px;
                outline: none;
            }
            
            QPushButton::hover {
                background-color: #00BCD4;
            }
            
            QPushButton::checked {
                background-color: #0097A7;
                outline: none;
            }
        """)



if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    wd = PnlPrincipalIzq()
    wd.show()
    sys.exit(app.exec_())