import pandas as pd
df=pd.read_csv('FastFoodRestaurants.csv')
print(df)
print("df-datatype",df.dtypes)

print("df.info():",df.info())
#display first 3 columns
print('first three columns:')
print(df.head(3))
print()

#display last 3 rows
print('last three rows:')
print(df.tail(3))
print()

#display first 3 rows
print('first three rows:')
print(df.head(3))
print()

#display last 3 columns
print('last three columns:')
print(df.iloc[:, -3:])
print()


#summary of statistics of dataframe using describe()method
print("#summary of statistics of dataframe using describe()method")
print(df.describe())


#counnting the number of rows and coulmns in dataframe using shape it return no of rows and coulmns in a tuple
print("#counting the number of rows and coulmns in dataframe using shape ():", df.shape)


#access the name of coulmn
city=df['city']
print('access the name of coulmn:df')
print(city)
print()


#selecting a single row using .loc
second_row=df.loc
print("#selecting a single row using .loc")
print(second_row)
print()


#selecting multiple rows using .loc
second_row3=df.loc
print("#selecting multiple rows using .loc")
print(second_row3)
print()


#selecting single row using .iloc
second_row=df.iloc
print("selecting single row using .iloc")
print(second_row)
print()


#selcting multiple coulmns using .iloc
second_row3=df.iloc
print("selecting multiple coulmns using .iloc")
print(second_row3)
print()


#selecting a single coulmn using .loc
single_column=df.loc[:, 'city']
print("selecting a single coulmn using .loc")
print(single_column)
print()



#combined selection of rows and columns using .loc
combined_selection=df.loc[1:3, ['name ', 'city']]
print("combined selection of rows and columns using .loc")
print(combined_selection)
print()


#combined selection of rows and columns using .iloc
combined_selection=df.iloc[1:3, [0,1]]
print("combined selection of rows and columns using.iloc")
print(combined_selection)
print()


