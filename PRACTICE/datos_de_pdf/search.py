from googlesearch import search
from tabula import read_pdf
import pandas as pd
import tabula 

query = input("Search something here: ")
lst = []

for a in search(query, tld="co.in",num=3,stop=3,pause=2):
    print(a)
    lst.append(a)
print(lst)

path = "/mnt/c/users/user/onedrive/escritorio/tablas_minas_2.xlsx"

writer = pd.ExcelWriter(path,engine="xlsxwriter")
x = 1
for lst_element in lst:
    if lst_element.endswith(".pdf"):
        tables_of_tables =read_pdf(lst_element,pages="all")
        for table in tables_of_tables:
            x += 1
            df = pd.DataFrame(table)
            if df.shape[0] < 10:
                continue
            else:
                df.to_excel(writer,sheet_name="como_{}".format(x))
writer.save()
