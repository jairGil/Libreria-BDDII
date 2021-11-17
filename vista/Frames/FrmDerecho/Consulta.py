from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QHeaderView, QTableView, QWidget, QGridLayout, QTableWidgetItem, QAbstractItemView


class Consulta(QWidget):
    def __init__(self):
        super().__init__()
        self.datos_mostrados = False
        self.layout = QGridLayout(self)
        self.tbl_consulta = QTableView(self)

        self.setup_ui()

    def setup_ui(self):
        self.tbl_consulta.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tbl_consulta.horizontalHeader().setStretchLastSection(True)

        self.layout.addWidget(self.tbl_consulta, 0, 0)

    def agrega_datos(self, columnas: list, datos: list(())):
        self.datos_mostrados = True
        model = QStandardItemModel(len(datos), len(columnas))
        model.setHorizontalHeaderLabels(columnas)

        for i, dato in enumerate(datos):
            for j, campo in enumerate(dato):
                model.setItem (i, j, QStandardItem(str(campo)))
        
        self.tbl_consulta.setModel(model)
