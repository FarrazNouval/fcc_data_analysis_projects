import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    df2k = df[df.Year >= 2000]

    # Create scatter plot
    plt.scatter(x=df.Year, y=df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    lr1 = linregress(x=df.Year, y=df['CSIRO Adjusted Sea Level'])
    x1 = range(df.Year.min(), 2051, 1)
    y1 = x1*lr1.slope + lr1.intercept
  
    plt.plot(x1, y1, 'r')


    # Create second line of best fit
    lr2 = linregress(x=df2k.Year, y=df2k['CSIRO Adjusted Sea Level'])
    x2 = range(2000, 2051, 1)
    y2 = x2*lr2.slope + lr2.intercept
  
    plt.plot(x2, y2, 'b')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()