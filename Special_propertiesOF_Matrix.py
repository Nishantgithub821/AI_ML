#Next lecture special properties of the matrix
# Kya hota hai? (Baby language)
# Quadratic form bas ek special calculation hoti hai jisme
# ek vector ko pehle matrix ke through ghumaya jata hai
# aur fir usi vector se wapas multiply kar diya jata hai

# 👉 Formula ka flow:
# vector  →  matrix  →  vector
# xᵀ A x


# Kyun use karte hain? (Why important)
# Quadratic form hume batata hai:
# - cost kitni hai
# - energy kitni hai
# - surface upar khuli hai ya niche
# - optimization safe hai ya nahi

# 👉 Machine Learning aur Optimization ka base concept hai


# Real-life examples (1 line)
# - Spring system → energy measure
# - ML loss function → error measure
# - Physics → stability check

#1.) Quadratic Form  Formula is => Q(x)=xTAx    here T is upon the x and T means Transpose row into column and column into row
import numpy as np
A = np.array([[1,2],    # this isthe metrix
              [2,3]])
x = np.array([1,2])   # this is the array okey
apply_Formula = x.T @ A @ x
print(apply_Formula)

# Agar result positive (>0) → quadratic form stable hai, energy/store value hamesha positive hai
# Agar result zero (=0) → system neutral hai, energy/store zero hai, koi effect nahi
# Agar result negative (<0) → system unstable hai, energy/store negative, matlab unrealistic ya problem
# ✅ Matlab: ye decide karta hai ki system behave karega stable, neutral ya unstable


#2. Rayleigh Quotient ek number deta hai jo batata hai:
# 👉 “Is direction (vector x) me matrix A kitna stretch / squeeze kar rahi hai?”
#Formula R(x) = (x transpose * A * x) / (x transpose * x)
import numpy as np
A = np.array([[1,2],    # this isthe metrix
              [2,3]])
x = np.array([1,2])   # this is the array okey
ap_f = ( x.T @ A @ x )/(x.T @ x)
print(ap_f)

#3. PSD and PD

# Imagine tum ek spring system dekh rahe ho
# x = kitna push lagaya spring me (vector)
# A = spring ki stiffness ya resistance (matrix)
# Q = x.T @ A @ x → total energy stored due to your push
# Agar Q > 0 → spring stable, energy positive → **Positive Definite (PD)**
# Agar Q = 0 → neutral, energy zero → **Positive Semi-Definite (PSD)**
# Agar Q < 0 → system unstable, energy negative → **Not PD/PSD**
# ✅ Matlab: ye check karta hai ki system stable hai ya nahi

import numpy as np
A = np.array([[1,2],    # this isthe metrix
              [2,3]])
x = np.array([1,2])
Q = x.T @ A @ x
if Q>0:
  print("PD",Q)
elif Q==0:
  print(" PSD",Q)
else:
  print(" Not PSD and PD",Q)


import numpy as np

# Example symmetric matrix
A = np.array([[2, -1],
              [-1, 2]])

# Compute eigenvalues
eigvals = np.linalg.eigvals(A)
print("Eigenvalues:", eigvals)

# Check PSD / PD
if np.all(eigvals > 0):
    print("PD → All directions positive")
elif np.all(eigvals >= 0):
    print("PSD → No negative direction")
else:
    print("Not PSD/PD → Some direction negative")


import numpy as np

# Imagine tum ek multiplayer video game me ho
# Har player ka movement aur power matrix me store hai (matrix A)
# Leading principal minors → check karte hain ki team ke combinations stable hai ya nahi
# Agar sab minors > 0 → team ka combo fully strong → PD
# Agar sab minors ≥ 0 → team me kuch weak links hain, but still safe → PSD
# Agar koi minor < 0 → kuch players clash kar rahe hain, team unstable → Not PD/PSD
# ✅ Matlab: minor check se easily pata chal jata hai ki team ka setup safe hai ya nahi

# Example symmetric matrix
A = np.array([[2, -1, 0],
              [-1, 2, -1],
              [0, -1, 2]])

n = A.shape[0]
is_pd = True
is_psd = True

# Check all leading principal minors
for k in range(1, n+1):
    minor = A[:k, :k]   # Top-left k x k submatrix
    det = np.linalg.det(minor)

# Determinant of each leading principal minor nikalne ka reason:
# Ye check karne ke liye ki **matrix PD (Positive Definite) ya PSD (Positive Semi-Definite)** hai ya nahi
# Rule: 
# - Agar har top-left k x k minor ka determinant > 0 → matrix PD
# - Agar har top-left k x k minor ka determinant ≥ 0 → matrix PSD
# ✅ Matlab: determinant se step-by-step system ke stability ya energy positivity ka pata chalta hai


    print(f"Determinant of {k}x{k} minor: {det}")
    if det <= 0:
        is_pd = False
    if det < 0:
        is_psd = False

if is_pd:
    print("PD → All minors positive")
elif is_psd:
    print("PSD → All minors non-negative")
else:
    print("Not PSD/PD")

import numpy as np
# Imagine tum ek photo-editing app use kar rahe ho
# A = pixels ka original data (matrix, har color channel / feature)
# A.T @ A → convert kar diya original data ko "safe energy space" me → hamesha PSD
# Eigenvalues → har direction me data kitna stretch ho raha hai, ya kitna info hai
# Agar sab eigenvalues > 0 → data full-rank, har feature useful → PD
# Agar sab eigenvalues ≥ 0 → kuch directions redundant, but safe → PSD
# Agar koi eigenvalue < 0 → data me problem, unstable → Not PD/PSD
# ✅ Matlab: A^T A se kisi bhi matrix ko PSD banake system ki stability / feature strength check kar sakte ho

# Any real matrix (not necessarily symmetric)
A = np.array([[1, 2],
              [3, 4],
              [5, 6]])

# Multiply transpose
ATA = A.T @ A # it converts any mattrix into psd
print("A^T A =\n", ATA)

# Check eigenvalues
eigvals = np.linalg.eigvals(ATA)
print("Eigenvalues of A^T A:", eigvals)

# PSD / PD check
if np.all(eigvals > 0):
    print("PD → Full rank, safe in all directions")
elif np.all(eigvals >= 0):
    print("PSD → Positive semi-definite")
else:
    print("Not PSD/PD")

#SPECIAL NOTE 
# Tumne perfectly notice kiya:
# - Agar kisi system ki **speed, strength, stiffness** dikhani ho → use matrix me store karte hain
#   (kyunki ye multiple directions aur interactions me vary kar sakti hain)
# - Agar kisi system me **movement ya direction** dikhani ho → use vector me represent karte hain
# ✅ Matlab: matrix → properties / system info, vector → actual motion / direction
