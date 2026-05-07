"""
Complete NumPy Methods Guide with Examples
==========================================
"""

import numpy as np

print("=" * 80)
print("1. ARRAY CREATION METHODS")
print("=" * 80)

# np.array() - Create array from list
arr1 = np.array([1, 2, 3, 4, 5])
print(f"np.array([1,2,3,4,5]): {arr1}")

# np.zeros() - Create array filled with zeros
arr2 = np.zeros((3, 4))
print(f"\nnp.zeros((3,4)):\n{arr2}")

# np.ones() - Create array filled with ones
arr3 = np.ones((2, 3))
print(f"\nnp.ones((2,3)):\n{arr3}")

# np.arange() - Create array with range of values
arr4 = np.arange(0, 10, 2)
print(f"\nnp.arange(0, 10, 2): {arr4}")

# np.linspace() - Create array with evenly spaced values
arr5 = np.linspace(0, 10, 5)
print(f"\nnp.linspace(0, 10, 5): {arr5}")

# np.eye() - Create identity matrix
arr6 = np.eye(3)
print(f"\nnp.eye(3):\n{arr6}")

# np.diag() - Create diagonal array
arr7 = np.diag([1, 2, 3, 4])
print(f"\nnp.diag([1,2,3,4]):\n{arr7}")

# np.full() - Create array filled with specific value
arr8 = np.full((2, 3), 7)
print(f"\nnp.full((2,3), 7):\n{arr8}")

# np.empty() - Create uninitialized array
arr9 = np.empty((2, 2))
print(f"\nnp.empty((2,2)):\n{arr9}")


print("\n" + "=" * 80)
print("2. ARRAY MANIPULATION METHODS")
print("=" * 80)

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Original array:\n{arr}\n")

# reshape() - Change shape without changing data
reshaped = arr.reshape(3, 2)
print(f"reshape(3, 2):\n{reshaped}")

# flatten() - Convert multidimensional to 1D
flattened = arr.flatten()
print(f"\nflatten(): {flattened}")

# ravel() - Similar to flatten but returns view
raveled = arr.ravel()
print(f"ravel(): {raveled}")

# transpose() / T - Transpose array
transposed = arr.transpose()
print(f"\ntranspose():\n{transposed}")

# concatenate() - Join arrays
arr_a = np.array([1, 2, 3])
arr_b = np.array([4, 5, 6])
concatenated = np.concatenate((arr_a, arr_b))
print(f"\nconcatenate([1,2,3], [4,5,6]): {concatenated}")

# stack() - Stack arrays vertically
stacked = np.stack((arr_a, arr_b))
print(f"\nstack([[1,2,3], [4,5,6]]):\n{stacked}")

# hstack() - Stack horizontally
h_stacked = np.hstack((arr_a, arr_b))
print(f"hstack([1,2,3], [4,5,6]): {h_stacked}")

# vstack() - Stack vertically
v_stacked = np.vstack((arr_a, arr_b))
print(f"\nvstack([1,2,3], [4,5,6]):\n{v_stacked}")

# split() - Split array into multiple sub-arrays
split_arrays = np.split(arr_a, 3)
print(f"\nsplit([1,2,3], 3): {split_arrays}")

# rotate() - Rotate array elements
rotated = np.roll(arr_a, 1)
print(f"roll([1,2,3], 1): {rotated}")

# sort() / argsort()
unsorted = np.array([3, 1, 4, 1, 5, 9])
sorted_arr = np.sort(unsorted)
print(f"\nsort([3,1,4,1,5,9]): {sorted_arr}")

# argsort() - Indices that would sort array
indices = np.argsort(unsorted)
print(f"argsort([3,1,4,1,5,9]): {indices}")


print("\n" + "=" * 80)
print("3. MATHEMATICAL OPERATIONS")
print("=" * 80)

arr = np.array([1, 2, 3, 4, 5])
print(f"Array: {arr}\n")

