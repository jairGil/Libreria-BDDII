from PyQt5.QtWidgets import QComboBox, QGridLayout, QLabel, QLineEdit, QPushButton, QSizePolicy, QSpacerItem, QWidget
from controlador.DMLCiudad import DMLCiudad
from controlador.DMLEncargado import DMLEncargado
from controlador.DMLLibreria import DMLLibreria
from controlador.DMLMunicipio import DMLMunicipio
from controlador.DMLPais import DMLPais
from modelo.Libreria import Libreria

from vista.Dialog.DlgAviso import DlgAviso


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
        self.btn_modificar = QPushButton("Modificar", self)

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
        self.layout.addWidget(self.btn_modificar, 9, 3)

        self.desactivar_campos()
        self.btn_modificar.clicked.connect(self.modificar_libreria)
        self.btn_buscar.clicked.connect(self.buscar_libreria)
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
    
    def buscar_libreria(self):
        try:
            id = int(self.txt_id.text())
            datos = self.dml_libreria.consultas(id)[0]
            for i, campo in enumerate(self.campos):
                campo.setText(str(datos[i+1]))
            self.activar_campos()
        except ValueError:
            DlgAviso(self, "Error, ID no válido")
        except IndexError:
            DlgAviso(self, "Libreria no existente")

    def modificar_libreria(self):
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
            try:
                id = int(self.txt_id.text())
                nombre = self.txt_nombre.text()
                telefono = self.txt_telefono.text()
                municipio = int(self.cmbx_municipio.currentData()[0])
                direccion = self.txt_direccion.text()
                encargado = self.cmbx_encargado.currentData()[0]
                print(id)

                lib = Libreria(nombre, telefono, encargado, municipio, direccion, id=id)

                self.dml_libreria.cambios(lib)
                self.limpiar_campos()
                DlgAviso(self, "Datos modificados correctamente")
            except ValueError:
                DlgAviso(self, "Id no válido")

    def activar_campos(self):
        for campo in self.campos:
            campo.setEnabled(True)
    
    def desactivar_campos(self):
        for campo in self.campos:
            campo.setEnabled(False)

    def limpiar_campos(self):
        for c in self.campos:
            c.setText("")
        try:
            for c in self.combos:
                c.setCurrentIndex(0)
        except TypeError:
            pass
