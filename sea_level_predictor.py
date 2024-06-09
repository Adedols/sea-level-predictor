import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    sns.scatterplot(data = df, x= df.Year, y = df['CSIRO Adjusted Sea Level']);


    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(1880, 2051))
    sea_level_pred = intercept + slope * years_extended
    plt.plot(years_extended, sea_level_pred, label='Best Fit Line 1880-2050', color='red')


    # Create second line of best fit
    df_2000 = df[df['Year'] >= 2000]
    slope_2000, intercept_2000, r_value_2000, p_value_2000, std_err_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    years_extended_2000 = pd.Series(range(2000, 2051))
    sea_level_pred_2000 = intercept_2000 + slope_2000 * years_extended_2000
    plt.plot(years_extended_2000, sea_level_pred_2000, label='Best Fit Line 2000-2050', color='green')



    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')


    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca() 