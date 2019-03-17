import PyPDF2
def extract_text():
    pdfFileObj = open('example.pdf','rb')

    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    print(pdfReader.numPages)

    pageObj = pdfReader.getPage(0)

    text = pageObj.extractText()

    pdfFileObj.close()

    return text


