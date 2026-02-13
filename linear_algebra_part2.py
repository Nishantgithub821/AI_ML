# JO JO TOPICS HAM LINEAR ALGEBRA ME COVER KERENGE ISME 
"""
No.	Topic Name	One-line Label / ML Use
1	Scalars	Real numbers
2	Vectors	Feature representation
3	Vector Operations	Add / scale features
4	Vector Space	Valid data space
5	Subspace	Reduced feature set
6	Linear Combination	Weighted sum
7	Span	All possible outputs
8	Linear Independence	Remove redundancy
9	Basis	Minimum features
10	Dimension	Feature count
11	Matrices	Dataset representation
12	Matrix Operations	Data transformations
13	Special Matrices	Identity, diagonal
14	Matrix Rank	Information content
15	Determinant	Invertibility check
16	Inverse Matrix	Solve equations
17	Linear Equations (Ax=b)	Model equations
18	Row Reduction	Gaussian elimination
19	Column Space	Feature space
20	Null Space	Lost information
21	Orthogonality	Independent features
22	Dot Product	Similarity measure
23	Norms	Regularization
24	Distance Metrics	Clustering
25	Projection	Feature projection
26	Least Squares	Regression base
27	Eigenvalues	Variance
28	Eigenvectors	Principal direction
29	Diagonalization	Matrix simplification
30	Spectral Theorem	Symmetric matrices
31	SVD	Core ML decomposition
32	Low Rank Approximation	Dim reduction
33	PCA	Feature compression
34	Covariance Matrix	Feature relation
35	Linear Transformation	Data mapping
36	Change of Basis	New feature space
37	Trace	Sum of eigenvalues
38	Positive Definite Matrix	Optimization safety
39	Quadratic Forms	Loss functions
40	Gradient (LA view)	Optimization bridge
"""
#Vector all topics notes with real apllicable situations with example
#First we know how to declare vector , how to multiply vector to scaler
# now we talk our first topic unit vector so
import numpy as np
# first we initilaize from ourselves the cordinates like you know unit vector find the direction right so directio is 4 east west north south so
# if we check in xy plane of east means right side and in right side +1 and another vector is 0 because if we goes right then only goes right we dont able to go of up and down so that will be zero
# likewies the working of east south north as well
east_unit_vector = np.array([1,0]) # so here we take the cordinates of the east now
print(east_unit_vector)
# if the directions is given then let suppose we have given 2 of east and 5 of north so [2,5]
direction_ggiven_v = np.array([2,5])
unit_v = direction_ggiven_v/np.linalg.norm(direction_ggiven_v) # this is the formula
print(unit_v)
#Next hai projection
light_direction = np.array([4, 2])
wall_direction = np.array([1, 3])
shadow_on_wall = (np.dot(light_direction, wall_direction)
    / np.dot(wall_direction, wall_direction)
) * wall_direction
print("Shadow on wall:", shadow_on_wall)
# formule me ist dot wali condition dikhati hai ki ligth ka kitna hissa walla ki direction pe ja rha hai matlab wall pe takra rha hai right
# and second dot product scale kerne ke liyee wapise wall ki direction me fit kerna and in sab ko wall ki direction se mulitply ker dena usse final shadow nikal ke ati hai

# Next topic is the vector space but for that first we understand three things Linear combinations and span ,
#So in the linear combination there is only one thing that is when we multiply two vector to scaler and adding between them that is called linear combination 
# and span ka kya matlab hai in span when we scale the vector after adding then the all combinations of the vector is called span 
# now program 
import numpy as np

# Given vectors
v1 = np.array([1, 0])
v2 = np.array([0, 1])

# Coefficients (scalars)
a = 2
b = 3

# Linear combination
lin_comb = a * v1 + b * v2

print("Linear combination:", lin_comb)

# Next topi is our vector space then we start subspace after finishing this okey 
# Vector space ka matlab hai like ki ek space me sab kuch sab vector ek hi space me ana cahihye right ilke isme ye 3 rules follow kerta hai ist zero vector hona chaihiye , addition honi chaiye and multiplication
#honi chaihye but all this in same space or ham kahe ki space ke ander okey like if i take real life example depends on three rules to 
"""
Example: Shopping Cart Feature Vectors
Vector = [fruits, vegetables] → kitne fruits aur vegetables tum cart me rakhe
Zero vector = [0,0] → cart empty
Addition = [2,3] + [1,1] = [3,4] → do carts ko combine kar do
Scalar multiplication = 2 * [2,3] = [4,6] → double quantity of same cart
"""
# Next is Vector subspace 
"""
Now in vector subspace , isme kya hai ki three condition same vahi condition ko satisfy kerna chaihiye ist hai zero vector second agar ham kisi bhi unknown scaler ko us vector se multiply kere and result 
ko kuch bhi kerke vaih same vector le aye jo starting me liya tha that is also our second condition of subsapce that is vector under scaler multiplication and third is addtion as you know when we addtion 
two vectors that will also lies in that space right .
"""
# so lets do a code right in which we satisfy all those three conditons and proof that this is subspace ex off shopping cart right 
import numpy as np 
# ab ek rule hai ki jo cart hai usme veg hai and fruits hai to veg is multiply of 2 and fruit is of 1 
ruleof_Cart = np.array([1,2])
# ist is zero vector 
zero_cart_means_cart_is_empty = np.array([0,0])
print(zero_cart_means_cart_is_empty)

