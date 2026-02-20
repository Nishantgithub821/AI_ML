#Next Topic is Eigen Decomposition
#det(A-λI) = 0 first solve this then in second step solve this (A-λ1​I)x = 0
# Matlab:
# 1️⃣ Eigenvalues alag-alag ya repeated ho sakte hain, lekin
# 2️⃣ Har eigenvalue ke liye **enough independent eigenvectors** hone chahiye
# Agar ye condition satisfy hai → matrix ka **eigen decomposition possible**
# Agar eigenvectors unique / independent nahi hain → decomposition impossible
# ✅ Matlab: eigen decomposition = eigenvalues + enough independent eigenvectors ka combination

# Main thing agar repetead bhi ho eigen values but eigen vectors independent hai enough like 2 ya 3 or vo dono alag alag hai to bhi possible hai agar same hai nahi okey

# Best Example:
# Socho tumhare robot ka dance plan hai
# Robot ke paas 2 moves (matrix 2x2)
# Eigenvalues = [2, 2] → same speed in both moves
# Lekin moves unique nahi hain (sirf 1 independent move) → missing move
# Matlab: hum robot ka dance step by step break nahi kar sakte (no eigen decomposition)
# ✅ Robot confuse ho jayega, exact simple steps me todna impossible

import numpy as np
A = np.array([[4,1],
              [1,3]])
print(A) # first step is to print the matrix

# second step is to find out the eiganvalues and eigenvectors
eiganval ,eigenvac  = np.linalg.eig(A)
print(eiganval)
print(eigenvac)

#third step is  to find out diagonnals okey
D = np.diag(eiganval) # it convert the values into matrix for better computation okey
print(D)

#4rth step is to seperate the eigenvectors
ev = eigenvac
print(ev)

#5th step is to if the  symmetric: A = V @ D @ V. ≈ A → decomposition successful
#then our eigen decoompsition possble right
A_reconstructed = ev @ D @ ev.T
print(np.round(A_reconstructed , 6))

#LOOK FIRST WE DO EIGEN DECOMPOSITION WITH HELP OF PEN AND PAPER BUT THERE ARE SOME THINGS WHICH YOU SHOULD KEEP IN MIND 


#Real eigenvalues ❌ guaranteed nahi

#Orthogonal eigenvectors ❌ guaranteed nahi

#Complex values aa sakti hain

#NOW OUTPUT AND ITS EXPLANATION 
# thats the final output first we print the orignal matrix 
#then we find out rigen values ,vectors then seee what is d here 
# then reconstructed the things which we seprate at the starting liike eigen vectors , D ,and the Transpose of eigen vectors 
#then finally if the same matrix is come in the results that means our eigen decomposition is possible 

[[4 1]
 [1 3]]
[4.61803399 2.38196601]
[[ 0.85065081 -0.52573111]
 [ 0.52573111  0.85065081]]
[[4.61803399 0.        ]
 [0.         2.38196601]]
[[ 0.85065081 -0.52573111]
 [ 0.52573111  0.85065081]]
[[4. 1.]
 # Means this is the best case which we called SD right which perform on symmetric matrix only and further in sd we also do with 
 # good example and see again this code 

 #SD

 #Spectral decomposition
"""
- Spectral Decomposition = special case of eigen decomposition
- Sirf **symmetric matrix** ke liye possible
- Idea: matrix ko tod do **main directions (eigenvectors) + magnitude (eigenvalues)** me
- Formula: A = V D V.T  (V = orthogonal eigenvectors, D = diagonal eigenvalues)
- ✅ Matlab: har direction ka effect clearly samajh me aa jata hai


- Socho robot ka symmetric dance floor hai
- Robot ka motion ko tod do 3 main moves me
- Har move = eigenvector (direction)
- Har move ki speed = eigenvalue
- Sab moves milke original dance plan = matrix A
- ✅ Easy to analyze + fully controlled
"""
import numpy as np

# -----------------------------
# Spectral Decomposition (ONLY for symmetric matrix)
# -----------------------------

# Step 1: Symmetric matrix
A = np.array([[4, 1],
              [1, 3]])
print("Matrix A:\n", A)

# Step 2: Eigenvalues & Eigenvectors
eigvals, eigvecs = np.linalg.eig(A)
print("\nEigenvalues:", eigvals)
print("\nEigenvectors:\n", eigvecs)

# Step 3: Diagonal matrix D (from eigenvalues)
D = np.diag(eigvals)
print("\nDiagonal matrix D:\n", D)

# Step 4: Reconstruct A using spectral decomposition
# A = V D V^T
A_reconstructed = eigvecs @ D @ eigvecs.T
print("\nReconstructed A:\n", np.round(A_reconstructed, 6))

# Step 5: Check if spectral decomposition is successful
if np.allclose(A, A_reconstructed):
    print("\nYES → Spectral decomposition possible")
else:
    print("\nNO → Spectral decomposition not possible")

#ED (Eigen Decomposition): square matrix ko tod-kar likhte hain
#A = V · D · V⁻¹ (jab possible ho)

#SD (Spectral Decomposition): symmetric matrix ke liye special case
#A = V · D · Vᵀ

"""
Special note is very important A = V D V^T This formula if we visualize this right
V^T is basically rotate eigen vectors to its standard basis
So A is linear transforamtion and V rotate back to its standard basis
D or we say here is lemda is our scaling with x and y axis and

"""
#Final output 

Matrix A:
 [[4 1]
 [1 3]]

Eigenvalues: [4.61803399 2.38196601]

Eigenvectors:
 [[ 0.85065081 -0.52573111]
 [ 0.52573111  0.85065081]]

Diagonal matrix D:
 [[4.61803399 0.        ]
 [0.         2.38196601]]

Reconstructed A:
 [[4. 1.]
 [1. 3.]]

YES → Spectral decomposition possible
 \nSpecial note is very important A = V D V^T This formula if we visualize this right \nSo A is linear transforamtion and V is a rotated by its eigen vectors \nD or we say here is lemda is our scaling with x and y axis and \nV^T is basically rotate eigen vectors to its standard basis \n


