import numpy as np

# Load CSV with header; use names=True to get a structured array
data = np.genfromtxt("Real_Estate_Sales_2001-2022_GL-Short.csv", delimiter=",", skip_header=1, usecols=(0,1,2))
print(data)

price = data[:, 2]

#Real_Estate_Sales_2001-2022_GL-Short.csv
print("Real_Estate price mean:", np.mean(price))
print("Real_Estate price average:",np.average(price))
print("Real_Estate price std:",np.std(price))
print("Real_Estate price mod:",np.median(price))
print("Real_Estate price percentile-25:",np.percentile(price,25))
print("Real_Estate price min:",np.min(price))
print("Real_Estate price max:",np.max(price))

#Real_Estate_Sales_2001-2022_GL-Short.csv maths operations
print("Real_Estate price square:",np.square(price))
print("Real_Estate price sqrt:", np.sqrt(price))
print("Real_Estate_Sales pows:", np.power(price,price))

#perform basic arithmetic operations
long = data[:, 0]
lat = data[:, 1]
addition = long + lat
print("Real_Estate longitude + latitude:", addition)

subtraction=long-lat
print("Real_Estate long-lat-subtraction:",subtraction)

multiplication=long*lat
print("Real_Estate long-lat-multiplication:",multiplication)

division=long/long
print("Real_Estate long-lat-division:",division)

# trigonometric function
pricepie = price / np.pi + 1
# calculate sine cosine tangent
sine_values = np.sin(pricepie)
cosine_values = np.cos(pricepie)
tangent_values = np.tan(pricepie)

print("Real_Estate price-pie-div-sine values:", sine_values)
print("Real_Estate price-pie-div-cosine values:", cosine_values)
print("Real_Estate price-pie-div-tangent values:", tangent_values)


#calculate the natural logarthim and base 10 logarthim
log_array=np.log(pricepie)
log10_array=np.log10(pricepie)

print("Real_Estate price-div-pie-Natural logarthim:",log_array)
print("Real_Estate price-div-pie-Natural logarthim:",log10_array)

# Example:Hyperbolic sine
#calculate the hyperbolic sine of each element
sinh_values=np.sinh(pricepie)
print("Real_Estate price-div-hyperbolic sinh values:",sinh_values)

#Example : Hyperbolic cosine
#calculate the hyperbolic cosine of each element
cosnh_values=np.cosh(pricepie)
print("Real_Estate price-div-hyperbolic cosnh values:",cosnh_values)


#Example : Hyperbolic tangent
#calculate the hyperbolic tangent of each element
tanh_values=np.tanh(pricepie)
print("Real_Estate price-div-hyperbolic tanh values:",tanh_values)

#inverse Hyperbolic tangent
#calculate the inverse hyerbolic cosine
tanh_values=np.tanh(pricepie)
print("Real_Estate price-div-inverse hyperbolic tangent value:", tangent_values)


#inverse hyperbolic sine
#calculate the inverse hyperbolic sine
asinh_values=np.arcsinh(pricepie)
print("Real_Estate price-div-inverse hyperbolic sine values: ", sine_values)


#inverse hyperbolic cosine
#calculate the inverse cosine
acosh_values=np.arccosh(pricepie)
print("Real_Estate price-div-inverse hyperbolic cosine values:",cosine_values)


#2dimentional array
D2longlat=np.array([long,lat])


print("Real_Estate long plus lat-2dimentional array -",D2longlat)
print("Real_Estate long plus lat-2dimentional array-dimension",D2longlat.ndin)

#output 2
#return total number of elements
print("Real_Estate long plus lat-2dimentional array-total number of elements:",D2longlat.size)

#output 6
#return a tuple that gives the size of array in each dimention
print("Real_Estate long plus lat-2 dimentional array - gives size of array in each dimension:",D2longlat.shape)

#splicing array
D2longlatslice=D2longlat[0:1:1,1:3:1]
print("Real_Estate long plus lat-2 dimentional array - spciling array-D2longlat[:1,:5]",D2longlat)


#indexing array
D2longlatsliceItemOnly=D2longlatslice[0,1]
print("Real_Estate long plus lat-2 dimentional array-index array-D2longlatslice[1,5]",D2longlatsliceItemOnly)


#you should use built in function nidter, if you don't need to have the indexes values
for elem in np.nditer(D2longlat):print(elem)

