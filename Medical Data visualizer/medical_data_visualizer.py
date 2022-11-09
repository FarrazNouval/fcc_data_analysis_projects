import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
bmi = df.weight / np.square(df.height / 100)
df['overweight'] = [1 if i > 25 else 0 for i in bmi]

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.

df['cholesterol'] = [0 if i == 1 else 1 for i in df.cholesterol]
df['gluc'] = [0 if i == 1 else 1 for i in df.gluc]


# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    cols = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
  
    df_cat = pd.melt(df, 
                     id_vars=['cardio'],
                     value_vars=cols)


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = df_cat.reset_index().groupby(['variable', 'cardio', 'value'], as_index=False).agg('count').rename(columns={'index': 'total'})
    

    # Draw the catplot with 'sns.catplot()'
    fig = sns.catplot(data=df_cat, x='variable', 
                      y='total', hue='value', 
                      col='cardio', kind='bar').fig


    # Get the figure for the output


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df.ap_lo <= df.ap_hi) & 
                 (df.height >= df.height.quantile(0.025)) &
                 (df.height <= df.height.quantile(0.975)) &
                 (df.weight >= df.weight.quantile(0.025)) &
                 (df.weight <= df.weight.quantile(0.975))]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True



    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 9))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(data=corr, mask=mask, 
                vmin=-0.16, vmax=0.32,
                annot=True, square=True,
                fmt='.1f')

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
