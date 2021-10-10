import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("sales_data.csv")
df["B/C"] = df.Profit/df.Cost

def cols(name,num,x,year,country):
    df_1 = df.loc[df.Year==year][["Age_Group",
                              "Customer_Gender",
                              "Country",
                              "Product",
                              name]]

    df_1_M = df_1.loc[df.Customer_Gender=="M"][["Age_Group",
                                            "Country",
                                            "Product",
                                            name]]
    df_1_F = df_1.loc[df.Customer_Gender=="F"][["Age_Group",
                                            "Country",
                                            "Product",
                                            name]]

    df_1_M = df_1_M.loc[df_1_M.Country==country][["Age_Group",
                                                      "Product",
                                                      name]]
    df_1_F = df_1_F.loc[df_1_F.Country==country][["Age_Group",
                                                      "Product",
                                                      name]]

    df_1_M = eval("pd.DataFrame(df_1_M.groupby(['Product','Age_Group'])[name].{}())".format(x))
    df_1_F = eval("pd.DataFrame(df_1_F.groupby(['Product','Age_Group'])[name].{}())".format(x))                                     

    df_1_M = df_1_M.reset_index(["Product","Age_Group"])
    df_1_F = df_1_F.reset_index(["Product","Age_Group"])

    pl_F= df_1_F.pivot(index="Age_Group",columns="Product",values=name)
    pl_M= df_1_M.pivot(index="Age_Group",columns="Product",values=name)

    pl_M_top= pl_M[pl_M.mean(axis=0).sort_values(ascending=False).iloc[:num].index]
    pl_F_top= pl_F[pl_F.mean(axis=0).sort_values(ascending=False).iloc[:num].index]

    return [pl_M_top,pl_F_top]

path = "/mnt/c/users/user/onedrive/escritorio"  
year = int(input("which year: "))  
country = input("\n.-".join(df.Country.unique())+" wich country: ")
title_1 = "{} from {} by Products on year "+str(year)+ " "+country

fig = plt.figure(figsize=(28,20))

ax1 = fig.add_subplot(2,2,1)
cols("B/C",5,"mean",year,country)[0].plot(kind="barh",colormap="Paired",title=title_1.format("Relation Profits/Costs","Male"),rot=0,ax=ax1)#,
            #figsize=(12,10)).figure.savefig(path+"/plt_F.png")
#ax = fig.add_subplot(ax)
ax2= fig.add_subplot(2,2,3)
cols("B/C",5,"mean",year,country)[1].plot(kind="barh",colormap="Paired",title=title_1.format("Relation Profits/Costs","Female"),rot=0,ax=ax2)#,
            #figsize=(12,10)).figure.savefig(path+"/plt_M.png")
#ax = fig.add_subplot(ax)
ax3 = fig.add_subplot(2,2,2)
cols("Profit",5,"sum",year,country)[0].plot(kind="barh",colormap="Paired",title=title_1.format("Profits","Male"),rot=0,ax=ax3)
#ax=fig.add_subplot(ax)
ax4= fig.add_subplot(2,2,4)
cols("Profit",5,"sum",year,country)[1].plot(kind="barh",colormap="Paired",title=title_1.format("Profits","Female"),rot=0,ax=ax4)
#ax=fig.add_subplot(ax)

fig.savefig(path+"/important_plot.png")
