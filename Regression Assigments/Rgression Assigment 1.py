import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Let's read the CSV file and package it into a DataFrame:
df = pd.read_csv('weatherHistory.csv')
import pandas as pd

# Convert Date string to datetime
df['Date'] = pd.to_datetime(df['Apparent Temperature (C)'])

# Create numeric features
df['year'] = pd.to_datetime(df['Apparent Temperature (C)']).dt.year
df['month'] = pd.to_datetime(df['Apparent Temperature (C)']).dt.month
df['day'] = pd.to_datetime(df['Apparent Temperature (C)']).dt.day

# Remove original Date column
df = df.drop('Apparent Temperature (C)', axis=1)

print(df.dtypes)
print(df.corr(numeric_only=True))

#Once the data is loaded in, let's take a quick peek at the first 5 values using the head() method:
print(df.head())
print(dtypes := df.dtypes)
#We can also check the shape of our dataset via the shape property:
print(df.columns.tolist())
# Scatter Plot
df.plot.scatter(
    x='Temperature (C)',
    y='Humidity',
    title='Temperature vs Humidity'
)

plt.show()

print("df.corr():        " , df.corr(numeric_only=True))


print("df.describe():                    " , df.describe())


print("Minimum Temperature:", df['Temperature (C)'].min())
print("Maximum Temperature:", df['Temperature (C)'].max())

X = df[['Humidity']]
y = df['Temperature (C)']

print("X:")
print(X)

print("y:")
print(y)

print(df['Humidity'].values) # [2.5 5.1 3.2 8.5 3.5 1.5 9.2 ... ]
print(df['Temperature (C)'].values.shape) # (25,)

print(X.shape) # (25, 1)
print(X)      # [[2.5] [5.1]  [3.2] ... ]
SEED = 42

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = SEED)


print(X_train) # [[2.7] [3.3] [5.1] [3.8] ... ]
print(y_train) # [[25] [42] [47] [35] ... ]


#Training a Linear Regression Model

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)
print(regressor.intercept_)
print(regressor.coef_)
def calc(slope, intercept, Temp_max):
    return slope*Temp_max+intercept

score = calc(regressor.coef_, regressor.intercept_, 9.5)
print(score) 
score = regressor.predict([[9.5]])
print(score) # 94.80663482
y_pred = regressor.predict(X_test)

df_preds = pd.DataFrame({'Actual': y_test.squeeze(), 'Predicted': y_pred.squeeze()})
print(df_preds)
from sklearn.metrics import mean_absolute_error, mean_squared_error,r2_score
import numpy as np

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f'Mean absolute error: {mae:.2f}')
print(f'Mean squared error: {mse:.2f}')
print(f'Root mean squared error: {rmse:.2f}')
print(f'R2 Score: {r2:.2f}')
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

path_to_file = ''
df = pd.read_csv('weatherHistory.csv')
import pandas as pd

# Convert Date string to datetime
df['Apparent Temperature (C)'] = pd.to_datetime(df['Apparent Temperature (C)'])

# Create numeric features
df['year'] = df['Apparent Temperature (C)'].dt.year
df['month'] = df['Apparent Temperature (C)'].dt.month
df['day'] = df['Apparent Temperature (C)'].dt.day

# Remove original Date column
df = df.drop('Apparent Temperature (C)', axis=1)

print(df.dtypes)
print(df.corr(numeric_only=True))

print("df.head():  \n",df.head())

print("df.shape: \n" , df.shape)

print("df.describe().round(2).T:    \n",df.describe().round(2).T)

import seaborn as sns # Convention alias for Seaborn


variables = ['Temperature (C)', 'Humidity', 'Wind Speed (km/h)', 'Pressure (millibars)']

for var in variables:
    sns.regplot(x=var, y='Wind Speed (km/h)', data=df)
    plt.title(f'Regression plot of {var} and Wind Speed')
    plt.show()
plt.figure()
correlations = df.corr(numeric_only=True)
print("correlations...\n" , correlations)
# annot=True displays the correlation values
g = sns.heatmap(correlations, annot=True).set(title='Heat map of Wind Speed (km/h) - Temperature (C)')
# Display the plot
plt.show()
read = input("Wait for me....")

y = df['Wind Speed (km/h)']
X = df[['Temperature (C)', 'Humidity', 'Pressure (millibars)']]

SEED = 200
#After setting our X and y sets, we can divide our data into train and test sets. We will be using the same seed and 20% of our data for training:
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size=0.2, 
                                                    random_state=SEED)

#After splitting the data, we can train our multiple regression model. Notice that now there is no need to reshape our X data, once it already has more than one dimension:
print("X.shape # (48, 4):     \n", X.shape )   

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

regressor.fit(X_train, y_train)

#After fitting the model and finding our optimal solution, we can also look at the intercept:
print("regressor.intercept_......\n", regressor.intercept_)

#And at the coefficients of the features
print("regressor.coef_ " , regressor.coef_)


feature_names = X.columns
model_coefficients = regressor.coef_

coefficients_df = pd.DataFrame(data = model_coefficients, 
                              index = feature_names, 
                              columns = ['Coefficient'])
print(coefficients_df)


#In the same way we had done for the simple regression model, let's predict with the test data:
y_pred = regressor.predict(X_test)


results = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print("Actual vs Predicted.....\n" , results)

from sklearn.metrics import mean_absolute_error, mean_squared_error
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print(f'Mean absolute error: {mae:.2f}')
print(f'Mean squared error: {mse:.2f}')
print(f'Root mean squared error: {rmse:.2f}')

actual_minus_predicted = sum((y_test - y_pred)**2)
actual_minus_actual_mean = sum((y_test - y_test.mean())**2)
r2 = 1 - actual_minus_predicted/actual_minus_actual_mean
print('R²:', r2)