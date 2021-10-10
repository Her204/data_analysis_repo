import pandas as pd
import os
import fitz
from tabula import read_pdf

files = []

def tables_from_pdf():
    for dirname, _, filenames in os.walk("/mnt/c/Users/User/OneDrive/LITO-CLASES/LITO-U/IX CICLO/ayudas-pdf"):
        for i,filename in enumerate(filenames):
            fil = os.path.join(dirname,filename)
            if filename.endswith(".pdf"):
                dataset = read_pdf(fil,pages="all")
                writer = pd.ExcelWriter(dirname+"/TABLAS/diapo_{}.xlsx".format(i),engine="xlsxwriter")
                for q, df in enumerate(dataset):
                    df_DF = pd.DataFrame(df)
                    df_DF.to_excel(writer,sheet_name="sheet_{}".format(q))
                writer.save()
    return print("Prcess complete")

def images_from_pdf():
    for dirname, _, filenames in os.walk("/mnt/c/Users/User/OneDrive/LITO-CLASES/LITO-U/IX CICLO/ayudas-pdf"):
        for i,filename in enumerate(filenames):
             if filename.endswith(".pdf"):
                 pdf_file = fitz.open("{}/{}".format(dirname,filename))
                 print(pdf_file)
                 #Reading the location where to save the file
                 number_of_pages = len(pdf_file)

                 #iterating through each page in the pdf
                 for current_page_index in range(number_of_pages):
                 #iterating through each image in every page of PDF
                     for img_index,img in enumerate(pdf_file.getPageImageList(current_page_index)):
                         xref = img[0]
                         image = fitz.Pixmap(pdf_file, xref)
                         try:
                             #if it is a is GRAY or RGB image
                             if image.n < 5:        
                                 image.writePNG("{}/image-{}-{}-{}.png".format(dirname+"/IMAGENES",i,current_page_index, img_index))
                             #if it is CMYK: convert to RGB first
                             else:                
                                 new_image = fitz.Pixmap(fitz.csRGB, image)
                                 new_image.writePNG("{}/image-{}-{}-{}.png".format(dirname+"/IMAGENES",i,current_page_index, img_index))
                         except:
                             continue
    return print(" Process complete")
tables_from_pdf()
images_from_pdf()