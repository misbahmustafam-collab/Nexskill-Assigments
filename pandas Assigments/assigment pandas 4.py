import pandas as pd

df=pd.read_csv('Real_Estate_Sales_2001-2022_GL-Short.csv')
print(df)
print("df_datatype",df.dtypes)

print("df.info():",df.info())

#selecting first three rows
print("selecting first three row")
print(df.head())


#selecting last three rows
print("selecting last three rows")
print(df.tail())

#summary of statistics of dataframe using describe () method
print("summary of statistics of dataframe using describes()method",df.describe())


#counting the rows and coulmns in dataframe using shape it return the no.of rows and coulmns enclosed in a tuple
print("counting the rows and coulmns in dataframe using shape():",df.shape)
print()



#case no 1 : using .loc -default case - starts here
#selecting a single row using .loc
second_row=df.loc[1]
print("selecting a single row using .loc")
print(second_row)
print()


#selecting multiple rows using .loc
second_row2=df.loc[3]
print("selecting multiple rows using .loc")
print(second_row2)
print()



#selecting a slice of rows using .loc
second_row3=df.loc[4]
print("selecting a silce of rows using .loc")
print(second_row3)
print()


#selecting a single coulmn using .iloc
second_row=df.loc[3]
print("selecting a single coulmn using .iloc")
print(second_row3)
print()  


#case no 1 using loc ends here

#case no 2 using .loc with index col - starts here



#combined the rows and coulmn using describe method
# second cycle-with index_col as sale amount
# why second_cycle note index -, index_col='sale amount'
df_index_col=pd.read_csv("Real_Estate_Sales_2001-2022_GL-Short.csv")
print(df_index_col)
print(df_index_col.dtypes)
print(df_index_col.info())


#second cycle-with index - col as sale amount





#conditional selection of rows using .loc
second_row4=df_index_col.loc
print("conditional selection of rows using .loc")
print(second_row4)
print()


print("case 3 using iloc starts here")
#case 3 using .iloc starts here

#selecting a single row using iloc

second_row=df_index_col.iloc[1]
print("selecting a single row using iloc")
print(second_row)
print()


#selecting multiple rows using .iloc
second_row3=df_index_col.iloc[2]
print("selecting multiple rows using .iloc")
print(second_row4)
print()



#selecting a single coulmn using .iloc
second_row2=df_index_col.iloc[3]
print("selecting a single coulmn using .iloc ")
print(second_row2)
print()



#delete row with index 1
df.drop(1, axis=0,inplace=True)
#delete row with index 3 and 5
df.drop([3,5],axis=0,inplace=True)
#display the modified dataframe after deleting rows
print("modified dataframe-remove rows:")
print(df)




#delete age coulmn





##########################



#case no 2 using .loc with index col - starts here
