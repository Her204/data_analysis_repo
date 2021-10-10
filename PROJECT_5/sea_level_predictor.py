import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
    # Read data from file
    
    df = pd.read_csv("epa-sea-level.csv")
    values = df[df.columns[1]]
    years = df[df.columns[0]]
    years_extended = np.arange(1880,2051,1)
    slope, intercept, r_value, p_value, std_err = linregress(years,values)
    line = [slope*xi+ intercept for xi in years_extended]

    # Create scatter plot
    
    fig, ax = plt.subplots(figsize=(25,8)) 
    plt.scatter(years,
            values)

    # Create first line of best fit
    
    plt.plot(years_extended,line, color="orange")

    # Create second line of best fit
    
    years_extended_2 = np.arange(2000,2051,1)
    values_2000 = df[df.columns[1]].loc[df["Year"]>=2000]
    years_2000 = df["Year"].loc[df["Year"]>=2000]
    reg_2 = linregress(years_2000,values_2000)
    line_2 = [reg_2.slope*xi +reg_2.intercept for xi in years_extended_2]
    plt.plot(years_extended_2,line_2,color="brown")

    # Add labels and title
    
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.xticks(range(1850,2100,25))
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()

#data_append = pd.DataFrame(data={"Year":years_extended,"CSIRO Adjusted Sea Level":line},index=np.arange(134,171,1))
#data = df[df.columns[:2]].copy()
#goal = data.append(data_append)


