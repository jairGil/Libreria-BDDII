from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QHeaderView, QTableView, QWidget, QGridLayout, QTableWidgetItem, QAbstractItemView


class Consulta(QWidget):
    def __init__(self, columnas: list, datos: list(())):
        super().__init__()
        self.layout = QGridLayout(self)
        self.tbl_consulta = QTableView(self)
        self.columnas = columnas
        self.datos = datos
        self.model = QStandardItemModel(len(datos), len(columnas))

        self.setup_ui()

    def setup_ui(self):
        self.model.setHorizontalHeaderLabels(self.columnas)
        self.tbl_consulta.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tbl_consulta.horizontalHeader().setStretchLastSection(True)

        self.agrega_datos()

        self.layout.addWidget(self.tbl_consulta, 0, 0)
        self.tbl_consulta.setModel(self.model)

    def agrega_datos(self):
        for i, dato in enumerate(self.datos):
            for j, campo in enumerate(dato):
                self.model.setItem (i, j, QStandardItem(str(campo)))
