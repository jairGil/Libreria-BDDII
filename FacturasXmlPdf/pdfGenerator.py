from decimal import Decimal
from lxml import etree, objectify

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch, mm
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Table, TableStyle

########################################################################
class PDFOrder(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, xml_file, pdf_file):
        """Constructor"""
        self.xml_file = xml_file
        self.pdf_file = pdf_file
        
        self.xml_obj = self.getXMLObject()
        
    #----------------------------------------------------------------------
    def coord(self, x, y, unit=1):
        """
        # http://stackoverflow.com/questions/4726011/wrap-text-in-a-table-reportlab
        Helper class to help position flowables in Canvas objects
        """
        x, y = x * unit, self.height -  y * unit
        return x, y  
        
    #----------------------------------------------------------------------
    def createPDF(self):
        """
        Create a PDF based on the XML data
        """
        self.canvas = canvas.Canvas(self.pdf_file, pagesize=letter)
        width, self.height = letter
        styles = getSampleStyleSheet()
        xml = self.xml_obj
        
        address = """ <font size="9">
        Enviar a:<br/>
        <br/>
        %s<br/>
        %s<br/>
        </font>
        """ % (xml.factura_id,xml.nombre_cliente)
        p = Paragraph(address, styles["Normal"])
        p.wrapOn(self.canvas, width, self.height)
        p.drawOn(self.canvas, *self.coord(18, 40, mm))
        
        order_number = '<font size="14"><b>Factura #%s </b></font>' % xml.factura_id
        p = Paragraph(order_number, styles["Normal"])
        p.wrapOn(self.canvas, width, self.height)
        p.drawOn(self.canvas, *self.coord(18, 50, mm))
        
        data = []
        data.append(["ISBN","Libro", "Precio", "Cantidad", "Total"])
        grand_total = 0
        for libro in xml.compra.iterchildren():
            row = []
            row.append(libro.isbn)
            row.append(str(libro.titulo)[:18] + "...")
            row.append(libro.precio)
            row.append(libro.cantidad)
            total = Decimal(str(libro.precio)) * Decimal(str(libro.cantidad))
            row.append(str(total))
            grand_total += total
            data.append(row)
        data.append(["", "", "", "Grand Total:", grand_total])
        t = Table(data, 1.5 * inch)
        t.setStyle(TableStyle([
            ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
            ('BOX', (0,0), (-1,-1), 0.25, colors.black)
        ]))
        t.wrapOn(self.canvas, width, self.height)
        t.drawOn(self.canvas, *self.coord(18, 85, mm))
        
        txt = "Thank you for your business!"
        p = Paragraph(txt, styles["Normal"])
        p.wrapOn(self.canvas, width, self.height)
        p.drawOn(self.canvas, *self.coord(18, 95, mm))
        
    #----------------------------------------------------------------------
    def getXMLObject(self):
        """
        Open the XML document and return an lxml XML document
        """
        with open(self.xml_file) as f:
            xml = f.read()
        return objectify.fromstring(xml)
    
    #----------------------------------------------------------------------
    def savePDF(self):
        """
        Save the PDF to disk
        """
        self.canvas.save()
    
#----------------------------------------------------------------------
if __name__ == "__main__":
    xml = "order.xml"
    pdf = "Factura.pdf"
    doc = PDFOrder(xml, pdf)
    doc.createPDF()
    doc.savePDF()