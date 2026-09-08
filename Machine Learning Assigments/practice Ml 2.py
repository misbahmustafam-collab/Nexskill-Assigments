import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv("weather_2016_2020_daily.csv")
print(df)
print("df_datatypes:", df.dtypes)

print(df.info())
df.plot.scatter(x='Temp_max',y='Dew_max',title='scatter plot of Temp_max and Dew_max percentage')
plt.show()
#graph2
df.plot.scatter(x='Temp_avg',y='Dew_avg',title='scatter plot of Temp_avg and Dew_avg percentage')
plt.show()
df_num = df.select_dtypes(include='number')
print("df.corr():")
print(df_num.corr())

print("df.decribes():")
print(df.describe())

df.plot.scatter(x='Temp_max',y='Dew_max',title='scatter plot of Temp_max and Dew_max percentage')
print("df['Temp_max']:",df['Temp_max'])
print("df['Dew_max']:",df['Dew_max'])
y=df['Dew_max'].values.reshape(-1,1)
x=df['Temp_max'].values.reshape(-1,1)

print("y:",y)
print("x:",x)


print(df['Dew_max'].values)
print(df['Temp_max'].values.shape)


print(x.shape)
print(x)
SEED=42
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=SEED)

regressor=LinearRegression()
regressor.fit(x_train, y_train)
print(regressor.intercept_)
print(regressor.coef_)
linear_pred=regressor.predict(x_test)
print(linear_pred)
print("linear Regression Metrics")
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
linear_Mae = mean_absolute_error(y_test, linear_pred)
linear_Mse = mean_squared_error(y_test, linear_pred)
linear_Rmse = np.sqrt(linear_Mse)
linear_R2 = r2_score(y_test, linear_pred)

print("Mae:", linear_Mae)
print("Mse:", linear_Mse)
print("Rmse:", linear_Rmse)
print("R2 score:", linear_R2)

#apply second logrothim
from sklearn.linear_model import Lasso
regressor=Lasso(alpha=0.1)
regressor.fit(x_train, y_train.ravel())
print("intercept:",regressor.intercept_)
print("cofficients:",regressor.coef_)
lasso_pred=regressor.predict(x_test)
print(lasso_pred)
#MATRIX
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
lasso_Mae = mean_absolute_error(y_test, lasso_pred)
lasso_Mse = mean_squared_error(y_test, lasso_pred)
lasso_Rmse = np.sqrt(lasso_Mse)
lasso_R2 = r2_score(y_test, lasso_pred)
print("Mae:", lasso_Mae)
print("Mse:", lasso_Mse)
print("Rmse:", lasso_Rmse)
print("R2 score:", lasso_R2)
# apply Ridge Regresstion
from sklearn.linear_model import Ridge
regressor=Ridge(alpha=0.1)
regressor.fit(x_train,y_train)
print("intercept:",regressor.intercept_)
print("cofficients:",regressor.coef_)
def calc(slope, intercept, hours):
    return slope * hours + intercept

score = calc(regressor.coef_[0], regressor.intercept_,9.5)
print(score)

# Passing 9.5 in double brackets to have a 2 dimensional array
score = regressor.predict([[9.5]])
print(score) # 94.80663482
y_pred = regressor.predict(x_test)
df_preds=pd.DataFrame({'Actual': y_test.squeeze(), 'predicted': y_pred.squeeze()})
print(df_preds)
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

import numpy as np

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f'Mean absolute error: {mae:.2f}')
print(f'Mean squared error: {mse:.2f}')
print(f'Root mean squared error: {rmse:.2f}')
print(f'R2 Score: {r2:.2f}')



