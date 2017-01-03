from PyPDF2 import PdfFileWriter, PdfFileReader
import StringIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.enums import TA_RIGHT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from django.conf import settings
 
# Register Fonts
pdfmetrics.registerFont(TTFont('Montserrat-Regular', 'static/fonts/Montserrat-Regular.ttf'))
pdfmetrics.registerFont(TTFont('Montserrat-Bold', 'static/fonts/Montserrat-Bold.ttf'))
 
# Our Custom Style
def get_pdf(text):

    packet = StringIO.StringIO()
    # create a new PDF with Reportlab
    can = canvas.Canvas(packet, pagesize=letter)
    can.setFont("Montserrat-Regular", 9)    
    y = 750
    for line in text.split("."):
        line.replace('                                           ', '\n')
        line.strip()                    #Remove all the leading and trailing whitespaces
        line += '.'                     #Add the fullstop back
        print line
        can.drawString(25, y, line)
        y -= 20
    can.save()

    #move to the beginning of the StringIO buffer
    packet.seek(0)
    new_pdf = PdfFileReader(packet)
    # read your existing PDF
    existing_pdf = PdfFileReader(file("media/write.pdf", "rb"))
    output = PdfFileWriter()
    # add the "watermark" (which is the new pdf) on the existing page
    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)
    # finally, write "output" to a real file
    outputStream = file("media/write_final.pdf", "wb")
    output.write(outputStream)
    outputStream.close()

