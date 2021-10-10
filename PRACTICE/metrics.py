import pandas as pd
tables = pd.read_html("https://es.wikipedia.org/wiki/Econom%C3%ADa_del_Per%C3%BA")
path = "/mnt/c/users/user/onedrive/escritorio/file.xlsx"
writer = pd.ExcelWriter(path,engine="xlsxwriter")
for i, df in enumerate(tables):
    pd.DataFrame(df).to_excel(writer,sheet_name="table_{}".format(i),float_format="%.2f")
writer.save()