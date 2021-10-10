import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv")

# Clean data.

df["date"] = pd.to_datetime(df["date"],format="%Y-%m-%d")

df = df[(df["value"] > df["value"].quantile(0.025))&
        (df["value"] < df["value"].quantile(0.975))]

def draw_line_plot():
    # Draw line plot
    fig,ax= plt.subplots(figsize=(16,5))
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    sns.lineplot(data=df,x="date",y="value",color="brown",linewidth=1)
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar["month"] = df_bar["date"].dt.month
    df_bar["Years"] = df_bar["date"].dt.year
    df_bar = df_bar.sort_values("month")
    DIQUI = {1:'January', 2:'February', 3:'March',
                   4:'April', 5:'May', 6:'June', 7:'July',
                   8:'August', 9:'September', 10:'October',
                   11:'November', 12:'December'}
    for val,key in DIQUI.items():
        df_bar.month = df_bar.month.replace(val,key)
    df_bar = df_bar.rename(columns={"value":"Average Page Views"})
    # Draw bar plot
    fig, ax = plt.subplots(figsize=(9,8))
    sns.barplot(data=df_bar,x="Years",
                y="Average Page Views",
                hue="month",palette="magma")
    #plt.legend(labels=months)


 
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    # Draw box plots (using Seaborn)
    Months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
             'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    fig, ax = plt.subplots(figsize=(16,5.6))
    plt.subplot(1,2,1)
    sns.boxplot(data=df_box,x="year",y="value")
    plt.xlabel("Year")
    plt.ylabel("Page Views")
    plt.title("Year-wise Box Plot (Trend)")
    plt.subplot(1,2,2)
    sns.boxplot(data=df_box,x="month",order=Months,y="value")
    plt.xlabel("Month")
    plt.ylabel("Page Views")
    plt.title("Month-wise Box Plot (Seasonality)")
    



    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

draw_line_plot()
draw_bar_plot()
draw_box_plot()