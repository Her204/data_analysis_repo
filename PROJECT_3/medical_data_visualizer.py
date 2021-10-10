import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Import data

df = pd.read_csv("medical_examination.csv")

# Add 'overweight' column

df['overweight'] = df["weight"]*10000/(df["height"])**2
df["overweight"]= np.where(df["overweight"] > 25,1,0)
# Normalize data by making 0 always good and 1 always bad. If the value of 'cholestorol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.

df["cholesterol"] = np.where(df["cholesterol"] > 1, 1, 0)
df["gluc"] = np.where(df["gluc"] > 1, 1, 0)


# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.DataFrame(pd.melt(df,id_vars=["cardio"],
                                  value_vars=sorted(["cholesterol",
                                  "gluc","smoke","alco","active",
                                  "overweight"])))

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the collumns for the catplot to work correctly.
    df_cat = df_cat.groupby(["cardio","variable"]).value
    df_cat = df_cat.value_counts().reset_index(name="total")
    df_cat = df_cat.sort_values(by=["variable","value"])

    # Draw the catplot with 'sns.catplot()'

    g = sns.catplot(x="variable",
               y= "total",
               col="cardio",
               hue="value",
               kind="bar",
               data=df_cat)
    fig = g.fig
    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig

# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df["ap_lo"]<=df["ap_hi"])&
                 (df["height"]>=df["height"].quantile(0.025))&
                 (df["height"]<=df["height"].quantile(0.975))&
                 (df["weight"]>=df["weight"].quantile(0.025))&
                 (df["weight"]<=df["weight"].quantile(0.975))]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True


    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(11,9))
    
    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr,vmin=-.08,vmax=0.28,
                      center=0.0001,linewidths=0.3,
                      annot=True,fmt=".1f",cbar_kws={"shrink":.52},
                      square=True,mask=mask)


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig

draw_cat_plot()
draw_heat_map()