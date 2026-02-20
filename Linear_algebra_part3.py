# next hai hamara dimensions rigt matlab The dimension is about how many independent basis vectors you need to represent your space
# in upper cart example we take that same and code it 
# Phone price prediction example right and one main thing if  a things has 10 features but 3 dimesnions so taht means 7 are redundant 
import numpy as np 
# lets say our phone price depends on 2 independet features right ist prefromance second storage capacity 
# now we pridict the score on the basis  of it we have many featutres but as minimum we take as better of it right 
performance_vector = np.array([1,0]) # thats means pure performance only , no storage right
storage_Vector = np.array([0,1]) # pure storage only , no performance right

# TO ISI ALGORITHUM TECHNIQUE SE HAM PHONE PRICE PREDICTION CODE BANATE HAI OKEY SO LETS DO IT 
# JISME AVILABLE OPTINOS OF MOBILES DALENGE AND USER PICK KEREGA TO YE PRICE DEGA OK SO 
import numpy as np 
# let assume that two variants same mobile company prices right 
iphone15gbof128 = 79000
iphone15pro128gb = 134900

performance_upgrade_cost = iphone15pro128gb-iphone15gbof128
storage_upgrade_cost  = 1000 # here we let the cos tof upgrade the storage right  now 
# and here we take only two facttors that one is perfomrance based and second is storage based prediction right then 
print("Basis Vector:")
performance_basis = np.array([55000,0]) 
storage_basis = np.array([0,10000])
print("performance",performance_basis)
print("storage",storage_basis)

# Now we put the functonality of the user input right so 
print("\n" + "="*50) # this is nothing but to decorate the code trick 
print("PHONE PRICE PREDICTOR")
print("="*50)

print("\navilable options:")
print("1. iPhone 15 Pro (A17 Pro + 256GB)")
print("2. iPhone 15 (A16 + 512GB)")
print("3. iPhone 15 Pro Max (A17 Pro + 512GB)")

choice = input("\nWhich phone prediction do you want to make? (1/2/3): ")
base_price = 79000
if choice == "1":
    phone = 1*performance_basis +1*storage_basis
    predicted_price = base_price+phone[0]+phone[1]
    actual_price=159900
  name = "iPhone 15 Pro (A17 Pro, 256GB)"
elif choice == "2":
  phone = 1*performance_basis +0*storage_basis
  predicted_price = base_price+phone[0]+phone[1]
  actual_price=134900
elif choice == "3":
    # 1 performance + 3 storage upgrades
    phone = 1*performance_basis + 3*storage_basis
    predicted_price = base_price + phone[0] + phone[1]
    actual_price = 189900
    name = "iPhone 15 Pro Max (A17 Pro, 512GB)"
else:
    print("Invalid choice !")
    exit()
print("\n" + "="*50)
print("RESULT:")
print("="*50)
print("Phone:", name)
print("Vector:", phone)
print("Predicted Price: ₹", predicted_price)
print("Actual Price: ₹", actual_price)
print("Difference: ₹", abs(predicted_price - actual_price))

# Next 11th topic hai hamara matrices 
matrices = np.array([[1,2],[2,3],[3,4]])
matrices
# Next 11th topic hai hamara matrices 
matrices = np.array([[1,2],[2,3],[3,4]])
matrices
np.zeros(2) # performing zero 
matrices.shape
matrices.ndim
Transpose = matrices.T
Transpose
np.eye(3)#create an identical matrix 

#Next topic 12th matrices opeartions 
import numpy as np

print("="*60)
print("📊 MATRIX OPERATIONS - Complete Guide")
print("="*60)

# Create sample matrices
A = np.array([[1, 2], 
              [3, 4]])

B = np.array([[5, 6], 
              [7, 8]])

C = np.array([[2], 
              [3]])

print("\nMatrix A:")
print(A)
print("\nMatrix B:")
print(B)
print("\nMatrix C:")
print(C)

# ============================================================
# 1. MATRIX ADDITION (Element-wise)
# ============================================================
print("\n" + "="*60)
print("1️⃣ MATRIX ADDITION")
print("="*60)

addition = A + B
print("A + B =")
print(addition)
print("✅ Use: Combining datasets, merging features")

# ============================================================
# 2. MATRIX SUBTRACTION (Element-wise)
# ============================================================
print("\n" + "="*60)
print("2️⃣ MATRIX SUBTRACTION")
print("="*60)

subtraction = A - B
print("A - B =")
print(subtraction)
print("✅ Use: Finding differences, error calculation")

# ============================================================
# 3. SCALAR MULTIPLICATION
# ============================================================
print("\n" + "="*60)
print("3️⃣ SCALAR MULTIPLICATION")
print("="*60)

scalar_mult = 3 * A
print("3 * A =")
print(scalar_mult)
print("✅ Use: Scaling data, learning rate multiplication")

# ============================================================
# 4. ELEMENT-WISE MULTIPLICATION (Hadamard Product)
# ============================================================
print("\n" + "="*60)
print("4️⃣ ELEMENT-WISE MULTIPLICATION")
print("="*60)

element_mult = A * B
print("A * B (element-wise) =")
print(element_mult)
print("✅ Use: Attention mechanisms, gating in neural networks")

# ============================================================
# 5. MATRIX MULTIPLICATION (Dot Product) - MOST IMPORTANT!
# ============================================================
print("\n" + "="*60)
print("5️⃣ MATRIX MULTIPLICATION (@ operator)")
print("="*60)

