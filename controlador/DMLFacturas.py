from controlador.Conexion import Conexion
from controlador.DML import DML

from decimal import Decimal
from lxml import etree, objectify
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch, mm
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Table, TableStyle

class DMLFacturas():
    dml: DML

    def __init__(self, conexion: Conexion):
        self.dml = DML(conexion)

    def get_detalles_cliente(self, id_factura: int):
        sql =  f''' SELECT f.factura_id, concat(c.nombre_persona, ' ', c.apellido_paterno, ' ', c.apellido_materno), 
                        to_char(f.fecha_compra, 'YYYY-MM-DD')
                        FROM libreria.factura as f, libreria.cliente as c 
                        WHERE f.rfc = c.rfc
                        AND f.factura_id = {id_factura}
                    '''
        return self.dml.consulta(sql)

    def get_detalles_compra(self, id_factura: int):
        sql =  f''' SELECT l.titulo, l.precio, fl.cantidad_libro, fl.cantidad_libro * l.precio
                        FROM libreria.libro as l, libreria.factura_libro as fl 
                        WHERE l.isbn = fl.isbn
                        AND fl.factura_id = {id_factura}
                    '''
        return self.dml.consulta(sql)
    
    """def __init__(self, xml_file, pdf_file):
        self.xml_file = xml_file
        self.pdf_file = pdf_file
        self.xml_obj = self.getXMLObject()"""
    
    def coord(self, x, y, unit=1):
        """
        # http://stackoverflow.com/questions/4726011/wrap-text-in-a-table-reportlab
        Helper class to help position flowables in Canvas objects
        """
        x, y = x * unit, self.height -  y * unit
        return x, y  
    
    def createPDF(self):
        """
        Create a PDF based on the XML data
        """
        self.canvas = canvas.Canvas(self.pdf_file, pagesize=letter)
        width, self.height = letter
        styles = getSampleStyleSheet()
        xml = self.xml_obj
        
        address = """ <font size="12">
        <br/>
        Enviar a:<br/>
        <br/>
        %s<br/>
        <br/>
        %s<br/>
        <br/>
        %s<br/>
        <br/>
        Código Postal: %s<br/>
        </font>
        """ % (str(xml.nombre_cliente) + str(xml.apellido_paterno) + str(xml.apellido_materno),
        xml.fecha_compra,
        xml.direccion,xml.cp)
        p = Paragraph(address, styles["Normal"])
        p.wrapOn(self.canvas, width, self.height)
        p.drawOn(self.canvas, *self.coord(18, 65, mm))
        
        factura = '<font size="20"><b>Factura #%s </b></font>' % xml.factura_id
        p = Paragraph(factura, styles["Normal"])
        p.wrapOn(self.canvas, width, self.height)
        p.drawOn(self.canvas, *self.coord(18, 20, mm))
        
        data = []
        data.append(["ISBN","Libro", "Precio", "Cantidad", "Total"])
        grand_total = 0
        total_libros = 0
        for libro in xml.compra.iterchildren():
            row = []
            row.append(libro.isbn)
            row.append(str(libro.titulo)[:18] + "...")
            row.append(libro.precio)
            row.append(libro.cantidad)
            total = Decimal(str(libro.precio)) * Decimal(str(libro.cantidad))
            total_libros += Decimal(str(libro.cantidad))
            row.append(str(total))
            grand_total += total
            data.append(row)
        data.append(["", "", "TOTALES", total_libros, grand_total])
        t = Table(data, 1.5 * inch)
        t.setStyle(TableStyle([
            ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
            ('BOX', (0,0), (-1,-1), 0.25, colors.black)
        ]))
        t.wrapOn(self.canvas, width, self.height)
        t.drawOn(self.canvas, *self.coord(18, 150, mm))
        
        txt = "GRACIAS POR SU COMPRA !!!"
        p = Paragraph(txt, styles["Normal"])
        p.wrapOn(self.canvas, width, self.height)
        p.drawOn(self.canvas, *self.coord(18, 200, mm))

    def getXMLObject(self):
        """
        Open the XML document and return an lxml XML document
        """
        with open(self.xml_file) as f:
            xml = f.read()
        return objectify.fromstring(xml)

    def savePDF(self):
        """
        Save the PDF to disk
        """
        self.canvas.save()

    def crearXML(self,id:int):
        sql = self.dml.consulta(f"""SELECT XMLELEMENT(name factura,XMLCONCAT((SELECT XMLCONCAT(
                                        XMLELEMENT(name factura_id,factura.factura_id),
                                                XMLELEMENT(name nombre_cliente, cliente.nombre_persona),
                                                XMLELEMENT(name apellido_paterno, cliente.apellido_paterno),
                                                XMLELEMENT(name apellido_materno, cliente.apellido_materno),
                                                XMLELEMENT(name direccion, cliente.direccion),
                                                XMLELEMENT(name cp, cliente.cp),
                                                XMLELEMENT(name fecha_compra, factura.fecha_compra))
                                        FROM factura, cliente
                                        WHERE factura.factura_id = {id}
                                        AND factura.rfc = cliente.rfc),(SELECT XMLELEMENT(name compra, XMLAGG(detalles))
                                    FROM (SELECT XMLELEMENT(name libro,
                                            XMLCONCAT(XMLELEMENT(name ISBN, libro.isbn),
                                                XMLELEMENT(name titulo, libro.titulo),
                                                XMLELEMENT(name precio, libro.precio),
                                                XMLELEMENT(name cantidad, factura_libro.cantidad_libro))
                                            ) as detalles
                                        FROM factura_libro, libro
                                        WHERE factura_libro.factura_id = {id}
                                        AND factura_libro.isbn = libro.isbn) t)));""")
        return self.dml.consulta(sql)

