import os
import pandas as pd
import pymysql
from sqlalchemy import create_engine

lst = []
for dirname,_,files in os.walk("/mnt/d/FAO_DATASET"):
    for file in files:
        if file.endswith("csv"):
            lst.append(os.path.join(dirname,file))
mydb = create_engine("mysql+pymysql://root:Her976300403@localhost:3306/testdatabase",echo=False)

for element in lst:
    df = pd.read_csv(element)
    try:
         name_1 = element.split("/")[-1][:-4]
         df.to_sql(name="table_{}".format(name_1),con=mydb,
                if_exists="replace", index=False)
         print("done")
    except:
        print("error")
        continue

