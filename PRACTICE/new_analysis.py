import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

columns_for_df = ['country_or_area-element_code-element-year-unit-value-value_footnotes-category',
 'Country Code-Country-Item Code-Item-Element Code-Element-Year Code-Year-Unit-Value-Flag',
 'Area Code-Area-Item Code-Item-Element Code-Element-Year Code-Year-Unit-Value-Flag',
 'Area Code-Area-Item Code-Item-Months Code-Months-Year Code-Year-Unit-Value-Flag-Note',
 'Country Code-Country-Source Code-Source-Indicator Code-Indicator-Year Code-Year-Unit-Value-Flag',
 'CountryCode-Country-ItemCode-Item-ElementGroup-ElementCode-Element-Year-Unit-Value-Flag',
 'Area Code-Area-Months Code-Months-Element Code-Element-Year Code-Year-Unit-Value-Flag',
 'Area Code-Area-Item Code-Item-ISO Currency Code-Currency-Year Code-Year-Unit-Value-Flag',
 'Recipient Country Code-Recipient Country-Item Code-Item-Donor Country Code-Donor Country-Year Code-Year-Unit-Value-Flag',
 'Reporter Country Code-Reporter Countries-Partner Country Code-Partner Countries-Item Code-Item-Element Code-Element-Year Code-Year-Unit-Value-Flag',
 'Survey Code-Survey-Breakdown Variable Code-Breakdown Variable-Breadown by Sex of the Household Head Code-Breadown by Sex of the Household Head-Indicator Code-Indicator-Measure Code-Measure-Unit-Value-Flag',
 'Area Code-Area-Item Code-Item-Element Code-Element-Months Code-Months-Year Code-Year-Unit-Value-Flag', 'Unnamed: 0']

files_diff_format = ['1/mnt/d/FAO_DATASET/fao_data_crops_data.csv',
   '3/mnt/d/FAO_DATASET/current_FAO/raw_files/ASTI_Researchers_E_All_Data_(Norm).csv',
   '2/mnt/d/FAO_DATASET/current_FAO/raw_files/CommodityBalances_Crops_E_All_Data_(Normalized).csv',
   '2/mnt/d/FAO_DATASET/current_FAO/raw_files/ConsumerPriceIndices_E_All_Data_(Normalized).csv',
   '3/mnt/d/FAO_DATASET/current_FAO/raw_files/Employment_Indicators_E_All_Data_(Norm).csv',
   '3/mnt/d/FAO_DATASET/current_FAO/raw_files/Environment_AirClimateChange_E_All_Data.csv',
   '2/mnt/d/FAO_DATASET/current_FAO/raw_files/Environment_Temperature_change_E_All_Data_(Normalized).csv',
   '2/mnt/d/FAO_DATASET/current_FAO/raw_files/Exchange_rate_E_All_Data_(Normalized).csv',
   '3/mnt/d/FAO_DATASET/current_FAO/raw_files/Food_Aid_Shipments_WFP_E_All_Data_(Normalized).csv',
   '3/mnt/d/FAO_DATASET/current_FAO/raw_files/Forestry_Trade_Flows_E_All_Data_(Normalized).csv',
   '3/mnt/d/FAO_DATASET/current_FAO/raw_files/Indicators_from_Household_Surveys_E_All_Data_(Normalized).csv',
   '2/mnt/d/FAO_DATASET/current_FAO/raw_files/Prices_Monthly_E_All_Data_(Normalized).csv', 
   '3/mnt/d/FAO_DATASET/current_FAO/__MACOSX/raw_files/._ASTI_Researchers_E_All_Data_(Norm).csv']

def extract_directory(path,lst=[]):
    for dirname,_,files in os.walk(path):
        for file in files:
            if file.endswith(".csv"):
                lst.append(os.path.join(dirname,file))
    return lst

def normalize_dataset(lst,ab=[],cd=[]):
    for a in lst:
        df = pd.read_csv(a)
        if "country_or_area" in df.columns and "-".join(df.columns) not in ab:
            cd.append(str(1)+a)    
            ab.append("-".join(df.columns))
            print("CASE 1",df.shape,df.columns)
        elif "Area" in df.columns and "-".join(df.columns) not in ab:
            cd.append(str(2)+a)    
            ab.append("-".join(df.columns))
            print("CASE 2",df.shape,df.columns)
            
        else:
            if "-".join(df.columns) not in ab:
                cd.append(str(3)+a)
                ab.append("-".join(df.columns))
                print("CASE 3",df.shape,df.columns)
    return [ab,cd]

