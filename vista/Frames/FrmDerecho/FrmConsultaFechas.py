from PyQt5.QtCore import QDate, QLocale
from PyQt5.QtWidgets import QDateEdit, QFrame, QGridLayout, QLabel, QPushButton, QRadioButton, QTableWidget, QTableWidgetItem
from controlador.Conexion import Conexion
from controlador.DML import DML

from vista.Frames.FrmDerecho.Consulta import Consulta


class FrmConsultaFechas(QFrame):
    def __init__(self) -> None:
        super().__init__()
        self.gridLayout = QGridLayout(self)
        self.rbtn_dia = QRadioButton("Dia", self)
        self.rbtn_mes = QRadioButton("Mes", self)
        self.rbtn_anio = QRadioButton("Año", self)
        self.rbtn_rango = QRadioButton("Rango", self)
        self.lbl_fecha_inicio = QLabel("Fecha de inicio", self)
        self.lbl_fecha_fin = QLabel("Fecha de Fin", self)
        self.ded_dia = QDateEdit(self)
        self.ded_mes = QDateEdit(self)
        self.ded_anio = QDateEdit(self)
        self.ded_fecha_inicio = QDateEdit(self)
        self.ded_fecha_fin = QDateEdit(self)
        self.btn_buscar = QPushButton("Buscar", self)

        self.tbl_consulta = QTableWidget(self)

        self.setup_ui()
        self.show()

    def setup_ui(self):
        # Añadiendo los radio buttons
        self.gridLayout.addWidget(self.rbtn_dia, 0, 0)
        self.gridLayout.addWidget(self.rbtn_mes, 0, 1)
        self.gridLayout.addWidget(self.rbtn_anio, 0, 2)
        self.gridLayout.addWidget(self.rbtn_rango, 0, 3)

        # Añadiendo los labels
        self.gridLayout.addWidget(self.lbl_fecha_inicio, 1, 3)
        self.gridLayout.addWidget(self.lbl_fecha_fin, 2, 3)

        # Añadiendo los date edits
        self.gridLayout.addWidget(self.ded_dia, 1, 0)
        self.gridLayout.addWidget(self.ded_mes, 1, 1)
        self.gridLayout.addWidget(self.ded_anio, 1, 2)
        self.gridLayout.addWidget(self.ded_fecha_inicio, 1, 4)
        self.gridLayout.addWidget(self.ded_fecha_fin, 2, 4)

        # Añadir el botón de búsqueda
        self.gridLayout.addWidget(self.btn_buscar, 0, 5, 3, 1)

        # Añadir la tabla de consultas
        self.gridLayout.addWidget(self.tbl_consulta, 3, 0, 1, 6)

        self.ded_dia.setDate(QDate(2021, 12, 11))
        self.tbl_consulta.setColumnCount(0)
        self.tbl_consulta.setRowCount(0)

        # Añadir los valores por defecto a cada date edit
        deds = [self.ded_dia, self.ded_mes, self.ded_anio, self.ded_fecha_inicio, self.ded_fecha_fin]
        for ded in deds:
            ded.setDate(QDate.currentDate())
            ded.setLocale(QLocale(QLocale.Spanish, QLocale.Mexico))

        self.retranslate_ui()

    def retranslate_ui(self):
        self.ded_dia.setDisplayFormat("dd/MMMM/yyyy")
        self.ded_mes.setDisplayFormat("MMMM")
        self.ded_anio.setDisplayFormat("yyyy")
        self.ded_fecha_inicio.setDisplayFormat("dd/MMMM/yyyy")
        self.ded_fecha_fin.setDisplayFormat("dd/MMMM/yyyy")
