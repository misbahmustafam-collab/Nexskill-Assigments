import numpy as np

data = np.genfromtxt("startup_growth_investment_data.csv", delimiter=",", skip_header=1)
print(data)


#startup_growth_investment_data.csv - statistics operations
price = data[:, 0]
print("startup_growth price mean:", np.mean(price))
print("startup_growth price average:",np.average(price))
print("startup_growth price std:",np.std(price))
print("startup_growth price mod:",np.median(price))
print("startup_growth price perentile-10:",np.percentile(price,10))
print("startup_growth price max:",np.max(price))
print("startup_growth price min:",np.min(price))

#startup_growth_investment_data.csv maths operations
print("startup_growth price square:",np.square(price))
print("startup_growth price sqrt:",np.sqrt(price))
print("startup_growth price pows:",np.power(price,price))
print("startup_growth price abs:",np.abs(price))

#perform basic arithmetic operations
addition = price + price
print("startup_growth price addition:", addition)


#calculate sine cosine and tangent
sine_value=np.sin(price)
cosine_value=np.cos(price)
tangent_value=np.tan(price)


print("startup_growth price-div-sine value:",sine_value)
print("startup_growth price -div-cosine value:",cosine_value)
print("startup_growth price -div-tangent value:",tangent_value)



#calculate the natural logarithm and base-10 logarithm
log_array = np.log(price)
log10_array = np.log10(price)
print("startup_growth price natural log:", log_array)
print("startup_growth price base-10 log:", log10_array)

#Example Hyperbolic sine
#calculate the hyperbolic sine of each element
sinh_value=np.sinh(price)

print("startup_growth price-div-Hyperbolic sinh_value:",sinh_value)


#Example Hyperbolic cosine
#calculate the hyperbolic cosine of each element
cosinh_value=np.cosh(price)
print("startup_growth price-div-Hyperbolic cosinh_value:",cosinh_value)


#Example Hyperbolic tangent
#calculate the hyperbolic tangent of each element
tanh_value=np.tanh(price)
print("startup_growth price-div-Hyperbolic tanh_value:",tanh_value)

#Example inverse hyperbolic sine
#calculate the inverse hyperbolic sine of each element
asinh_values=np.arcsinh(price)
print("startup_growth price-div-inverse Hyperbolic sine value:",asinh_values)


#Example inverse Hyperbolic cosine
#calculate the inverse hyperbolic cosine of each element
acosh_values=np.arccosh(price)
print("startup_growth price-div-inverse Hyperbolic cosine value:",acosh_values)



#2 Dimentional array
# create 2D array of longitude and latitude if available in data
# assume columns 1 and 2 are long and lat; fall back to empty arrays if not present
if data.shape[1] >= 3:
	long = data[:, 1]
	lat = data[:, 2]
else:
	long = np.array([])
	lat = np.array([])

D2longlat = np.array([long, lat])
print("D2 long/lat:", D2longlat)

#you should use the builtin function nidter,if uou don't need to have the indexes value
for index, elem in np.ndenumerate(D2longlat):
	print(index, elem)
	
    