# Basic arithmetic
print(f"add (arr + 2): {np.add(arr, 2)}")
print(f"subtract (arr - 2): {np.subtract(arr, 2)}")
print(f"multiply (arr * 2): {np.multiply(arr, 2)}")
print(f"divide (arr / 2): {np.divide(arr, 2)}")
print(f"power (arr ** 2): {np.power(arr, 2)}")
print(f"mod (arr % 2): {np.mod(arr, 2)}")

# Trigonometric functions
angles = np.array([0, np.pi/2, np.pi])
print(f"\nsin(angles): {np.sin(angles)}")
print(f"cos(angles): {np.cos(angles)}")
print(f"tan(angles): {np.tan(angles)}")

# Exponential and logarithmic
arr_exp = np.array([1, 2, 3, 4])
print(f"\nexp([1,2,3,4]): {np.exp(arr_exp)}")
print(f"log([1,2,3,4]): {np.log(arr_exp)}")
print(f"log10([1,2,3,4]): {np.log10(arr_exp)}")
print(f"sqrt([1,2,3,4]): {np.sqrt(arr_exp)}")

# Absolute and sign
arr_signed = np.array([-3, -1, 0, 1, 3])
print(f"\nabs({arr_signed}): {np.abs(arr_signed)}")
print(f"sign({arr_signed}): {np.sign(arr_signed)}")

# ceil, floor, round
arr_float = np.array([1.2, 2.5, 3.7, 4.1])
print(f"\nceil({arr_float}): {np.ceil(arr_float)}")
print(f"floor({arr_float}): {np.floor(arr_float)}")
print(f"round({arr_float}): {np.round(arr_float)}")


print("\n" + "=" * 80)
print("4. STATISTICAL FUNCTIONS")
print("=" * 80)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(f"Array: {arr}\n")

print(f"sum(): {np.sum(arr)}")
print(f"mean(): {np.mean(arr)}")
print(f"median(): {np.median(arr)}")
print(f"std() (standard deviation): {np.std(arr)}")
print(f"var() (variance): {np.var(arr)}")
print(f"min(): {np.min(arr)}")
print(f"max(): {np.max(arr)}")
print(f"ptp() (peak-to-peak): {np.ptp(arr)}")

# cumsum, cumprod
print(f"\ncumsum(): {np.cumsum(arr)}")
print(f"cumprod(): {np.cumprod(arr)}")

# Percentile
print(f"\npercentile(arr, 25): {np.percentile(arr, 25)}")
print(f"percentile(arr, 50): {np.percentile(arr, 50)}")
print(f"percentile(arr, 75): {np.percentile(arr, 75)}")

# Quantile
print(f"\nquantile(arr, 0.5): {np.quantile(arr, 0.5)}")

# 2D array statistics
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(f"\n2D Array:\n{arr_2d}")
print(f"sum(axis=0): {np.sum(arr_2d, axis=0)}")
print(f"sum(axis=1): {np.sum(arr_2d, axis=1)}")
print(f"mean(axis=0): {np.mean(arr_2d, axis=0)}")


print("\n" + "=" * 80)
print("5. COMPARISON AND LOGICAL OPERATIONS")
print("=" * 80)

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([2, 2, 2, 4, 6])
print(f"Array 1: {arr1}")
print(f"Array 2: {arr2}\n")

print(f"equal (arr1 == arr2): {np.equal(arr1, arr2)}")
print(f"not_equal (arr1 != arr2): {np.not_equal(arr1, arr2)}")
print(f"greater (arr1 > arr2): {np.greater(arr1, arr2)}")
print(f"less (arr1 < arr2): {np.less(arr1, arr2)}")
print(f"greater_equal (arr1 >= arr2): {np.greater_equal(arr1, arr2)}")
print(f"less_equal (arr1 <= arr2): {np.less_equal(arr1, arr2)}")

