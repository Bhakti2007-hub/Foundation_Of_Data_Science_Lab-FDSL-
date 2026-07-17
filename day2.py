import numpy as np 

#array
arr=np.array([2,3,4,5,6])
print("Array :",arr)

#zero array
arra_0 = np.zeros((2,2))
print("Zero Array :",arra_0)

#Ones Array
arr_1 = np.ones((4,2))
print("Ones Array : ", arr_1)

#filled array with same value 
arr_same= np.full((5,5),10)
print("Filled with constant value:\n" , arr_same)

#identity matrix
arr_identity = np.eye(6)
print("Identity Matrix :\n",arr_identity)

# arangement
range_arr = np.arange(0, 10, 2)   #start,stop,step
print("arange array:", range_arr)

# linspace
lin_arr = np.linspace(0, 1, 5)    #5 numbers between 0 and 1
print("linspace array:", lin_arr)

# Random arrays
rand_arr = np.random.rand(2, 3)      #uniform distribution (0, 1)
randint_arr = np.random.randint(1, 100, size=(2, 3))  #random integers
print("Random float array:\n", rand_arr)
print("Random integer array:\n", randint_arr)

s = np.array([[1, 2, 3], [4, 5, 6]])

print("Array:\n", s)
print("Shape:", s.shape)      #rows,columns
print("Dimensions:", s.ndim)  # number of axes
print("Size:",s.size)        # total elements
print("Data type:",s.dtype)  # data type of elements

# Reshaping arrays
reshaped =s.reshape(3, 2)  
print("Reshaped (3x2):\n", reshaped)

# Flattening to 1D
flat = s.flatten()
print("Flattened:", flat)

# Transpose 
print("Transpose:\n", s.T)

# Joining arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

j = np.concatenate((a, b))
print("Concatenated:",j)

v = np.vstack((a, b))   # vertical stack
h = np.hstack((a, b))   # horizontal stack
print("Vertical stack:\n",v)
print("Horizontal stack:",h)

# Sorting arrays
unsorted = np.array([5, 2, 9, 1, 7])
sorted_arr = np.sort(unsorted)
print("Original:", unsorted)
print("Sorted:", sorted_arr)

a= np.array([10, 20, 30, 40])
b= np.array([1, 2, 3, 4])

print("Addition:",a+b)
print("Subtraction:",a-b)
print("Multiplication:",a*b)
print("Division:",a/b)
print("Power:",a**3)

data = np.array([4, 8, 15, 16, 23, 42])

print("Sum:",np.sum(data))#sum
print("Mean:",np.mean(data))#mean
print("Minimum:",np.min(data))#min
print("Maximum:",np.max(data))#max
print("Standard deviation:",np.std(data))#std
print("Variance:",np.var(data))#var

# Universal functions work element-wise
nums = np.array([1, 4, 9, 16])

print("Square root:",np.sqrt(nums))#square root
print("Exponential:",np.exp(nums))#exponential
print("Natural log:",np.log(nums))#Natural Log
print("Sine:",np.sin(nums))#sine

# Matrix operations
m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])

print("Element-wise multiplication:\n",m1 * m2)
print("Matrix multiplication(dot):\n",np.dot(m1, m2))
print("Matrix multiplication(matmul):\n",np.matmul(m1, m2))

p = np.array([2, 4, 6, 8, 10])
q = np.array([1, 3, 5, 7, 9])

sum = p+q
product = p*q
print("Sum:",sum)
print("Product:",product)
print("Mean of sum:",np.mean(sum))

arr = np.array([10, 20, 30, 40, 50, 60])

print("Full array:", arr)
print("First element:", arr[0])
print("Last element:", arr[-1])
print("Elements from index 1 to 3:", arr[1:4])
print("Every second element:", arr[::2])
print("Reversed array:", arr[::-1])

matrix = np.array([[1, 2, 3],[4, 5, 6],  [7, 8, 9]])

print("Matrix:\n", matrix)
print("Element at row 1, col 2:", matrix[1, 2])
print("First row:", matrix[0, :])
print("First column:", matrix[:, 0])
print("Sub-matrix (rows 0-1, cols 1-2):\n", matrix[0:2, 1:3])