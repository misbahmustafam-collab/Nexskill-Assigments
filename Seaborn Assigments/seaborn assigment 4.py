import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("FastFoodRestaurants.csv")
print(df.dtypes)
diffilter = df.head(30)
diffilter90 = df.head(90)

# Plot a countplot of city with hue by country using the first 30 rows
plt.figure(figsize=(10, 6))
g = sns.countplot(data=diffilter, x='city', hue='country')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

read = input("wait for me..")

"""
The relationship between x and y can be shown for different subsets of the data using the
hue, size, and style parameters. These parameters control what visual semantics are used to
identify the different subsets. It is possible to show up to three dimensions independently
by using all three semantic types, but this style of plot can be hard to interpret and is
often ineffective. Using redundant semantics (i.e. both hue and style for the same variable)
can be helpful for making graphics more accessible.
"""
#use seaborn to create a plot
g=sns.histplot(data=diffilter,x='address',y='city',hue='country')
g.figure.suptitle("sns.histplot(x=address,y=city,hue=country)")
g.figure.show()
read=input("wait for me..")


""""Plot rectangular data as a color-encoded matrix.

This is an Axes-level function and will draw the heatmap into the currently-active Axes if none is provided to the ax argument. Part of this Axes space will be taken and used to plot a colormap, unless cbar is False or a separate Axes is provided to cbar_ax."""
#.pivot(index="Model", columns="agency", values="price")
glue = diffilter.pivot(columns="agency", values="price")

g=sns.heatmap(glue)
g.figure.suptitle("sns.heatmap(glue)  - glue = dffilter.pivot(columns=agency, values=price)"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()