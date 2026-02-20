#New topic [ Subtopics heading below there ]

#Dot Product (Orthogonality check)

#Angle Between Vectors

#Projection of a Vector onto Another Vector

#Projection using Unit Vector

#Error / Orthogonal Component

#Orthogonal Complement (single vector)

#Orthogonal Complement (subspace / matrix)

#Projection onto a Subspace (matrix form)

#Least Squares Interpretation

#ML Intuition Check (final sanity)



import numpy as np
vec_v1 = np.array([1,2])
vec_v2 = np.array([2,3])
print(np.linalg.norm(vec_v1))
print(np.linalg.norm(vec_v1,ord=3))
print(np.linalg.norm(vec_v1,ord=np.inf))
unit_v = vec_v1/np.linalg.norm(vec_v1)
print(unit_v)
print(np.linalg.norm(vec_v1-vec_v2))


# Now we see the projection of a vector onto another vector so the formula is

# Imagine you are pushing a trolley in a mall
# The trolley can move only straight forward (v2)
# But you push it slightly sideways by mistake (v1)
# Only the forward part of your push actually moves the trolley
# The sideways push does nothing and is wasted
# Projection = useful push in the correct direction
# ✅ Used to keep only what actually works and ignore waste


#Dot product of u and v divide by underroot vsquare into v
import numpy as np
v1 = np.array([1,2])
v2 = np.array([2,3])
#applying formula
w1 = (np.dot(v1,v2)/np.linalg.norm(v2)**2)*v2
print(w1)
#So this way we find out the projection between two vectors okey by remembering
# that formula that is dot product of two vector divide by length of second vector
#**2)*second vector again okey

#NOTE : Method-1: “Push along THIS long walkway”


# now we find out the w2 the vector component of u orthogonal to v so
# thats formula is w2 = u-w1

# Imagine you are walking in heavy rain
# Wind is blowing in one fixed direction (v2)
# You walk in some other direction (v1)
# w1 = part of your walking that goes with the wind
# w2 = part of your walking that goes sideways against the wind
# Sideways effort makes you tired but doesn’t help forward
# ✅ Used to split helpful movement and useless movement

import numpy as np
v1 = np.array([1,2])
v2 = np.array([2,3])
#applying formula
w1 = (np.dot(v1,v2)/np.linalg.norm(v2)**2)*v2
print(w1)
# now we find out the w2 the vector component of u orthogonal to v so
# thats formula is w2 = u-w1
w2 = v1-w1
print(w2) # in this case in w1 if we push somneone fro  ramp so the push that goes alson the ramp
# called w1 and in w2 t dont apply it dont goes along with that it goes orthogonal or sidways .


#finding the vector projection using unit vector right so

# Imagine you are in a mall walking on a straight moving walkway
# The walkway moves in only one direction (unit vector v3)
# You try to walk diagonally while talking to a friend (v1)
# Only the part of your walk along the walkway matters
# That straight-ahead part = projection using unit vector
# Unit vector means: only direction of the walkway
# Matrix A is like a security guard gently pushing you sideways
# After that push, your walking direction changes (s)
# ✅ Used to separate direction you want vs outside influence


import numpy as np
v1 = np.array([1,2])
A = np.array([[5,6],[2,3]])
v2 = np.array([2,3])
v3 = v2/np.linalg.norm(v2)
proj = np.dot(v1,v3)*v3
print(proj) # means that like we stricking the torch light on wall so the shsadow will come
# that is our total result of this formual okey right
#small note mattrix multiplicaiotn ko hi shear bolte hai uske result ko right like
s = A@v1
print(s)

#NOTE: Method-2: “Push only in THIS direction, length doesn’t matter”


# 1️⃣ What you did before (projection onto 1 vector)

# Imagine one stick on the ground
# You have a ball (vector) in the air
# You shine a torch on the ball → shadow falls only on that stick
# That shadow = projection onto the stick
# The part of the ball’s motion going sideways = orthogonal component
# ✅ So, only one direction matters here.

# 2️⃣ Now (projection onto subspace / matrix form)

