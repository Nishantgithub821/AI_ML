# Day 1: NumPy Basics + Linear Algebra Foundations

import numpy as np  # NumPy for numerical & linear algebra operations

# Vector Initialization 
leta = np.array([1, 2, 3])   # initialize vector
letb = np.array([5, 6, 7])

# Basic Vector Operations 
print(leta + letb)   # vector addition
print(leta - letb)   # vector subtraction
print(leta * letb)   # element-wise multiplication
print(leta / letb)   # element-wise division

# Scalar Multiplication 
print(3 * leta)      # scalar * vector
a = 3
print(a * letb)
print(44 * letb - 33 * leta)

# Vector Length (Norm) 
print(np.linalg.norm(leta))  # magnitude of vector
print(np.linalg.norm(letb))

#  Dot Product 
a = np.array([1, 2])
b = np.array([-1, 1])
print(np.dot(a, b))           # dot product

#  Matrix Operations 
d = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

e = np.array([[0, 0, 8],
              [1, 2, 3],
              [2, 3, 4]])

print(d + e)   # matrix addition
print(d - e)   # matrix subtraction

# Matrix Inverse 
f = np.linalg.inv(e)  # inverse (only works if det ≠ 0)
print(f)

#  Linear Combination 
DAY1 DETAIL README : 
# AI / ML Interpretation of Linear Combination

# Imagine you are building a SIMPLE ML model (like linear regression)

# You have 3 features (inputs):
# v1 = user watched time (in hours)
# v2 = number of clicks
# v3 = device quality score

# Each feature contributes SOME AMOUNT to the final prediction

# AI's job:
# Find how important each feature is (weights)

# Final prediction formula:
# prediction = w1*v1 + w2*v2 + w3*v3

# This is EXACTLY a linear combination

# If data is clean and independent → exact solution exists
# If features are redundant → model breaks (singular matrix)

a = np.array([1, 2, 3])
b = np.array([2, 3, 4])
alpha = 3
beta = 5
print(alpha * a + beta * b)

# Solving Linear Combination 
v1 = np.array([1, 2, 1])
v2 = np.array([1, 1, 0])
v3 = np.array([0, 1, -1])

t = np.array([1, 6, -5])     # target vector

A = np.column_stack([v1, v2, v3])  # combine vectors as columns

solution = np.linalg.solve(A, t)   # solve A·x = t

print("Coefficients:", solution)
