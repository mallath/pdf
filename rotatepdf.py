from PyPDF2 import PdfFileReader,PdfFileWriter

def rotateDDF(inPdfFilename, outPdfFilename, degree):
       pdfReader = PdfFileReader(inPdfFilename)
       pdfWriter = PdfFileWriter()

       for i in range(pdfReader.getNumPages()):
        page=pdfReader.getPage(i).rotate.Clockwise(degree)
        pdfWriter.addPage(page)

        with open(outPdfFilename,'wb') as outPdf:
            pdfWriter.write(outPdf)
            
inPdfFilename ='E:\python project\pdf\document1.pdf'
outPdfFilename='E:\python project\pdf\document2.pdf'
degree=90
rotateDDF(inPdfFilename, outPdfFilename, degree)



