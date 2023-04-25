import numpy as np 
from numpy import pi 

# 1. Create a numpy array
x = [1,2,3]
x_np = np.array(x) 
x_np = np.array([1,2,3])
#print(x_np)

# 2. Create a numpy array with zeros
x_np = np.zeros(3)
#print(x_np)

# 3. Create a numpy array with ones
x_np = np.ones(3)
#print(x_np)

# 4. Create a numpy array with a range
a = np.arange(15) 
#print(a)

# 4.1. Create a numpy array with a range from 2 to 10
a = np.arange(2, 11)
#print(a)

# 4.2. Create a numpy array with a range from 2 to 10 with step 2
a = np.arange(2, 11, 2)
print(a.dtype)
#print(a)

# 5. Random numbers
x_np = np.random.rand(3)
#print(x_np)
print(a.dtype)

# 6. Create a numpy matrix
x_np = np.array([[1,2,3], [4,5,6]])
print(x_np)

# 7. Create a numpy matrix with zeros
x_np = np.zeros((3,3))
print(x_np)

# 8. Create a numpy matrix with ones
x_np = np.ones((3,3))
print(x_np)

# 9.Linspace 
x = np.linspace(0, 10, 100)  # 100 linearly spaced numbers

# 10. Sin
f = np.sin(x) 
print(f)

# 11. Reshape
a = np.arange(6)
print(a.reshape(3,2))

########################
# BASIC OPERATIONS    # 
########################

# 1. Sum
a = np.array([1,2,3])
b = np.array([4,5,6])
print(a+b)
print(np.add(a,b))

# 2. Subtraction
print(a-b)
print(np.subtract(a,b))

# 3. Multiplication
print(a*b)
print(np.multiply(a,b))

# 4. Division
print(a/b)
print(np.divide(a,b))

# 5. Exponentiation
print(a**2)         # a^2
print(np.exp(a))    # e**a

# 5. Matrix operations 
A = np.array([[1, 1],
              [0, 1]])
B = np.array([[2, 0],
              [3, 4]])
print(A*B)      # Elementwise product

print(A@B)      # Matrix product

print(A.dot(B)) # Another matrix product

# 6. Transpose
print(A.T)

# 7. Universal functions in matrixes and arrays

# 7.1. Sum
a = np.arange(6).reshape(2,3)
print(a)
print(a.sum())

# 7.2. Min
print(a.min())

# 7.3. Max
print(a.max())

# 7.4. Min in each column
print(a.min(axis=0)[1]) # Get the second column minimum element

# 7.5. Min in a row
print(">>> a.min(axis=1)[0]: ") 
print(a.min(axis=1)[0]) # Get the first row minimum element

###################################
# Indexing, slicing and iterating #
###################################

a = np.arange(10) 
print(">>> a[2]")
print(a[2])
print(">>> a[2:5]")
print(a[2:5])
print(">>> a[::2]")
a[1::2] = 666   # All the odd elements are 666
print(a)

print(">>> a[::-1]")
print(a[::-1]) # Reverse the array
# [1,2,3,4,5,6,7,8,9,10] -> [10,9,8,7,6,5,4,3,2,1]
print(">>> a[::2]")
print(a[::2])  # Get the even elements
print(">>> a[1::2]")
print(a[1::2]) # Get the odd elements

# 2. Iterate over an array
for i in a: 
    print(i)

# 3. Iterate over a matrix
b = np.arange(12).reshape(3,4)
print(b)
# 3.1. Iterate over the rows
for i in b: 
    # 3.2. Iterate over the columns
    for j in i:
        print(j)

    
# 4. Flat => Convert the matrix to an array
b = np.arange(12).reshape(3,4)
print(b)
print(np.array(b.flat)) # Convert the matrix to an array
# Iterate over the matrix as an array 
for i in b.flat:
    print(i)

##################################
# SHAPE MANIPULATION            #
##################################

a = np.arange(0,10)
a = a.reshape(2,5)  # Reshape the array
print(a.ravel())    # Convert the matrix to an array
# The same thing of np.array(a.flat)
print(a.shape)
a.resize((5,2))     # Resize the array, inplace. 
# print(a.resize((5,2))) # This is wrong
print(a)

##################################
# STACKING                       #
##################################

a = np.floor(10*np.random.random((2,2)))
print("a:", a)
b = np.floor(10*np.random.random((2,2)))
print("b", b)
print("Add b to a.")
print(np.vstack((a,b)))    # Vertical stack
# Append b to a 
# in normal python : a + b
print("Add elements to each line of a.")
print(np.hstack((a,b)))    # Horizontal stack

##################################
# SPLITTING                      #
##################################

a = np.arange(0,10)
print(np.hsplit(a, 5))  # Split a into 5

b = np.arange(0,20).reshape(2,10)
# [[0,1,2,3,4,5,6,7,8,9], 
# [10,11,12,13,14,15,16,17,18,19]]

# [[0,1],[10,11]]
# [[2,3],[12,13]]

print(np.hsplit(b, 5))  # Split a into 5

c = np.arange(0,20).reshape(4,5)

print(np.vsplit(c, 2)) # Split a into 5
