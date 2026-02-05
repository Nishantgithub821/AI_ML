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

# Next topic is our 
