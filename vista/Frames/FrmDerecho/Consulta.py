from PyQt5.QtWidgets import QWidget, QGridLayout, QTableWidget, QTableWidgetItem, QAbstractItemView


class Consulta(QWidget):
    def __init__(self, columnas: list, datos: list(())):
        super().__init__()
        self.layout = QGridLayout(self)
        self.tbl_consulta = QTableWidget(self)
        self.columnas = columnas
        self.datos = datos

        self.setup_ui()

    def setup_ui(self):
        self.tbl_consulta.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tbl_consulta.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tbl_consulta.setSortingEnabled(True)
        self.tbl_consulta.setCornerButtonEnabled(False)
        self.tbl_consulta.horizontalHeader().setStretchLastSection(True)

        self.agrega_encabezados()
        self.agrega_datos()

        self.layout.addWidget(self.tbl_consulta, 0, 0)

    def agrega_encabezados(self):
        self.tbl_consulta.setColumnCount(len(self.columnas))
        self.tbl_consulta.setHorizontalHeaderLabels(self.columnas)

    def agrega_datos(self):
        self.tbl_consulta.setRowCount(len(self.datos))
        for i, dato in enumerate(self.datos):
            for j, campo in enumerate(dato):
                self.tbl_consulta.setItem(i, j, QTableWidgetItem(campo.__str__()))
