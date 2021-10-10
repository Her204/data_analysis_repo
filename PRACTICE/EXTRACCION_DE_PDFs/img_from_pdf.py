import fitz
from googlesearch import search
import urllib.request

query = input("Search something here: ")
lst = []

for a in search(query, tld="co.in",num=3,stop=3,pause=2):
    print(a)
    lst.append(a)

for i, link in enumerate(lst):
    urllib.request.urlretrieve(link,"/mnt/c/users/user/onedrive/escritorio/pruebas/filename_{}.pdf".format(i))
    pdf_file = fitz.open("/mnt/c/users/user/onedrive/escritorio/pruebas/filename_{}.pdf".format(i))

    #Reading the location where to save the file
    location = "/mnt/c/users/user/onedrive/escritorio/pruebas/prueba"
    number_of_pages = len(pdf_file)

    #iterating through each page in the pdf
    for current_page_index in range(number_of_pages):
    #iterating through each image in every page of PDF
        for img_index,img in enumerate(pdf_file.getPageImageList(current_page_index)):
            print(img)
            xref = img[0]
            image = fitz.Pixmap(pdf_file, xref)
            try:
                #if it is a is GRAY or RGB image
                if image.n < 5:        
                    image.writePNG("{}/image{}-{}.png".format(location,current_page_index, img_index))
                #if it is CMYK: convert to RGB first
                else:                
                    new_image = fitz.Pixmap(fitz.csRGB, image)
                    new_image.writePNG("{}/image{}-{}.png".format(location,current_page_index, img_index))
            except:
                continue
