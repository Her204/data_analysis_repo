import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("/mnt/c/users/user/onedrive/escritorio/sales_data.csv")

df_col_num = [col for col in df.columns if str(df[col].dtype).startswith("i") or str(df[col].dtype).startswith("f")]

df_col_string = [col for col in df.columns if str(df[col].dtype).startswith("o") and col != "Date"]

cols = [col for col in df_col_string if col != "Country" and len(df[col].unique()) < 10]

melt_data =pd.DataFrame(pd.melt(df, id_vars=df_col_string[3],
    value_vars=cols)).value_counts().reset_index(name="total")

def fig_return(data):
    for a in data["Country"].unique():
        values = data.loc[data["Country"]==a]
        g = sns.catplot(data=values,
                    x="variable",
                    y="total",
                    col = "Country",
                    hue="value",
                    kind="bar", aspect=25/5)
        fig = g.fig
        fig.savefig("IMAGES/categorical_plot_{}".format(a))
    pass

def fig_return_heat(data):
    data_corr = data.corr()
    mask = np.zeros_like(data_corr)
    mask[np.triu_indices_from(mask)] = True
    fig, ax = plt.subplots(figsize=(12,10))
    sns.heatmap(data_corr,vmin=-.08,vmax=0.28,
                center=0.0001,linewidths=0.3,
                annot=True,fmt=".1f",cbar_kws={"shrink":.52},
                square=True,mask=mask)
    fig = plt.savefig("IMAGES/heat_sales.png")
    return fig

def data_to_excel():
    path = "/mnt/c/users/user/onedrive/escritorio/something_read.xlsx"

    writer = pd.ExcelWriter(path,engine="xlsxwriter")

    melt_data.to_excel(writer,sheet_name="melt_data")
    df[df_col_num].mean(axis=0).to_excel(writer,sheet_name="means_df")
    df[df_col_num].corr().to_excel(writer,sheet_name="correlations")
    df[df_col_num].to_excel(writer,sheet_name="numeric_cols",float_format="%.2f")
    data_2 = np.fft.fftn(df[df_col_num].values)
    pd.DataFrame(data_2.round()).to_excel(writer,sheet_name="fft")
    data_3 = np.fft.ifftn(data_2)
    pd.DataFrame(data_3.round()).to_excel(writer,sheet_name="ifft")
    writer.save()
    pass

fig_return_heat(df[df_col_num])
fig_return(melt_data)
data_to_excel()
