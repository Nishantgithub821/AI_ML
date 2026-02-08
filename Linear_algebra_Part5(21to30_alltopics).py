Here it is the code of row reductino form in this what we do we simply make 
#the diagonal elements one and another are zero by using eminitating theorem  
#which we also do in 11th and 12th class using by row or bc column 

#Topic 19 &  Topc 20 Column space and null space and also we say another one is nulity 
#Topic 19:
import numpy as np
from sympy import Matrix

# Matrix (cart / features example)
A = Matrix([
    [1, 2],
    [2, 4],
    [3, 6]
])

print("Matrix A:")
print(A)

# -----------------------------
# COLUMN SPACE
# -----------------------------
col_space = A.columnspace()
print("\nColumn Space:")
for v in col_space:
    print(v)



import numpy as np
from sympy import Matrix

# Matrix (cart / features example)
A = Matrix([
    [1, 2],
    [2, 4],
    [3, 6]
])

print("Matrix A:")
print(A)

# -----------------------------
# COLUMN SPACE
# -----------------------------
col_space = A.columnspace()
print("\nColumn Space:",col_space)

#Null space 
null_space = A.nullspace()
print("\nNull Space:",null_space)
# Rank =  A.rank()
rank = A.rank()
rank
# and Nulity is nothing if we have a matrix we know how many columns in it and 
# and we know the rank so ther is a formual to find out the nulity that is 
#ank + Nullity = number of columns or Nulity = Columns - rank (simple )

#Topic 21 -29 all topics basic idea after completing these almost 30 topics 
#we go on practice mode and we solve all the topics code logic ex real life examples 
# on notebook so fatafat ise khatam kerte hai taki practice ker sakte ok 

import numpy as np

print("="*60)
print("TOPIC 21 → 29 : LINEAR ALGEBRA CORE (ML VIEW)")
print("="*60)

# =====================================================
# 21. ORTHOGONALITY (Independent features)
# =====================================================
print("\n21. ORTHOGONALITY")

v1 = np.array([1, 0])   # fruit feature
v2 = np.array([0, 1])   # veg feature

dot_ortho = np.dot(v1, v2)
print("Dot product:", dot_ortho)
# dot = 0 → bilkul independent (jaise fruits & roll number)

# =====================================================
# 22. DOT PRODUCT (Similarity)
# =====================================================
print("\n22. DOT PRODUCT (Similarity)")

user1 = np.array([1, 2, 3])   # movie likes
user2 = np.array([2, 4, 6])

similarity = np.dot(user1, user2)
print("Similarity score:", similarity)
# bada dot → zyada similar taste

# =====================================================
# 23. NORM (Vector strength / length)
# =====================================================
print("\n23. NORM (Strength)")

cart = np.array([3, 4])
strength = np.linalg.norm(cart)
print("Cart strength:", strength)
# kitna heavy cart hai (ML me regularization)

# =====================================================
# 24. DISTANCE METRIC (Closeness)
# =====================================================
print("\n24. DISTANCE (Closeness)")

shop1 = np.array([1, 2])
shop2 = np.array([4, 6])

distance = np.linalg.norm(shop1 - shop2)
print("Distance:", distance)
# clustering, KNN me use hota hai

# =====================================================
# 25. PROJECTION (Shadow)
# =====================================================
print("\n25. PROJECTION")

data = np.array([3, 4])
important_direction = np.array([1, 0])

projection = (np.dot(data, important_direction) /
              np.dot(important_direction, important_direction)) * important_direction

print("Projected data:", projection)
# PCA ka base idea

# =====================================================
# 26. LEAST SQUARES (Best fit)
# =====================================================
print("\n26. LEAST SQUARES (Best fit)")

A = np.array([[1, 1],
              [1, 2],
              [1, 3]])
b = np.array([2, 2.5, 3.5])

solution, _, _, _ = np.linalg.lstsq(A, b, rcond=None)
print("Best fit solution:", solution)
# exact match nahi → best possible line

# =====================================================
# 27. EIGENVALUES (Importance)
# 28. EIGENVECTORS (Direction)
# =====================================================
print("\n27 & 28. EIGENVALUES & EIGENVECTORS")

M = np.array([[2, 0],
              [0, 1]])

eigen_values, eigen_vectors = np.linalg.eig(M)

print("Eigenvalues:", eigen_values)
print("Eigenvectors:\n", eigen_vectors)
# PCA me sabse bada eigenvalue = most important direction

# =====================================================
# 29. DIAGONALIZATION (Simplification)
# =====================================================
print("\n29. DIAGONALIZATION")

P = eigen_vectors
D = np.diag(eigen_values)
P_inv = np.linalg.inv(P)

reconstructed_M = P @ D @ P_inv
print("Reconstructed Matrix:\n", reconstructed_M)
# complex matrix → simple form

print("\n✅ TOPIC 21 → 29 COMPLETED")
print("="*60)
