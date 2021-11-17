from PyQt5.QtWidgets import QFrame, QGridLayout, QLabel, QLineEdit, QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout, QWidget

from controlador.DML import DML
from controlador.DMLFacturas import DMLFacturas
from vista.Dialog.DlgAviso import DlgAviso


class FrmFacturas(QWidget):
    def __init__(self, p: QWidget):
        super().__init__(parent=p)
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
        self.layout_detalles.addWidget(self.lbl_separador, 0, 0, 1, 6)
        self.layout_detalles.addWidget(self.lbl_detalles, 1, 0,)
        self.layout_detalles.addWidget(self.lbl_libro, 2, 0, 1, 3)
        self.layout_detalles.addWidget(self.lbl_precio, 2, 3)
        self.layout_detalles.addWidget(self.lbl_cantidad, 2, 4)
        self.layout_detalles.addWidget(self.lbl_subtotal, 2, 5)

        self.limpiar_factura()

        self.layout_factura.addWidget(self.frm_detalles)
        
        self.btn_buscar.clicked.connect(self.accion_btn_buscar)

    def accion_btn_buscar(self):
        try:
            id_factura = int(self.txt_id.text())
            dml_facturas = DMLFacturas(self.parent().parent().conex)
            datos = dml_facturas.get_detalles_cliente(id_factura)
            detalles = dml_facturas.get_detalles_compra(id_factura)

            self.agregar_detalles(detalles)
            self.agregar_datos(datos)
        except ValueError:
            DlgAviso(self, "Verifique el campo de texto ID \n\n ID NO VALIDO")  

    def agregar_datos(self, datos:list):
        try: 
            d = datos[0]
            self.lbl_id_factura.setText("ID FACTURA: " + str(d[0]))
            self.lbl_cliente.setText("CLIENTE: " + str(d[1]))
            self.lbl_fecha.setText("FECHA: " + str(d[2]))
        except IndexError:
            DlgAviso(self, "Factura no existente")
            self.limpiar_factura()

    def agregar_detalles(self, detalles: list):
        self.limpiar_factura()
        total = 0
        labels = []
        for libro in detalles:
            titulo = str(libro[0])
            precio = str(libro[1])
            cantidad = str(libro[2])
            subtotal = str(libro[3])
            lbl_titulo_libro = QLabel(titulo, self.frm_detalles)
            lbl_precio_libro = QLabel(precio, self.frm_detalles)
            lbl_cantidad_libro = QLabel(cantidad, self.frm_detalles)
            lbl_subtotal_libro = QLabel(subtotal, self.frm_detalles)
            labels.append((lbl_titulo_libro, lbl_precio_libro, lbl_cantidad_libro, lbl_subtotal_libro))
            total += float(subtotal)

        fila = 3
        for renglon in labels:
            columna = 0
            for label in renglon:
                if columna == 0:
                    self.layout_detalles.addWidget(label, fila, columna, 1, 3)
                    columna += 2
                else:
                    self.layout_detalles.addWidget(label, fila, columna)
                columna += 1
            fila += 1

        txt_total = f"${total:.2f}"
        
        lbl_total = QLabel("TOTAL", self.frm_detalles)
        lbl_total_cuenta = QLabel(txt_total, self.frm_detalles)
        self.layout_detalles.addWidget(lbl_total, fila, 4)
        self.layout_detalles.addWidget(lbl_total_cuenta, fila, 5)

    def limpiar_factura(self):
        self.lbl_id_factura.setText("ID FACTURA: ")
        self.lbl_cliente.setText("CLIENTE: ")
        self.lbl_fecha.setText("FECHA: ")

        labels = []
        for i in range(6):
            lbl_titulo_libro = QLabel("", self.frm_detalles)
            lbl_precio_libro = QLabel("", self.frm_detalles)
            lbl_cantidad_libro = QLabel("", self.frm_detalles)
            lbl_subtotal_libro = QLabel("", self.frm_detalles)
            labels.append((lbl_titulo_libro, lbl_precio_libro, lbl_cantidad_libro, lbl_subtotal_libro))

        fila = 3
        for renglon in labels:
            columna = 0
            for label in renglon:
                if columna == 0:
                    self.layout_detalles.addWidget(label, fila, columna, 1, 3)
                    columna += 2
                else:
                    self.layout_detalles.addWidget(label, fila, columna)
                columna += 1
            fila += 1
