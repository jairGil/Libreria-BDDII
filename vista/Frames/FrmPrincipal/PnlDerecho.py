from PyQt5.QtWidgets import QFrame, QGridLayout, QSpacerItem, QSizePolicy, QStackedWidget, QLabel, QWidget
from controlador.Conexion import Conexion
from controlador.DML import DML
from vista.Frames.FrmDerecho.Consulta import Consulta

from vista.Frames.FrmDerecho.FrmConsultaFechas import FrmConsultaFechas
from vista.Frames.FrmDerecho.FrmFacturas import FrmFacturas


class PnlPrincipalDer(QFrame):
    def __init__(self, conexion: Conexion, p):
        super().__init__(parent=p)
        self.grid_layout = QGridLayout(self)
        self.stack = QStackedWidget(self)
        self.conex = conexion
        dml = DML(self.conex)
        datos_libro = dml.consulta("SELECT l.isbn, l.titulo, l.precio, c.nombre_categoria FROM libreria.libro as l, libreria.categoria as c WHERE l.categoria_id = c.categoria_id ORDER BY 1")
        encabezados_libro = ["ISBN", "Titulo", "Precio", "Categoria"]
        datos_libreria = dml.consulta("Select libreria_id, nombre_libreria, telefono, RFC, cp, direccion from libreria.libreria")
        encabezados_libreria = ["libreria_id", "nombre_libreria", "telefono", "RFC", "cp", "direccion"]
        datos_encargado = dml.consulta("Select RFC, apellido_paterno, apellido_materno, nombre_persona, cp, direccion from libreria.encargado")
        encabezados_encargado = ["RFC", "Apellido Paterno", "Apellido Materno", "Nombre", "cp", "direccion"]
        #print(len(datos_encargado))
        print("Agregando widgets")
        self.pagina_inicio = QWidget()
        self.pagina_reportes = FrmConsultaFechas()
        self.pagina_facturacion = FrmFacturas(self)
        self.pagina_librerias = Consulta(encabezados_libreria, datos_libreria)
        self.pagina_libros = Consulta(encabezados_libro, datos_libro)
        self.pagina_encargados = Consulta(encabezados_encargado, datos_encargado)
        self.setup_ui()

    def setup_ui(self):
        self.setStyleSheet("QFrame{background-color: #ECEFF1;}")

        self.stack.setMinimumSize(900, 600)
        """
        lbl = QLabel("Aqui estoy", self.stack)
        lbl.setAlignment(Qt.AlignCenter)
        """
        # SELECT count(factura.factura_id, factura.rfc, cliente.nombre_persona, cliente.apellido_paterno, 
        #               cliente.apellido_materno, factura.fecha_compra, libro.isbn, factura_libro.cantidad_libro, libro.precio) 
        # FROM factura, cliente, factura_libro, libro
        # GROUP BY ROLLUP (factura.factura_id, factura.rfc, cliente.nombre_persona, cliente.apellido_paterno, 
        #               cliente.apellido_materno, factura.fecha_compra)
        # WHERE factura_id = 1000000
        # AND f.factura_id = lf.factura_id 
        # AND fl.isbn = l.isbn
        # AND f.rfc = c.rfc 
        self.stack.addWidget(self.pagina_inicio) # Reportes semanales
        self.stack.addWidget(self.pagina_reportes) # Reportes personalizados
        self.stack.addWidget(self.pagina_facturacion) # Facturacion
        self.stack.addWidget(self.pagina_librerias) # Cambio de precios de los libros
        self.stack.addWidget(self.pagina_libros)
        self.stack.addWidget(self.pagina_encargados)
        self.grid_layout.addWidget(self.stack,0, 0)


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    frm = PnlPrincipalDer()
    frm.show()
    sys.exit(app.exec_())