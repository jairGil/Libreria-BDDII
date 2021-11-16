from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QFrame, QGridLayout, QLabel, QLineEdit, QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout, QWidget


class FrmFacturas(QWidget):
    def __init__(self):
        super().__init__()
        self.layout_principal = QGridLayout(self)
        self.lbl_id_buscar = QLabel("ID FACRURA:", self)
        self.txt_id = QLineEdit(self)
        self.btn_buscar = QPushButton("Buscar", self)
        self.btn_genera_pdf = QPushButton("Generar PDF", self)
        self.frm_factura = QFrame(self)
        self.layout_factura = QVBoxLayout(self.frm_factura)
        self.frm_datos_factura = QFrame(self.frm_factura)
        self.layout_datos_factura = QVBoxLayout(self.frm_datos_factura)
        self.lbl_id_factura = QLabel("ID FACTURA: ", self.frm_datos_factura)
        self.lbl_cliente = QLabel("CLIENTE: ", self.frm_datos_factura)
        self.lbl_fecha = QLabel("FECHA: ", self.frm_datos_factura)
        self.frm_detalles = QFrame(self.frm_factura)
        self.layout_detalles = QGridLayout(self.frm_detalles)
        self.lbl_separador = QLabel("-" * 200, self.frm_detalles)
        self.lbl_detalles = QLabel("DETALLES:", self.frm_detalles)
        self.lbl_libro = QLabel("LIBRO", self.frm_detalles)
        self.lbl_precio = QLabel("PRECIO", self.frm_detalles)
        self.lbl_cantidad = QLabel("CANTIDAD", self.frm_detalles)
        self.lbl_subtotal = QLabel("SUBTOTAL", self.frm_detalles)
        self.label_12 = QLabel("Label_12", self.frm_detalles)
        self.label_13 = QLabel("Label_13", self.frm_detalles)
        self.label_11 = QLabel("Label_11", self.frm_detalles)
        self.label_15 = QLabel("Label_15", self.frm_detalles)
        self.label_14 = QLabel("Label_14", self.frm_detalles)
        self.label_10 = QLabel("Label_10", self.frm_detalles)

        self.setup_ui()

    def setup_ui(self):
        # Estilo del frame factura
        self.frm_factura.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frm_factura.setFrameShape(QFrame.Box)
        self.frm_factura.setFrameShadow(QFrame.Raised)
        self.frm_factura.setMinimumWidth(500)
        self.frm_datos_factura.setMaximumHeight(80)

        spacerItem = QSpacerItem(160, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        spacerItem1 = QSpacerItem(160, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        # Colocar los widgets principales
        self.layout_principal.addWidget(self.lbl_id_buscar, 0, 1)
        self.layout_principal.addWidget(self.txt_id, 0, 2, 1, 3)
        self.layout_principal.addWidget(self.btn_buscar, 0, 5)
        self.layout_principal.addWidget(self.frm_factura, 1, 1, 1, 5)
        self.layout_principal.addWidget(self.btn_genera_pdf, 2, 5)
        self.layout_principal.addItem(spacerItem, 1, 6)
        self.layout_principal.addItem(spacerItem1, 1, 0)

        # Colocar widgets de los datos de la factura
        self.layout_datos_factura.addWidget(self.lbl_id_factura)
        self.layout_datos_factura.addWidget(self.lbl_cliente)
        self.layout_datos_factura.addWidget(self.lbl_fecha)

        self.layout_factura.addWidget(self.frm_datos_factura)

        # Colocar widgets detalles de la compra
        self.layout_detalles.addWidget(self.lbl_separador, 0, 0, 1, 5)
        self.layout_detalles.addWidget(self.lbl_detalles, 1, 0,)
        self.layout_detalles.addWidget(self.lbl_libro, 2, 1)
        self.layout_detalles.addWidget(self.lbl_precio, 2, 2)
        self.layout_detalles.addWidget(self.lbl_cantidad, 2, 3)
        self.layout_detalles.addWidget(self.lbl_subtotal, 2, 4)

        self.layout_detalles.addWidget(self.label_12, 3, 1)
        self.layout_detalles.addWidget(self.label_13, 3, 2)
        self.layout_detalles.addWidget(self.label_11, 4, 4)
        self.layout_detalles.addWidget(self.label_15, 3, 4)
        self.layout_detalles.addWidget(self.label_14, 3, 3)
        self.layout_detalles.addWidget(self.label_10, 4, 3)
        self.layout_factura.addWidget(self.frm_detalles)
        
        self.btn_buscar.clicked.connect(self.accion_btn_buscar)

    def accion_btn_buscar(self):
        pass
