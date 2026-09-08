import pandas as pd

df = pd.read_csv('RealEstate-USA.csv')
print(df)
print("df -datatype" ,df.dtypes)
print("df.info():",df.info)
#display first 3 colums
print("first 3 colums")
print(df.iloc[:, :3]) # Display first 3 columns

print("df.describes():",df.describe())
#display 3 last rows
print("last 3 rows")
print(df.tail(3))
#summary of statistics of datafram using describe( method)
print("summary of statistics of datafram using describes() method", df.describe())
#couting the number if rows and columns in dataframe useing shape().it returns the no.of rows and columns inclosed in a tuple
print("Number of rows and columns in dataframe:", df.shape)
print()


#selecting a single row using .loc
print("#selecting a single row using .loc")
print(df.loc[1])  # Display the second row (index 1)
#selecting multiple rows using .loc
print("#selecting multiple rows using .loc")
print(df.loc[1:3])  # Display rows 2 to 4 (index 1 to 3)
#selecting a slice of rows using.loc
print("#selecting a slice of rows using .loc")
print(df.loc[1:3])  # Display rows 2 to 4 (index 1 to 3)
#conditional selection of rows using.loc
print("#conditional selection of rows using .loc")
print(df.loc[df['price'] > 500000])  # Display rows where price is greater than 500000
#combining rows and columns selection using.loc
print("#combining rows and columns selection using .loc")
print(df.loc[df["price"]>100000,["price","bed"] ])
#case 1 :using .loc - default case - ends here
print("#case2:using.loc with index_col - ends here")

