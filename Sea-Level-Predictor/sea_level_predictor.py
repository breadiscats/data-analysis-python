import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(12,8))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color = 'blue', s=8)

    # Create first line of best fit
    regress = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create range of year to 2050
    years_extended = np.arange(df['Year'].min(), 2051)
    sea_levels_extended = regress.intercept + regress.slope * years_extended
    plt.plot(years_extended, sea_levels_extended, color= 'red', label='Line of Best Fit')

    # Create second line of best fit
    # Filter data for years >= 2000
    df_recent = df[df['Year'] >= 2000]
    sec_bestfit = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    
    # Create range of year to 2050
    years_extended_2 = np.linspace(2000, 2050, 51)
    sea_levels_extended_2 = sec_bestfit.intercept + sec_bestfit.slope * years_extended_2
    plt.plot(years_extended_2, sea_levels_extended_2, color= 'green', label='Second Line of Best Fit')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
