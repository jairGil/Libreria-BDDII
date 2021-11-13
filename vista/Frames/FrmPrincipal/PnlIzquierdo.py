from PyQt5.QtWidgets import QDesktopWidget, QFrame, QPushButton, QStackedLayout, QStackedWidget, QVBoxLayout, QSpacerItem, QSizePolicy


class PnlPrincipalIzq(QFrame):
    def __init__(self, p: QStackedWidget):
        super().__init__(parent=p)
        self.layout = QVBoxLayout(self)
        self.btn_inicio = QPushButton("Inicio", self)
        self.btn_categoria = QPushButton("Categoria", self)
        self.btn_marca = QPushButton("Marca", self)
        self.btn_producto = QPushButton("Producto", self)
        self.btn_modo_pago = QPushButton("Modo Pago", self)
        self.btn_cliente = QPushButton("Cliente", self)
        self.btn_factura = QPushButton("Factura", self)
        self.btn_detalle = QPushButton("Detalle", self)
        self.btn_salir = QPushButton("Salir", self)
        self.spacer = QSpacerItem(20, 40, vPolicy=QSizePolicy.Expanding)

        self.buttons = [self.btn_inicio, self.btn_categoria, self.btn_marca,  self.btn_producto, self.btn_modo_pago,
                        self.btn_cliente, self.btn_factura, self.btn_detalle]

        self.setup_ui()
        self.set_acciones()

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

    def set_acciones(self):
        self.btn_salir.clicked.connect(self.btn_salir_click)

    def btn_salir_click(self):
        self.parent().parent().parent().setCurrentIndex(0)



if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    wd = PnlPrincipalIzq()
    wd.show()
    sys.exit(app.exec_())