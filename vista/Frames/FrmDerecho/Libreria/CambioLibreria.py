from PyQt5.QtWidgets import QComboBox, QGridLayout, QLabel, QLineEdit, QPushButton, QSizePolicy, QSpacerItem, QWidget


class CambioLibreria(QWidget):
    def __init__(self, p:QWidget):
        super().__init__(parent=p)
        self.layout = QGridLayout(self)
        self.lbl_id = QLabel("ID", self)
        self.txt_id = QLineEdit(self)
        self.btn_buscar = QPushButton("Buscar", self)
        self.lbl_nombre = QLabel("Nombre", self)
        self.txt_nombre = QLineEdit(self)
        self.lbl_telefono = QLabel("Telefono", self)
        self.txt_telefono = QLineEdit(self)
        self.lbl_pais = QLabel("Pais", self)
        self.cmbx_pais = QComboBox(self)
        self.lbl_ciudad = QLabel("Ciudad", self)
        self.cmbx_ciudad = QComboBox(self)
        self.lbl_municipio = QLabel("Municipio", self)
        self.cmbx_municipio = QComboBox(self)
        self.lbl_direccion = QLabel("Direccion", self)
        self.txt_direccion = QLineEdit(self)
        self.lbl_encargado = QLabel("Encargado", self)
        self.cmbx_encargado = QComboBox(self)
        self.btn_limpiar = QPushButton("Limpiar", self)
        self.btn_modificar = QPushButton("Modificar", self)

        self.campos = [self.txt_nombre, self.txt_telefono, self.cmbx_pais, self.cmbx_ciudad, self.cmbx_municipio, 
                        self.txt_direccion, self.cmbx_encargado, self.btn_modificar, self.btn_limpiar]

        self.setup_ui()
    
    def setup_ui(self):
        self.txt_nombre.setMinimumWidth(300)
        
        verticalSpacer = QSpacerItem(20, 71, QSizePolicy.Minimum, QSizePolicy.Expanding)
        horizontalSpacer = QSpacerItem(63, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        horizontalSpacer_2 = QSpacerItem(63, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        verticalSpacer_2 = QSpacerItem(20, 71, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.layout.addItem(verticalSpacer, 0, 1)
        self.layout.addItem(verticalSpacer_2, 10, 1)
        self.layout.addItem(horizontalSpacer, 1, 0)
        self.layout.addItem(horizontalSpacer_2, 1, 4)

        self.layout.addWidget(self.lbl_id, 1, 1)
        self.layout.addWidget(self.txt_id, 1, 2)
        self.layout.addWidget(self.btn_buscar, 1, 3)
        self.layout.addWidget(self.lbl_nombre, 2, 1)
        self.layout.addWidget(self.txt_nombre, 2, 2, 1, 2)
        self.layout.addWidget(self.lbl_telefono, 3, 1)
        self.layout.addWidget(self.txt_telefono, 3, 2, 1, 2)
        self.layout.addWidget(self.lbl_pais, 4, 1)
        self.layout.addWidget(self.cmbx_pais, 4, 2, 1, 2)
        self.layout.addWidget(self.lbl_ciudad, 5, 1)
        self.layout.addWidget(self.cmbx_ciudad, 5, 2, 1, 2)
        self.layout.addWidget(self.lbl_municipio, 6, 1)
        self.layout.addWidget(self.cmbx_municipio, 6, 2, 1, 2)
        self.layout.addWidget(self.lbl_direccion, 7, 1)
        self.layout.addWidget(self.txt_direccion, 7, 2, 1, 2)
        self.layout.addWidget(self.lbl_encargado, 8, 1)
        self.layout.addWidget(self.cmbx_encargado, 8, 2, 1, 2)
        self.layout.addWidget(self.btn_limpiar, 9, 2)
        self.layout.addWidget(self.btn_modificar, 9, 3)

        self.desactivar_campos()
    
    def activar_campos(self):
        for campo in self.campos:
            campo.setEnabled(True)
    
    def desactivar_campos(self):
        for campo in self.campos:
            campo.setEnabled(False)
