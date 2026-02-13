#What is an Eigenvector
#What is an Eigenvalue
#Eigen Equation (Ax = λx)
#Finding Eigenvalues (math + NumPy)
#Finding Eigenvectors (math + NumPy)
#Numerical Precision & Rounding (practical issue)
#Basic Intuition (direction + scaling)

# New Lecture Eigen values and the Eigen vectors
#eigen values  = A-λI and eigenvectors will be  (A-λI)X = 0  and in this X there is a column of X then Y then below Z and in the matrix before we find out three eigenvalues like 15 3 0 and we put one by one all three
#values one by one in matrix and solve and find out further with multiplication method which we use in 10th class to solve 3 equations then our answer will come okey

# Imagine tum ek toy robot ke motion ko analyze kar rahe ho
# Robot ke movement ko matrix A se represent kiya hai
# Eigenvalues → robot ke motion ke "strength" ya speed along certain directions
# Eigenvectors → wo directions jisme robot move karta hai bina direction change kiye
# Hum matrix ka eigen nikalte hain → A-λI = 0 → jaise 3 equations 10th class method se solve karte hain
# Numpy se direct calculate karte hain, fir round karke clean values lete hain
# ✅ Matlab: eigenvalues + eigenvectors se humko robot ke main directions aur effect ka idea milta hai

import numpy as np
A = np.array([
                [8,-6,2],
               [-6,7,-4],
               [2,-4,3]])
eigenvalues, eigenvectors = np.linalg.eig(A)
print(eigenvalues)
print(eigenvectors)

# now here you see it cant give us clean values right so ffor that we use this thing
eigenvalues_clean = np.round(eigenvalues, 6)
print(eigenvalues_clean)
eigenvectors = np.round(eigenvectors, 1) # here we use 1 2 3 as wwe wish at which decimal point we need the value but 6 is round off safe option
print(eigenvectors)



import numpy as np

# -----------------------------
# Matrix Definition
# -----------------------------
A = np.array([
    [8, -6,  2],
    [-6, 7, -4],
    [2, -4,  3]
])

# -----------------------------
# Finding Eigenvalues (Math + NumPy)
# -----------------------------
# Math: Solve det(A - λI) = 0 for λ
# NumPy:
eigenvalues = np.linalg.eigvals(A)        # Just eigenvalues
eigenvalues = np.round(eigenvalues, 6)
print("Eigenvalues:", eigenvalues)

# -----------------------------
# Finding Eigenvectors (Math + NumPy)
# -----------------------------
# Math: Solve (A - λI)x = 0 for each λ
# NumPy:
eigenvalues, eigenvectors = np.linalg.eig(A)
eigenvectors = np.round(eigenvectors, 6)
print("\nEigenvectors (columns correspond to eigenvalues):\n", eigenvectors)

# -----------------------------
# Verify first eigenpair
# -----------------------------
i = 0
x = eigenvectors[:, i]
lam = eigenvalues[i]
print("\nCheck A @ x == λ * x ? :", np.allclose(A @ x, lam * x))


