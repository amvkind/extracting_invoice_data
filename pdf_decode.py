import PyPDF2
import json
import os.path

def pdf_to_text(filename):
    save_path = 'C:/Users/Himanshu Prajapati/Downloads/Sampleproject/data'
    abs_path = os.path.join(save_path,filename)

    pdfFileObj = open(abs_path,'rb')

    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    pageObj = pdfReader.getPage(0)

    text = pageObj.extractText()

    pdfFileObj.close()

    store_path = 'C:/Users/Himanshu Prajapati/Downloads/Sampleproject/converted'
    abs_store_path = os.path.join(store_path,filename[:-4]+'.txt')


    writeFile = open(abs_store_path,'w')

    writeFile.write(text)

    writeFile.close()

