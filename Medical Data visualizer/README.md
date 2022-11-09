# Medical Data Visualizer

This is the third project of freeCodecamp Data Analysis with Python Course. <br>
the objectives are :

1. Create a chart similar to examples/Figure_1.png, where we show the counts of good and bad outcomes for the cholesterol, gluc, alco, active, and smoke variables for patients with cardio=1 and cardio=0 in different panels.
2. Use the data to complete the following tasks in medical_data_visualizer.py:

> 1. Add an overweight column to the data. To determine if a person is overweight, first calculate their BMI by dividing their weight in kilograms by the square of their height in meters. If that value is > 25 then the person is overweight. Use the value 0 for NOT overweight and the value 1 for overweight.
> *Normalize the data by making 0 always good and 1 always bad. If the value of cholesterol or gluc is 1, make the value 0. If the value is more than 1, make the value 1.
> 2. Convert the data into long format and create a chart that shows the value counts of the categorical features using seaborn's catplot(). The dataset should be split by 'Cardio' so there is one chart for each cardio value. The chart should look like examples/Figure_1.png. 
> * Clean the data. Filter out the following patient segments that represent incorrect data:
> > * diastolic pressure is higher than systolic (Keep the correct data with (df['ap_lo'] <= df['ap_hi']))
> > * height is less than the 2.5th percentile (Keep the correct data with (df['height'] >= df['height'].quantile(0.025)))
> > * height is more than the 97.5th percentile
> > * weight is less than the 2.5th percentile
> > * weight is more than the 97.5th percentile
> 3. Create a correlation matrix using the dataset. Plot the correlation matrix using seaborn's heatmap(). Mask the upper triangle. The chart should look like examples/Figure_2.png.
<br>
Click <a href='https://replit.com/@FarrazNouval1/boilerplate-medical-data-visualizer'>here</a> to see my repl on replit.
