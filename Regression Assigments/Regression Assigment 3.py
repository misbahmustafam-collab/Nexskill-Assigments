import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Let's read the CSV file and package it into a DataFrame:
df = pd.read_csv('car data.csv')
import pandas as pd

# Check dataset
print(df.head())
print(df.columns.tolist())
print(df.dtypes)

# Correlation of numeric columns
print(df.corr(numeric_only=True))
# Remove original Date column
df = df.drop('Car_Name', axis=1)

print(df.dtypes)
print(df.corr(numeric_only=True))

#Once the data is loaded in, let's take a quick peek at the first 5 values using the head() method:
print(df.head())
print(dtypes := df.dtypes)
#We can also check the shape of our dataset via the shape property:
print(df.columns.tolist())
# Scatter Plot
df.plot.scatter(
    x='Present_Price',
    y='Selling_Price',
    title='Present Price vs Selling Price'
)
plt.show()

print("df.corr():        " , df.corr(numeric_only=True))


print("df.describe():                    " , df.describe())


print("Minimum Present_Price:", df['Present_Price'].min())
print("Maximum Present_Price:", df['Present_Price'].max())

X = df[['Selling_Price']]
y = df['Present_Price']

print("X:")
print(X)

print("y:")
print(y)

print(df['Present_Price'].values) # [2.5 5.1 3.2 8.5 3.5 1.5 9.2 ... ]
print(df['Present_Price'].values.shape) # (25,)

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
df = pd.read_csv('car data.csv')
import pandas as pd

# Check Car Dataset
print(df.head())
print(df.columns.tolist())
print(df.dtypes)

# Correlation of numeric columns
print(df.corr(numeric_only=True))

print(df.dtypes)
print(df.corr(numeric_only=True))

print("df.head():  \n",df.head())

print("df.shape: \n" , df.shape)

print("df.describe().round(2).T:    \n",df.describe().round(2).T)

import seaborn as sns # Convention alias for Seaborn


variables = ['Temperature (C)', 'Humidity', 'Wind Speed (km/h)', 'Pressure (millibars)']

# Regression Plots for Car Dataset

import seaborn as sns
import matplotlib.pyplot as plt

variables = ['Present_Price', 'Kms_Driven']

for var in variables:
    sns.regplot(x=var, y='Selling_Price', data=df)
    plt.title(f'Regression Plot of {var} and Selling Price')
    plt.show()

# Correlation
correlations = df.corr(numeric_only=True)
print("Correlations:\n", correlations)

# Heatmap
sns.heatmap(correlations, annot=True)
plt.title('Heatmap of Car Dataset')
plt.show()

# Features and Target
X = df[['Present_Price', 'Kms_Driven']]
y = df['Selling_Price']

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