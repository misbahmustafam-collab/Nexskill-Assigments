import numpy as np
import  pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



df = pd.read_csv('RealEstate-USA.csv')
print(df.dtypes)
diffilter=df.head(30)
diffilter50=df.head(50)

sns.set(style="whitegrid")
g = sns.displot(data=diffilter, x="status", y="price")
g.figure.suptitle("sns.displot(data=diffilter, x='status', y='price')")
# display plot
g.figure.show()
read = input('wait')

g=sns.lineplot(data=df, x="bed", y="price", hue="status", marker="o")
g.figure.set_clip_box("sns.linplot(data='diffilter',x='bed',y='price',hue='stauts',marker='o')")
plt.show()

cat_fig = sns.catplot(data=diffilter, x="bed", y="price", hue="status")
cat_fig.fig.suptitle("sns.catplot(data=diffilter, x='bed', y='price', hue='status')")
plt.show()