# Logical operations
arr_bool1 = np.array([True, True, False, False])
arr_bool2 = np.array([True, False, True, False])
print(f"\nArray 1: {arr_bool1}")
print(f"Array 2: {arr_bool2}")
print(f"logical_and: {np.logical_and(arr_bool1, arr_bool2)}")
print(f"logical_or: {np.logical_or(arr_bool1, arr_bool2)}")
print(f"logical_not: {np.logical_not(arr_bool1)}")
print(f"logical_xor: {np.logical_xor(arr_bool1, arr_bool2)}")

# all, any
print(f"\nall([True, True, True]): {np.all([True, True, True])}")
print(f"all([True, False, True]): {np.all([True, False, True])}")
print(f"any([True, True, False]): {np.any([True, True, False])}")
print(f"any([False, False, False]): {np.any([False, False, False])}")


print("\n" + "=" * 80)
print("6. INDEXING AND SELECTION")
print("=" * 80)

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])
print(f"Array: {arr}\n")

print(f"arr[0]: {arr[0]}")
print(f"arr[-1]: {arr[-1]}")
print(f"arr[1:4]: {arr[1:4]}")
print(f"arr[::2]: {arr[::2]}")
print(f"arr[::-1]: {arr[::-1]}")

# Boolean indexing
mask = arr > 50
print(f"\narr > 50: {mask}")
print(f"arr[arr > 50]: {arr[arr > 50]}")

# where()
result = np.where(arr > 50, arr, 0)
print(f"\nnp.where(arr > 50, arr, 0): {result}")

# searchsorted()
sorted_arr = np.array([1, 3, 5, 7, 9])
print(f"\nArray: {sorted_arr}")
print(f"searchsorted(arr, 5): {np.searchsorted(sorted_arr, 5)}")
print(f"searchsorted(arr, 4): {np.searchsorted(sorted_arr, 4)}")

# nonzero()
arr_zeros = np.array([0, 1, 0, 2, 0, 3])
print(f"\nArray: {arr_zeros}")
print(f"nonzero(): {np.nonzero(arr_zeros)}")
print(f"nonzero()[0]: {np.nonzero(arr_zeros)[0]}")


print("\n" + "=" * 80)
print("7. LINEAR ALGEBRA")
print("=" * 80)

# Matrix multiplication
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(f"Matrix A:\n{A}")
print(f"Matrix B:\n{B}\n")

print(f"dot(A, B):\n{np.dot(A, B)}")
print(f"\nmatmul(A, B):\n{np.matmul(A, B)}")

# Transpose
print(f"\ntranspose(A):\n{np.transpose(A)}")

# Determinant
det = np.linalg.det(A)
print(f"\nlinalg.det(A): {det}")

# Inverse
inv = np.linalg.inv(A)
print(f"linalg.inv(A):\n{inv}")

# Eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)
print(f"\neigenvalues: {eigenvalues}")
print(f"eigenvectors:\n{eigenvectors}")

# Trace (sum of diagonal)
trace = np.trace(A)
print(f"\ntrace(A): {trace}")

# Rank
rank = np.linalg.matrix_rank(A)
print(f"matrix_rank(A): {rank}")

# Solve linear system: Ax = b
b = np.array([5, 11])
x = np.linalg.solve(A, b)
print(f"\nSolving Ax = b where b = {b}")
print(f"Solution x: {x}")


print("\n" + "=" * 80)
print("8. RANDOM NUMBER GENERATION")
print("=" * 80)

# Set seed for reproducibility
np.random.seed(42)

print(f"rand(5): {np.random.rand(5)}")
print(f"randn(5): {np.random.randn(5)}")
print(f"randint(0, 10, 5): {np.random.randint(0, 10, 5)}")
print(f"choice([1,2,3,4,5], 3): {np.random.choice([1,2,3,4,5], 3)}")
print(f"shuffle: ", end="")
arr_shuffle = np.array([1, 2, 3, 4, 5])
np.random.shuffle(arr_shuffle)
print(arr_shuffle)