def core_columns(columns_formats,files_names):
    columns_df = [a.split("-") for a in columns_formats]
    for file in files_names:
        df = pd.read_csv(file)
        for a in columns_df:
            try: 
                if a[0].endswith("Code"):
                    df = df.rename(columns={a[1]:"AREA-NEW"})
                    df = df.rename(columns={a[0]:"AREA-NEW CODE"})
                else:
                    df = df.rename(columns={a[0]:"AREA-NEW"})
            except:
                print("\n")
                print("-------error-------------")
                print("\n")
                continue
        print(df.columns)

print(core_columns(columns_for_df,extract_directory("/mnt/d/FAO_DATASET")))

#print(normalize_dataset(extract_directory("/mnt/d/FAO_DATASET")))

def process_data(files):
    for file in files:
        df = pd.read_csv(file)
        df = df.dropna(axis=0)
        if df.shape[0]<=10:
            continue
        else:
            print(df.columns,file.split("/")[-1])
            #try:
             #   df_particular_country = analyzing_particular_country(df,"United States of America")
             #   dic = look_values(df_particular_country)
             #   dic_col = [col for col in dic.keys()]
             #   #print(df_particular_country)
             #   print(file.split("/")[-1][:-4])
             #   count_particular_data(df_particular_country,
             #                         dic_col,
             #                         file.split("/")[-1][:-4])
            #except:
                #continue

def analyzing_particular_country(df,countr):
    if "country_or_area" in df.columns:
        df_2 = df.loc[df["country_or_area"] == countr]
        countries =df.country_or_area.loc[
                    df.country_or_area.apply(lambda x:x.upper().startswith("U"))].unique()
    elif "Area" in df.columns:
        df_2 = df.loc[df["Area"]==countr]
        countries = df.Area.loc[
                     df.Area.apply(lambda x: x.upper().startswith("U"))].unique()
    elif "Country" in df.columns:
        df_2 = df.loc[df["Country"]==countr]
        countries = df.Country.loc[df.Country.apply(lambda x:x.upper().startswith("U"))].unique()
    else:
        return "error"
    return df_2

def count_particular_data(df,cols,file_name):
    try:
        if "country_or_area" in df.columns:
            print("run")
            df_2 = df["country_or_area"]
            countries = df_2.unique()
        elif "Area" in df.columns:
            print("not run")
            df_2 = df["Area"]
            countries = df_2.unique()
        elif "Country" in df.columns:
            df_2 = df["Country"]
            countries = df_2.unique()
        else:
            return print("-----END_ERROR--------")
        print("-----START------")
        print(countries)
        print(" ")
        if "value" in df.columns:
            anali = df[[cols[-3],"value"]]    
        elif "Value" in df.columns:
            anali = df[[cols[-3],"Value"]]
        else:
            return print("---END_ERROR_2-----")
        anali = anali.loc[df_2==countries[-1]]
        anali = anali.value_counts().reset_index(name="TOTAL")
        val_anali = anali[anali.columns[0]].unique()
        print(anali[:20])
        plot_data(df=anali[:10],
                    x_la=anali.columns[1],
                    y_la=anali.columns[2],
                    col=anali.columns[0],
                    val=file_name)
                    
        #plot_map_data(df=anali,
        #              x_la=anali.columns[1],
        #              y_la=anali.columns[2],
        #              hue=anali.columns[0],
        #              val=file_name)
        #for val_1 in val_anali:
        #    data_plt = anali.loc[anali[anali.columns[0]]==val_1]
        #    print(data_plt[:20])
        print("-----END------")
    except:
        return print("------Central Error-----")

def look_values(df,dictionary={},lst=[]):
    for a in df.columns:
        if len(df[a].unique())<100:
            for b in df[a].unique():
                if not b in lst:
                    lst.append(b)
            dictionary[a] = lst
            lst = []
    return dictionary

def plot_data(df,x_la,y_la,col,val):
    #plt.subplots(figsize(100,100))
    g = sns.catplot(x=x_la,
                y=y_la,
                col=col,
                kind="bar",
                data=df)
    sns.set(rc={"figure.figsize":(10,30)})
    g.set_xticklabels(rotation=30)
    fig = g.fig
    fig.savefig("img/catplot_{}.png".format(val))
    return fig
    
def plot_map_data(df,x_la,hue,y_la,val):
    g = sns.kdeplot(
                x=eval("df.{}".format(x_la)),
                y=eval("df.{}".format(y_la)),
                shade=True,
                hue=eval("df.{}".format(hue)),
                bw_adjust=.5
                )
    fig = g.fig
    fig.savefig("img/maplot_{}.png".format(val))
    return fig

#process_data(extract_directory("/mnt/d/FAO_DATASET"))




