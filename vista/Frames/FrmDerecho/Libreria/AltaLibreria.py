from PyQt5 import QtCore
from PyQt5.QtWidgets import QAction, QComboBox, QGridLayout, QLabel, QLineEdit, QPushButton, QSizePolicy, QSpacerItem, QWidget
from controlador.DMLCiudad import DMLCiudad
from controlador.DMLEncargado import DMLEncargado
from controlador.DMLPais import DMLPais
from modelo.Libreria import Libreria
from vista.Dialog.DlgAviso import DlgAviso
from controlador.DMLLibreria import DMLLibreria
from controlador.DMLMunicipio import DMLMunicipio


class AltaLibreria(QWidget):
    def __init__(self, p:QWidget):
        super().__init__(parent=p)
        self.layout = QGridLayout(self)
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
        self.btn_agregar = QPushButton("Agregar", self)

        self.campos = [self.txt_nombre, self.txt_telefono, self.txt_direccion]
        self.combos = [self.cmbx_pais, self.cmbx_ciudad, self.cmbx_municipio, self.cmbx_encargado]
        
        self.conexion = self.parent().parent().conex
        self.dml_libreria = DMLLibreria(self.conexion)

        self.setup_ui()
    
    def setup_ui(self):
        self.txt_nombre.setMinimumWidth(300)
        
        verticalSpacer = QSpacerItem(20, 71, QSizePolicy.Minimum, QSizePolicy.Expanding)
        horizontalSpacer = QSpacerItem(63, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        horizontalSpacer_2 = QSpacerItem(63, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        verticalSpacer_2 = QSpacerItem(20, 71, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.layout.addItem(verticalSpacer, 0, 1)
        self.layout.addItem(verticalSpacer_2, 9, 1)
        self.layout.addItem(horizontalSpacer, 1, 0)
        self.layout.addItem(horizontalSpacer_2, 1, 4)

        self.layout.addWidget(self.lbl_nombre, 1, 1)
        self.layout.addWidget(self.txt_nombre, 1, 2, 1, 2)
        self.layout.addWidget(self.lbl_telefono, 2, 1)
        self.layout.addWidget(self.txt_telefono, 2, 2, 1, 2)
        self.layout.addWidget(self.lbl_pais, 3, 1)
        self.layout.addWidget(self.cmbx_pais, 3, 2, 1, 2)
        self.layout.addWidget(self.lbl_ciudad, 4, 1)
        self.layout.addWidget(self.cmbx_ciudad, 4, 2, 1, 2)
        self.layout.addWidget(self.lbl_municipio, 5, 1)
        self.layout.addWidget(self.cmbx_municipio, 5, 2, 1, 2)
        self.layout.addWidget(self.lbl_direccion, 6, 1)
        self.layout.addWidget(self.txt_direccion, 6, 2, 1, 2)
        self.layout.addWidget(self.lbl_encargado, 7, 1)
        self.layout.addWidget(self.cmbx_encargado, 7, 2, 1, 2)
        self.layout.addWidget(self.btn_limpiar, 8, 2)
        self.layout.addWidget(self.btn_agregar, 8, 3)

        self.agregar_acciones()        

    def agregar_acciones(self):
        self.btn_agregar.clicked.connect(self.accion_btn_agregar)
        self.btn_limpiar.clicked.connect(self.limpiar_campos)
        self.agregar_datos_cmbx_pais()
        self.cmbx_pais.setCurrentIndex(-1)
        self.cmbx_pais.currentTextChanged.connect(self.llenar_cmbx_ciudad)

    def agregar_datos_cmbx_pais(self):
        dml_pais = DMLPais(self.conexion)
        datos = dml_pais.consultas()
        for d in datos:
            self.cmbx_pais.addItem(d[1], d)
    
    def llenar_cmbx_ciudad(self):
        self.cmbx_ciudad.clear()
        dml_pais = DMLCiudad(self.conexion)
        datos = dml_pais.consultas(self.cmbx_pais.currentData()[0])
        for d in datos:
            self.cmbx_ciudad.addItem(d[1], d)
        self.cmbx_ciudad.currentTextChanged.connect(self.llenar_cmbx_municipio)
        
    def llenar_cmbx_municipio(self):
        self.cmbx_municipio.clear()
        dml_municipio = DMLMunicipio(self.conexion)
        datos = dml_municipio.consultas(self.cmbx_ciudad.currentData()[0])
        for d in datos:
            self.cmbx_municipio.addItem(d[1], d)
        self.cmbx_municipio.currentTextChanged.connect(self.llenar_cmbx_encargados)

    def llenar_cmbx_encargados(self):
        self.cmbx_encargado.clear()
        dml_encargado = DMLEncargado(self.conexion)
        datos = dml_encargado.consultas(int(self.cmbx_municipio.currentData()[0]))
        for d in datos:
            self.cmbx_encargado.addItem(d[1], d)

    def accion_btn_agregar(self):
        vacios = False
        for campo in self.campos:
            if campo.text() == "" or campo.text() is None:
                DlgAviso(self, "ERROR: Se encontraron campos vacíos")
                vacios = True

        for cmbx in self.combos:
            if cmbx.currentText() == "" or cmbx.currentText() is None:
                DlgAviso(self, "ERROR: Se encontraron combo boxes vacíos")
                vacios = True
        
        if not vacios:
            nombre = self.txt_nombre.text()
            telefono = self.txt_telefono.text()
            municipio = int(self.cmbx_municipio.currentData()[0])
            direccion = self.txt_direccion.text()
            encargado = self.cmbx_encargado.currentData()[0]

            lib = Libreria(nombre, telefono, encargado, municipio, direccion)

            self.dml_libreria.altas(lib)

            DlgAviso(self, "Datos ingresados correctamente")

    def limpiar_campos(self):
        for c in self.campos:
            c.setText("")
        try:
            for c in self.combos:
                c.setCurrentIndex(0)
        except TypeError:
            pass
