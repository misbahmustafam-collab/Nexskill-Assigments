import pandas as pd

df=pd.read_csv('startup_growth_investment_data.csv')
print(df)
print("df-datatypes",df.dtypes)

print("df.info():",df.info())
#display the first three rows
print("first three rows")
print(df.head(3))


#display the last three rows
print("last three rows")
print(df.tail())


#summary of statsitics of dataframe using describe() method
print("summary of statsitics of dataframe using describe() method", df.describe())

#counting the rows and coulmns in dataframe using shape().it returns the no of rows and coulmns in a tuple
print("counting the rows and coulmns in dataframe using shape():", df.shape())
print()


#access the name column
industry=df['industry']
print("access the name coulmn:df:")
print()


#selecting a single row using .loc
second_row=df.loc[1]
print("selecting single rows using .loc")
print(second_row)
print()



#selecting multiple rows using .iloc
second_row3=df.loc[1]
print("selecting multiple rows using .iloc")
print(second_row3)
print()



#selecting a single coulmn using .loc
second_row=df.loc[1]
print("selecting a single coulmn using .loc")
print(second_row)
print()


#selecting multiple coulmn using .iloc
second_row3=df.iloc[1]
print("selecting multiple coulmn using .iloc")
print(second_row3)
print()


#selecting a silce of rows using .loc
second_row2=df.loc[1:3]
print("selecting a silce of rows using .loc")
print(second_row2)
print()



#selecting a silce of coulmn using .iloc
second_row4=df.iloc[1:2]
print("selecting a silce of coulmn using .iloc")
print(second_row2)
print()


#conditional selection of rows using .loc
second_row5=df.loc[df['industry'] == 'Technology']
print("conditional selection of rows using .loc")
print(second_row5)
print()


