#check vevctor is orthogonal and orthonormal
#orthonormal
v1 = np.array([1, 2])
v2 = np.array([-2, 1])

len = np.linalg.norm(v2)
if len == 1:
  print("vector is orthonormal ")
else:
  print("Not , vector are not orthonormal ")

#orthogonal
import numpy as np

# Define two vectors
v1 = np.array([1, 2])
v2 = np.array([-2, 1])

# Compute dot product
dot = np.dot(v1, v2)

# Check if dot product is zero
if dot == 0:
    print("Vectors are orthogonal")
else:
    print("Vectors are NOT orthogonal")

#how to find out the angle                        # here we learn arccos and degree lib component in numpy (arccoss convert the values in radian )
import numpy as np
a = np.array([1,2])
b = np.array([2,3])
# we find out the angle between two vectors
# first we find out upper part in formula that is dot product
dot_product = np.dot(a,b)
#now we find out the length of both a and b and then we divide our c with Mulitpliccation of both lengths
length1 = np.linalg.norm(a)
length2 = np.linalg.norm(b)
# now we apply the formula upper is dot prodcut in lower there is mulitplicaiton so
apply_formula = dot_product/(length1*length2)
# now we find radian so
in_Radian = np.arccos(apply_formula) # here our values comes in cos−1(0.984)≈0.179 radians like this because computer understand cos sin and all are in radian thats why
in_degree = np.degrees(in_Radian)
print(in_degree) # so this is the angle between the two vectors

# So here we see some laws first is commutative law                      # we lear
#this thing that if we apply if condtion in array so we dont use == we only use when
# we work in single digits numbers in array we use np.array_equal (builtin function)
import numpy as np
v1 = np.array([1,2])
v2 = np.array([2,3])
v3 = v1+v2
v4 = v2+v1
if np.array_equal(v3,v4):
  print("Yes this follows commutative law ")
else:
  print("Not it does not follow comutative law")

#associative law  # here we learn about if vector are more than two then we use add operation to check whether all three are equal or not
import numpy as np
v1 = np.array([1,2])
v2 = np.array([2,3])
v3 = np.array([3,4])
v4 = v1+(v2+v3)
v5 = (v1+v2)+v3
v6 = v1+v2+v3
if np.array_equal(v4,v5) and np.array_equal(v5,v6):
  print("Yes this follows asssocaite law ")
else:
  print("Not it does not follow associative law")
