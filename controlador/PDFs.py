from decimal import Decimal
from lxml import etree, objectify
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch, mm
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Table, TableStyle


class PDFs:
    def __init__(self, xml_file, pdf_file):
        self.xml_file = xml_file
        self.pdf_file = pdf_file
        self.xml_obj = self.getXMLObject()
    
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
        """ % (str(xml.nombre_cliente) + " " +str(xml.apellido_paterno) + " " + str(xml.apellido_materno),
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

    