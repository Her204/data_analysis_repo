from tabula import read_pdf
import pandas as pd 
import tabula

tables = read_pdf("/mnt/c/users/user/onedrive/escritorio/Miracajp.pdf",pages="all")

path = "/mnt/c/users/user/onedrive/escritorio/pruebas/data.xlsx"

writer = pd.ExcelWriter(path, engine="xlsxwriter")

for i, df in enumerate(tables):
    df_data = pd.DataFrame(df)
    if df_data.shape[0] < 10:
        continue
    else:
        df_data.to_excel(writer,sheet_name="table_{}".format(i))

writer.save()