# Method 1: @ operator (recommended)
matrix_mult = A @ B
print("A @ B =")
print(matrix_mult)

# Method 2: np.dot() (old way)
matrix_mult_dot = np.dot(A, B)
print("\nnp.dot(A, B) =")
print(matrix_mult_dot)

print("✅ Use: Neural network forward pass, transformations")

# ============================================================
# 6. MATRIX-VECTOR MULTIPLICATION
# ============================================================
print("\n" + "="*60)
print("6️⃣ MATRIX-VECTOR MULTIPLICATION")
print("="*60)

mat_vec = A @ C
print("A @ C =")
print(mat_vec)
print("✅ Use: Applying transformations to data points")

# ============================================================
# 7. TRANSPOSE
# ============================================================
print("\n" + "="*60)
print("7️⃣ TRANSPOSE")
print("="*60)

transpose = A.T
print("A.T (transpose) =")
print(transpose)
print("✅ Use: Gradient calculation, switching rows/columns")

# ============================================================
# 8. POWER (Element-wise)
# ============================================================
print("\n" + "="*60)
print("8️⃣ ELEMENT-WISE POWER")
print("="*60)

power = A ** 2
print("A ** 2 (element-wise) =")
print(power)
print("✅ Use: Squared error, activation functions")

# ============================================================
# 9. DIVISION (Element-wise)
# ============================================================
print("\n" + "="*60)
print("9️⃣ ELEMENT-WISE DIVISION")
print("="*60)

D = np.array([[2, 4], 
              [6, 8]])
division = A / D
print("A / D =")
print(division)
print("✅ Use: Normalization, probability calculations")

# ============================================================
# 10. MATRIX INVERSE (if exists)
# ============================================================
print("\n" + "="*60)
print("🔟 MATRIX INVERSE")
print("="*60)

try:
    inverse = np.linalg.inv(A)
    print("Inverse of A =")
    print(inverse)
    
    # Verify: A @ A_inv = Identity
    verify = A @ inverse
    print("\nVerification (A @ A_inverse) =")
    print(verify)
    print("✅ Use: Solving linear equations, optimization")
except:
    print("Matrix is not invertible!")

# ============================================================
# 11. DETERMINANT
# ============================================================
print("\n" + "="*60)
print("1️⃣1️⃣ DETERMINANT")
print("="*60)

det = np.linalg.det(A)
print("Determinant of A =", det)
print("✅ Use: Check invertibility, volume scaling")

import numpy as np

print("="*60)
print("🏠 HOUSE PRICE PREDICTION - Real Example")
print("="*60)

# INPUT FEATURES (X)
# Feature 1: Area (in 1000 sq ft) = 1.0 (matlab 1000 sq ft)
# Feature 2: Age (in years) = 2.0 (matlab 2 years old)

X = np.array([[1.0],   # Area: 1000 sq ft
              [2.0]])  # Age: 2 years

print("\n📊 INPUT (Ghar ki details):")
print("Area: 1000 sq ft")
print("Age: 2 years")
print("X =")
print(X)

# WEIGHTS (W) - Machine ne seekha hai training se
# Row 1: Price calculation
# Row 2: Demand calculation

W = np.array([[0.5, 0.3],   # Weight for price calculation
              [0.2, 0.8]])  # Weight for demand calculation

print("\n⚖️ WEIGHTS (Model ne seekhe hue):")
print("W =")
print(W)
print("\nMeaning:")
print("Row 1: [0.5, 0.3] → Price = 0.5×Area + 0.3×Age")
print("Row 2: [0.2, 0.8] → Demand = 0.2×Area + 0.8×Age")

# PREDICTION
Y = W @ X

print("\n💰 PREDICTION (Y = W @ X):")
print(Y)

# DETAILED CALCULATION
print("\n🔢 DETAILED CALCULATION:")
price = 0.5*1.0 + 0.3*2.0
demand = 0.2*1.0 + 0.8*2.0

print("Price prediction = 0.5×1000 + 0.3×2 =", price, "→ ₹", price*10, "lakhs")
print("Demand score = 0.2×1000 + 0.8×2 =", demand)

print("\n" + "="*60)
print("🎯 REAL MEANING:")
print("="*60)
print("Agar ghar:")
print("  • 1000 sq ft area hai")
print("  • 2 years purana hai")
print("\nTo model predict karta hai:")
print("  • Price: ₹11 lakhs (approx)")
print("  • Demand score: 1.8 (high demand!)")
# ============================================================
# SUMMARY TABLE
# ============================================================
print("\n" + "="*60)
print("📋 QUICK SUMMARY")
print("="*60)
print("Operation          | Syntax        | ML Use")
print("-" * 60)
print("Addition           | A + B         | Combine datasets")
print("Subtraction        | A - B         | Calculate errors")
print("Scalar multiply    | k * A         | Scale learning rate")
print("Element-wise mult  | A * B         | Gating, attention")
print("Matrix multiply    | A @ B         | Neural net layers")
print("Transpose          | A.T           | Gradient calc")
print("Inverse            | np.linalg.inv | Solve equations")
print("Determinant        | np.linalg.det | Check invertibility")

print("\n✅ Topic 12 COMPLETE! Ready for Topic 13: Special Matrices")