# Distributions
print(f"\nnormal(loc=0, scale=1, size=5): {np.random.normal(0, 1, 5)}")
print(f"uniform(0, 1, 5): {np.random.uniform(0, 1, 5)}")
print(f"binomial(n=10, p=0.5, size=5): {np.random.binomial(10, 0.5, 5)}")
print(f"poisson(lam=3, size=5): {np.random.poisson(3, 5)}")


print("\n" + "=" * 80)
print("9. USEFUL UTILITY FUNCTIONS")
print("=" * 80)

# Shape and size
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Array:\n{arr}\n")
print(f"shape: {arr.shape}")
print(f"size: {arr.size}")
print(f"ndim: {arr.ndim}")
print(f"dtype: {arr.dtype}")

# unique()
arr_dup = np.array([1, 1, 2, 2, 3, 3, 4])
print(f"\nArray with duplicates: {arr_dup}")
print(f"unique(): {np.unique(arr_dup)}")

# bincount()
arr_counts = np.array([0, 1, 1, 0, 2, 2, 2])
print(f"\nArray: {arr_counts}")
print(f"bincount(): {np.bincount(arr_counts)}")

# repeat() and tile()
arr_repeat = np.array([1, 2, 3])
print(f"\nArray: {arr_repeat}")
print(f"repeat(2): {np.repeat(arr_repeat, 2)}")
print(f"tile(2): {np.tile(arr_repeat, 2)}")

# argmax() and argmin()
arr_extremes = np.array([1, 5, 3, 9, 2])
print(f"\nArray: {arr_extremes}")
print(f"argmax(): {np.argmax(arr_extremes)}")
print(f"argmin(): {np.argmin(arr_extremes)}")

# clip()
arr_clip = np.array([1, 5, 10, 15, 20])
print(f"\nArray: {arr_clip}")
print(f"clip(5, 15): {np.clip(arr_clip, 5, 15)}")

# append(), insert(), delete()
print(f"\nappend([1,2,3], 4): {np.append([1, 2, 3], 4)}")
print(f"insert([1,2,3], 1, 99): {np.insert([1, 2, 3], 1, 99)}")
print(f"delete([1,2,3,4], 2): {np.delete([1, 2, 3, 4], 2)}")

# diff() - Calculate differences
arr_diff = np.array([1, 3, 6, 10])
print(f"\nArray: {arr_diff}")
print(f"diff(): {np.diff(arr_diff)}")

# gradient() - Calculate gradient
arr_grad = np.array([1, 2, 4, 7])
print(f"\nArray: {arr_grad}")
print(f"gradient(): {np.gradient(arr_grad)}")


print("\n" + "=" * 80)
print("10. ADVANCED FUNCTIONS")
print("=" * 80)

# meshgrid()
x = np.array([1, 2, 3])
y = np.array([4, 5])
X, Y = np.meshgrid(x, y)
print(f"meshgrid([1,2,3], [4,5]):")
print(f"X:\n{X}\nY:\n{Y}")

# histogram()
arr_hist = np.array([1, 1, 2, 2, 2, 3, 3, 3, 3, 4])
counts, bins = np.histogram(arr_hist, bins=4)
print(f"\nhistogram([1,1,2,2,2,3,3,3,3,4], bins=4):")
print(f"counts: {counts}")
print(f"bins: {bins}")

# polyfit() and poly1d() - Polynomial fitting
x_data = np.array([1, 2, 3, 4, 5])
y_data = np.array([2, 4, 5, 4, 5])
coefficients = np.polyfit(x_data, y_data, 2)
poly = np.poly1d(coefficients)
print(f"\nPolyfit (degree 2) coefficients: {coefficients}")
print(f"Poly1d evaluation at x=3: {poly(3)}")

# convolve() - Convolution
a = np.array([1, 2, 3])
b = np.array([0, 1, 0.5])
print(f"\nconvolve([1,2,3], [0,1,0.5]): {np.convolve(a, b)}")

print("\n" + "=" * 80)
print("GUIDE COMPLETE!")
print("=" * 80)
