import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df=pd.read_csv('Real_Estate_Sales_2001-2022_GL-Short.csv')
print(df.dtypes)
diffilter=df.head(30)
diffilter80=df.head(80)

g=sns.pairplot(data=diffilter,x='Serial Number',y='List Year',hue='Value')
g.figure.supxlabel("sns.pairplot(data=diffilter,x=Serial Number,y=List Year,hue=Value)")
g.figure.show()
read=input("wait for me...")


g=sns.miscplot(data=diffilter,x='Serial Number',y='List Year',hue='Value')
g.figure.supxlabel("sns.miscplot(data=diffilter,x=Serial Number,y=List Year,hue=Value)")
g.figure.show()
read=input("wait for me..")


