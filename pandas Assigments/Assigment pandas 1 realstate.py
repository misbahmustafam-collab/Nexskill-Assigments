import pandas as pd
df=pd.read_csv("RealEstate-USA.csv")
print(df)
print("df-data types",df.dtypes)
print("df.info():",df.info())
#display last three rows
print("last three roww")
print(df.tail(3))

#display first three rows
print("first three rows")
print(df.head(3))

#display first three coulmns
print("first three coulmns")
print(df.head(3))

#display last three coulmns
print("last three coulmns")
print(df.tail(3))


#summary of statistics of dataframe using describes () method
print("summary of statistics of dataframe using describes()method:",df.describe())


#counting the rows and coulmns in dataframe using shape()it return the no of rows and coulmns enclosed in a tuple
print("counting the rows and coulmns in dataframe using shape():",df.shape)
print()

#selecting a single row using .loc
second_row=df.loc[1]
print("selecting a single row using .loc")
print(second_row)
print()


#selecting multiple rows using .loc
second_rows2=df.loc[[1,3]]
print("selecting multiple rows using .loc")
print(second_rows2)
print()

#selecting a slice of rows using .loc
second_row3=df.loc[1:5]
print("selecting a slice of rows using .loc")
print(second_row3)
print()


#access multiple coulmns
bed=df[['bed']]
print("access multiple coulmns:df:")
print(bed)
print()

#selecting a single coulmn using .loc
second_row5=df.loc[:1,'bed']
print("selecting a single coulmn using .loc")
print(second_row5)
print()

#selecting multiple coulmns using .loc
second_row6=df.loc[:,['bed']]
print("#selecting multiple coulmns using .loc")
print(second_row6)
print()



#selecting a single row using .iloc
second_row=df.iloc[1]
print("selecting a single row using .iloc")
print(second_row)
print()



#Selecting multiple rows using .iloc
second_row2 = df.iloc[[1, 3, 5]]
print("#Selecting multiple rows using .iloc")
print(second_row2)
print()



#Selecting a slice of rows using .iloc
second_row3 = df.iloc[2:5]
print("#Selecting a slice of rows using .iloc")
print(second_row3)
print()



#Combined row and column selection using .iloc
second_row8 = df.iloc[[1, 3,5],2:4]
print("#Combined row and column selection using .iloc")
print(second_row8)
print()