# ✅ So now many directions together define the space (subspace).Socho tum ek shopping mall me gaye, 
#jahan kuch fixed walking paths banaye gaye hain—jaise floor par lines ya corridors jo sirf ek ya do directions me ja rahe hain.
#Tum randomly chal rahe ho, diagonally, idhar-udhar, apni friend se baat karte hue. Mall ka security system kehta hai ki tum sirf unhi
#fixed paths pe chal sakte ho. Ab jo part tumhare chalne ka exactly un paths ke direction me gaya, wahi projection hai—yehi tumhare 
#steps ka useful part hai. Jo tumhare steps us path ke bahar gaye, side me ya diagonally, wahi orthogonal part hai—yeh efforts wasted
#hain, mall ke rules ke hisaab se correct karne padenge. Agar mall me ek hi straight corridor ho → simple line (Code 1). Agar mall me 
#ek area hai jahan multiple directions allowed hain → flat plane (Code 2). ✅



# Now next is orthogonal complement on subspace matrix okey
# so first what is subspace ( ye dikhati hai distance origian se like ham aise likhet hain
# s = span {(1,2)}) ab ye hamara subspace hai abb ise matrix ki form me likhenge ham use hi subspace matrix
#bola jata hai right now

#1
import numpy as np
subspaceof_matrix = np.array([[1],
             [2]])
now_we_need_vector = np.array([2,1])
# So this is the projection onto subspace
P = subspaceof_matrix @ np.linalg.inv(subspaceof_matrix.T @ subspaceof_matrix) @subspaceof_matrix.T
p_proj = P @ now_we_need_vector
print(p_proj)
v_ortho = now_we_need_vector - p_proj
print(v_ortho)

#2
we_have_a_matrix = np.array([[1,0],
                     [0,1],
                     [1,1]]) # this is 3x2 matrix subspae matrix just for now for understanding okey
now_we_have_vector = np.array([2,3,4])
#now we applyin formula here also like previous one

P = we_have_a_matrix @ np.linalg.inv(we_have_a_matrix.T @ we_have_a_matrix) @ we_have_a_matrix.T
p_project = P @ now_we_have_vector
print(p_project)
now_we_have_vector_ortho = now_we_have_vector-p_project
print(now_we_have_vector_ortho)


# Least Squares Interpretation

## Socho tum ek mall me ho aur tumhare paas ek delivery robot hai
# Mall ke floor par kuch fixed paths banaye gaye hain
# Tumhare robot ko teen alag-alag points pe deliveries deni hain
# Robot ke paas sirf do directions me chalne ki ability hai
# Isliye wo teen points ko ek saath exact nahi hit kar sakta
# Ab robot smart hai: wo apni movement aise plan karta hai
# Ki sab points ke nazdeek sabse best path follow kare
# Yehi uska projection hai → jo movement allowed directions me actually useful hai
# Jo movement points se miss hota hai → wo residual hai → thoda sa error ya wasted effort
# ✅ Matlab: robot har delivery point pe exact nahi ja pa raha
# Lekin total distance ka error minimum karke best approximate path follow kar raha hai

import numpy as np

# Suppose we have a system of equations (over-determined)
# Example: 3 equations, 2 unknowns
# A x = b  (cannot solve exactly because more equations than unknowns)
A = np.array([[1, 1],
              [1, 2],
              [1, 3]])  # 3x2 matrix (3 equations, 2 unknowns)

b = np.array([1, 2, 2])  # target values

# Least squares solution: x_hat = (A^T A)^-1 A^T b
x_hat = np.linalg.inv(A.T @ A) @ A.T @ b
print("Least squares solution (x_hat):", x_hat)

# Compute predicted values (projection onto column space of A)
b_proj = A @ x_hat
print("Projection of b onto column space of A:", b_proj)

# Compute residual (orthogonal component / error)
residual = b - b_proj
print("Residual (orthogonal to subspace):", residual)


# ML Intuition Check (final sanity)

# Imagine you are trying to predict a student's score
# You have some features like hours studied and practice tests (these form a "feature subspace")
# The true score is like a vector in space (target vector b)
# Your prediction is like projecting b onto the feature subspace
# The "shadow" of the score on the feature subspace = predicted score
# The part of the score that is perpendicular to feature subspace = residual error
# ✅ So all your projections, subspaces, and least squares together explain how ML predicts as best as possible

import numpy as np

A = np.array([[1, 2],    
              [2, 1],    
              [3, 0]])   


b = np.array([5, 4, 6])

x_hat = np.linalg.inv(A.T @ A) @ A.T @ b
print("ML feature weights (x_hat):", x_hat)

b_proj = A @ x_hat
print("Predicted scores (projection onto subspace):", b_proj)

residual = b - b_proj
print("Residuals (orthogonal to feature subspace):", residual)


# TOPIC FINISHED HERE #
