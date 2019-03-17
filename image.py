from PIL import Image,ImageEnhance, ImageFilter
import pytesseract
import os

def img_to_txt(filename):
    save_path = 'C:/Users/Himanshu Prajapati/Downloads/Sampleproject/data'
    abs_path = os.path.join(save_path,filename)
    im = Image.open(abs_path)
    text = pytesseract.image_to_string(im)

    store_path = 'C:/Users/Himanshu Prajapati/Downloads/Sampleproject/converted'
    abs_store_path = os.path.join(store_path,filename[:-4]+'.txt')


    writeFile = open(abs_store_path,'w')

    writeFile.write(text)

    writeFile.close()