# second hame proof kerna hai ki sacler under multiplicaiton condition ko satisfy kerta hia ya nahi to 
cart = np.array([2,4])  # man le ki 2 fruits ho gaye hamarae pass and 4 veg yani ki 2 fruits dal diye 6 vegeis dal di cart me 
multiplier = 3 # matlab 3 a multiple ho gya to result aya 6 and 12 
final_cart = cart*multiplier
print(final_cart)
# now ham ab check kerenge if else se ki ye under multiplication hai ya nahi right 
scale_fruit = final_cart[0]/ruleof_Cart[0]
scale_veg = final_cart[1]/ruleof_Cart[1]
if scale_fruit==scale_veg:
    print("yes")
else:
    print("no")
#Last is our addition condition right 
cart1 = np.array([1, 2])
cart2 = np.array([2, 4])
add_both_of_them = cart1+cart2
print(add_both_of_them)
scale_fruit_add = final_cart[0]/ruleof_Cart[0]
scale_veg_add = final_cart[1]/ruleof_Cart[1]
if scale_fruit_add==scale_veg_add:
    print("yes")
else:
    print("no")

# Next topic is our Linear independence yar simple hai bilkul uper wale ka ulta jisme ki koi bhi combination multiply ya add se na bane simple 
# code and ex:
import numpy as np


cart1 = np.array([1, 2])
cart2 = np.array([2, 4])
cart3 = np.array([8, 16]) # simpler ye samajh dependent matlab dnoo ko ek hi scaler se multiply ker rhe hai like yaha pe hamne cart 2  ko 4 se multiply kera aise hi chahe 100 se ker le 

# Matrix of old carts
A = np.column_stack((cart1, cart2))

# Solve a*cart1 + b*cart2 = cart3 approximately
target = cart3
solution ,residual,rank,_ = np.linalg.lstsq(A,target,rcond=None)
# Check if new cart can be made
if np.allclose(A @ solution, cart3):
    print("❌ cart3 is dependent")
else:
    print("✅ cart3 is independent")
#Next hai basis basis matlab kya hota hai ki bina kisi extra information ke thoda se data se ml model pure data ko samjh sake 
# like agar ek cart me sirf2 cheeje aa sakti hai veg and fruit to hame na add kerna pade na multiply na ratio issab ke bawjab minimum opeariotn me result aye use bais bolte hai like ek vector hai
# [0,1] , second hai [1,0] to agar ham pehle ko 3 se dusre ko 5 se mulitply kere inme weight se mulitply kere to [3,5] apne app create ho gya and naya cart ban gya simple 
# Agar ham Code ki bat kere to 
import numpy as np
fruit_feature = np.array([1, 0])   # sirf fruits count karta hai
veg_feature   = np.array([0, 1])   # sirf vegetables count karta hai
cart = 3*fruit_feature + 5*veg_feature
print(cart)
# EK OR REAL LIFE PROBLEM SOLVE KERNE WALA ACTUAL EXMAPLE DETA HIN 
# LIKE HAMARA PASS BOHT SARI ITEMS HAI VEG KI AND FRUIT KI TO HAMARE PASS BOHT SARA 100+ DATA HAI 
# TO HAM KYA KERRENGE HAME PATA HAI TYPE 2 I HAI TO DONO TYPE ME ITEMS KO IKATTHA KER DENGE RIGHT LIKE 
import numpy as np 
customer_cart = np.array([1,2,3,   4,5,6])
# fruits: apple, banana, mango | veg: potato, onion, tomato
# now convert into basis like how let see 
total_fruits = customer_cart[:3].sum() # yaha pe start se leker second index tak 0 to 2 sari values ko add kerdega yani ki sum 
total_Vegies = customer_cart[3:].sum() # yaha pe 3rd index se last tak add ker deega 
basis_Feature = np.array([total_fruits,total_Vegies]) # fir ye unka array bana dega right 
print(basis_Feature)
