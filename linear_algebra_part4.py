

# NOW LECTURE 13 IS STARTED AND HERE IS ALL THE THINGS WHICH WE NEED TO KNOW TO MOVE ON NEXT TOPIC THAT IS 14TH RIGHT 

import numpy as np

print("SPECIAL MATRICES - Simple Version")
print("="*50)

# ============================================================
# 1. IDENTITY MATRIX
# ============================================================
print("\n1. IDENTITY MATRIX")
print("-"*50)

I = np.eye(3)
print(I)
print("Use: A @ I = A (kuch change nahi hota)")

# ============================================================
# 2. ZERO MATRIX
# ============================================================
print("\n2. ZERO MATRIX")
print("-"*50)

Z = np.zeros((3, 3))
print(Z)
print("Use: Starting point, padding")

# ============================================================
# 3. ONES MATRIX
# ============================================================
print("\n3. ONES MATRIX")
print("-"*50)

O = np.ones((3, 3))
print(O)
print("Use: Initialization")

# ============================================================
# 4. DIAGONAL MATRIX
# ============================================================
print("\n4. DIAGONAL MATRIX")
print("-"*50)

D = np.diag([1, 2, 3])
print(D)
print("Use: Scaling karne ke liye")

# ============================================================
# 5. SYMMETRIC MATRIX
# ============================================================
print("\n5. SYMMETRIC MATRIX")
print("-"*50)

S = np.array([[1, 2, 3],
              [2, 4, 5],
              [3, 5, 6]])
print(S)
print("Property: S = S.T (transpose same hai)")

# ============================================================
# 6. UPPER TRIANGULAR
# ============================================================
print("\n6. UPPER TRIANGULAR MATRIX")
print("-"*50)

U = np.array([[1, 2, 3],
              [0, 4, 5],
              [0, 0, 6]])
print(U)
print("Upar triangle non-zero, neeche zero")

# ============================================================
# 7. LOWER TRIANGULAR
# ============================================================
print("\n7. LOWER TRIANGULAR MATRIX")
print("-"*50)

L = np.array([[1, 0, 0],
              [2, 3, 0],
              [4, 5, 6]])
print(L)
print("Neeche triangle non-zero, upar zero")

# ============================================================
# 8. RANDOM MATRIX
# ============================================================
print("\n8. RANDOM MATRIX")
print("-"*50)

R = np.random.rand(3, 3)
print(R)
print("Use: Random initialization")

# ============================================================
# SUMMARY
# ============================================================
print("\n" + "="*50)
print("SUMMARY")
print("="*50)
print("Identity     : np.eye(n)")
print("Zero         : np.zeros((m,n))")
print("Ones         : np.ones((m,n))")
print("Diagonal     : np.diag([...])")
print("Random       : np.random.rand(m,n)")

print("\nTopic 13 Done!")

# TOPIC 14TH Matrix Rank 
import numpy as np

print("MATRIX RANK - Simple Version")
print("="*50)

# ============================================================
# 1. FULL RANK MATRIX
# ============================================================
print("\n1. FULL RANK MATRIX")
print("-"*50)

A = np.array([[1, 2],
              [3, 4]])
print(A)
print("Rank:", np.linalg.matrix_rank(A))
print("Meaning: sari rows/columns useful hain")

# ============================================================
# 2. RANK DEFICIENT MATRIX
# ============================================================
print("\n2. RANK DEFICIENT MATRIX")
print("-"*50)

B = np.array([[1, 2],
              [2, 4]])
print(B)
print("Rank:", np.linalg.matrix_rank(B))
print("Meaning: duplicate info, ek row dusri ki copy")

# ============================================================
# 3. ZERO MATRIX RANK
# ============================================================
print("\n3. ZERO MATRIX RANK")
print("-"*50)

Z = np.zeros((3, 3))
print(Z)
print("Rank:", np.linalg.matrix_rank(Z))
print("Meaning: koi info nahi")

# ============================================================
# 4. RECTANGULAR MATRIX RANK
# ============================================================
print("\n4. RECTANGULAR MATRIX RANK")
print("-"*50)

C = np.array([[1, 2, 3],
              [4, 5, 6]])
print(C)
print("Rank:", np.linalg.matrix_rank(C))
print("Rule: rank <= min(rows, columns)")

# ============================================================
# 5. PRACTICAL ML VIEW
# ============================================================
print("\n5. PRACTICAL ML VIEW")
print("-"*50)
print("Rank = kitni independent features hain")
print("Low rank = redundant features")

# ============================================================
# SUMMARY
# ============================================================
print("\n" + "="*50)
print("SUMMARY")
print("="*50)
print("rank(A) = np.linalg.matrix_rank(A)")
print("Full rank      → no redundancy")
print("Low rank       → duplicate info")
print("Zero rank      → no information")

print("\nTopic 14 Done!")

#Topic 15th 16th and 17th 
import numpy as np

print("TOPIC 15–17 : DetermINANT, INVERSE, Ax=b (Simple Version)")
print("="*60)

# ============================================================
# 15. DETERMINANT
# ============================================================
print("\n15. DETERMINANT (Invertibility Check)")
print("-"*60)

A = np.array([[2, 1],
              [4, 2]])

det_A = np.linalg.det(A)
print("Matrix A:\n", A)
print("Determinant:", det_A)

if det_A == 0:
    print("❌ det = 0 → Inverse possible nahi")
else:
    print("✅ det ≠ 0 → Inverse possible")

print("Baby logic: det batata hai info duplicate hai ya nahi")

# ============================================================
# 16. INVERSE MATRIX
# ============================================================
print("\n16. INVERSE MATRIX (Equation Solve Tool)")
print("-"*60)

B = np.array([[1, 2],
              [3, 4]])

det_B = np.linalg.det(B)

print("Matrix B:\n", B)
print("Determinant:", det_B)

if det_B != 0:
    B_inv = np.linalg.inv(B)
    print("Inverse of B:\n", B_inv)
    print("Check: B @ B_inv = Identity\n", B @ B_inv)
else:
    print("Inverse exist nahi karta")

print("Baby logic: Inverse = undo button of matrix")

# ============================================================
# 17. LINEAR EQUATIONS (Ax = b)
# ============================================================
print("\n17. LINEAR EQUATIONS (Ax = b)")
print("-"*60)

A = np.array([[2, 1],
              [1, 3]])

b = np.array([5, 6])

print("Matrix A:\n", A)
print("Target b:", b)

# Solve Ax = b
x = np.linalg.solve(A, b)
print("Solution x:", x)

print("Check: A @ x =", A @ x)

print("Baby logic: A = rules, x = unknowns, b = result")

# ============================================================
# SUMMARY
# ============================================================
print("\n" + "="*60)
print("SUMMARY (EXAM + ML READY)")
print("="*60)

print("15. Determinant → inverse possible hai ya nahi")
print("16. Inverse     → equations ko ulta solve karna")
print("17. Ax = b      → real problems ka math model")

print("\nNow you are READY for Topic 18: Row Reduction 🔥")

