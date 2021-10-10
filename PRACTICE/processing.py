import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as plt
df = pd.read_csv("/mnt/c/users/user/onedrive/escritorio/sales_data.csv")

columns = df.columns
for col in columns:
    print(df[col].unique())
