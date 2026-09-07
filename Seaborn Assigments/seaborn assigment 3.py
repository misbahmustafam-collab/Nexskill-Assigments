import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('startup_growth_investment_data.csv')
print(df.dtypes)
diffilter=df.head(40)
diffilter100=df.head(100)

g = sns.barplot(data=diffilter, x='Startup Name', y='Industry', hue='Funding Rounds')
g.figure.supxlabel("sns.barplot(data=diffilter,x=Startup Name,y=Industry,hue=funding Rounds)")
g.figure.show()
read=input("Wait for me....")


g=sns.boxenplot(data=diffilter,x='Startup Name',y='Industry',hue='Funding Rounds')
g.figure.align_labels("sns.boxenplot(data=diffilter,x=Startup Name,y=Industry,hue=Funding Rounds)")
g.figure.show()
read=input("wait for me....")