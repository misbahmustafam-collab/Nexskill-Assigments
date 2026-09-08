import numpy as np

data = np.genfromtxt(
    "FastFoodRestaurants.csv",
    delimiter=",",
    skip_header=1,
    usecols=(0,1,2),
    dtype=str,
    encoding="utf-8",
    invalid_raise=False
)

print(data)

#FastFoodRestaurants.csv statistics operations
# extract price column (assumed to be the 3rd column) and convert to float
prices = data[:, 2]
# remove common non-numeric characters like $ and commas
clean = np.char.replace(prices, '$', '')
clean = np.char.replace(clean, ',', '')

# convert cleaned price strings to float, set non-numeric to np.nan
clean = np.where(clean == '', 'nan', clean)
try:
    price_num = clean.astype(float)
except ValueError:
    # fallback: coerce with vectorized conversion
    price_num = np.array([float(x) if x not in ('', 'nan') else np.nan for x in clean], dtype=float)

print("FastFood price mean:", np.nanmean(price_num))
print("FastFoodRestaurants price average:", np.nanmean(price_num))
print("FastFoodRestaurants price min:", np.nanmin(price_num))
print("FastFoodRestaurants price max:", np.nanmax(price_num))

#FastFoodRestaurants.csv maths operations (skip invalids)
print("FastFoodRestaurants price square:", np.square(price_num))
print("FastFoodRestaurants price sqrt:", np.sqrt(price_num))
print("FastFoodRestaurants price pows:", np.power(price_num, price_num))
print("FastFoodRestaurants price abs:", np.abs(price_num))


# perform basic arithmetic operations on first two columns if numeric
coords = np.where(data[:, 0:2] == '', 'nan', data[:, 0:2])
try:
    coords = coords.astype(float)
    longitude = coords[:, 0]
    latitude = coords[:, 1]
    addition = longitude + latitude
    print("Sum of first two numeric columns:", addition)
except ValueError:
    print("Could not convert first two columns to float for addition.")
