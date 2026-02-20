# So  This is the numpy lecture okey for the machine learning .
#pre-requists for it first knwoign about list loops datasetts and variables so this is okey for now later on we see the dictonaries and tuples etc.
#PHASE 1
import numpy as np
arr_1D = np.array([1,2,3,4,5])
print(arr_1D)
arr_2d = np.array([[1,2,3],[3,4,5]]) # here we put the two arrays in single list thats why it doesnt give any error
print(arr_2d)

#diff between arrays and list opereations
py_list = [1,2,3]
print(py_list*2) # this is for list multiplication
# now for array
np_arr = np.array([1,2,3])
print(np_arr*2) # this is for array multiplication

# below is basic code to check the execution time of list vs array okey
import time
start = time.time()
py_list = [i*2 for i in range(1000000)]
print(time.time()-start)
start = time.time()
np_array = np.arange(1000000)*2
print(time.time()-start) # so numpy is far more faster than list simple one right

#creating array from scratch
zeroes = np.zeros((3,4))
print(zeroes) # it print the matrix of 3 by 4 fill with all zeroes
ones = np.ones((3,4))
print(ones) # it print the matrix of 3 by 4 filled with all ones
full  = np.full((2,2),7)
print(full) # it print 2 by 2 matrix fully filled with single number that is 7
random = np.random.random((2,2))
print(random) # print random matrix of 2 by 2 with random numbers
sequence = np.arange(0,11,3)
print(sequence) #last element is not included and gap is by 3 means 3 multiple

#vector,matrix and Tensor
vector = np.array([1,2,3]) # how vector is normally created right
print(vector) # this is normally how we create one d array thats called vector
matrix = np.array([[1,2,3],
                   [2,3,4]])
print(matrix) # this is 2d calle matrix and much nore than 2d called tensor

tensor = np.array([[[1,2],[2,3],[3,4],[4,5],[5,6]]])
print(tensor) # more than 2d called tensor okey

# Arrays properties
arr = np.array([[1,2,3],[2,3,8.6]])
print(arr.shape) # it print the shape of the array
print(arr.ndim) # how many dimesional of the earray is
print(arr.size) # size of the array
print(arr.dtype) # datatype

#Array Reshaping
arr = np.arange(12)
print(arr) # orignal array
reshaped = arr.reshape((3,4))
print(reshaped) #reshaped array
flattterned = reshaped.flatten() # it print copy
print(flattterned)
revelved = reshaped.ravel() # it prints real return iew instead of copy
print(revelved)
transpose = reshaped.T
print(transpose)


# PHASE 2 OF NUMPY : OPEARTIONS ON NUMPY ARRRAY
import numpy as np
#indexing and slicing
arr = np.arange(12)
print("Basic Slicing :",arr[2:7]) # goes from 2 to 6th position
print("with step ",arr[2:7:3]) # starting include , 7th not include and 3 difference
print("NEgative slicing",arr[-4])
#Now performing opration on 2d array
Two_D = np.array([[1,2,3], #0
                   [4,5,6], #1
                   [6,7,8], #2
                   [1,2,3]]) #3
print(Two_D[3,1])
print("Entire row",Two_D[1]) # this way we prints entire row ist which is 4,5,6
print("Entire column",Two_D[:,2]) # i think first paramter for row and second one is for column
#sorting
unsorted_array = np.array([1,4,3,2,5,6,4,3,2,23,4,4,5,1])
print("sorted_array is :",np.sort(unsorted_array))
arr_2d_unsorted = np.array([[3,1],[1,2],[2,3]])
print("Sorted 2d Sorted array by row )",np.sort(arr_2d_unsorted , axis=0)) # it goes top to bottom and majorly we use axis =0 and in rare cases we use axis =1
#Now Filtering
numbers = np.arange(12)
even_number = numbers[numbers%2==0]
print(even_number)
#Another Method in Filter with mask
mask = numbers>5
print("numbers greater than 5",numbers[mask])
#Fancy Indexing vs np.where()
indices = [0,2,4]
print(numbers[indices])
where_result = np.where(numbers>2)
print("NP where ",numbers[where_result])
#conditional array condition where wr put more than one condition that is our 2 or 3 i think we try with 2
condition_array = np.where(numbers>0 , numbers*40 ,numbers)
print(condition_array)
# How the code of conditional array is written in backend
#so always keep this thing in mind that numpy created from cpp yani ki c++ and
#now if(numbers>5){
 # numbers*40;
#}else{
# 3numbers
#}"""

#Arrays adding ,removing and combining
arr1 = np.arange(10)
arr2 = np.arange(10,20)
print("concatination is :",np.concatenate((arr1,arr2))) #combining process
#Whenw we work in ai or ml in depth then there we have lot of n dimensioanl data
# where we want to check the compatibility right

# comapnitbilty of array
a = np.array([1,2,3])
b = np.array([1,2,3,4])
c = np.array([1,2,6])
print("Comaptibility of a and b is ",a.shape==b.shape)
print("Comaptibility of a and c is ",a.shape==c.shape)
#some operations
orignal = np.array([[1,2],[2,3],[4,5]])
new_row = np.array([66,77])
with_new_row = np.vstack((orignal ,new_row)) # vstack always add the row
print(new_row)
print(with_new_row)
print(orignal) # orignal array
new_col = np.array([[73],[38],[44]]) # 3X3 if we add new col then we need three new elements in column right
with_new_col = np.hstack((orignal,new_col))
print(new_col)
print(with_new_col)

#now delted things
arr= np.array([1,2,3])
deleted = np.delete(arr,2)
print("Array after Deletion ",deleted) # now this is for one d
# similar like in 2d same like we do slicing before if we delte use like this [1:2]


#PRACTICE WITH REAL DATA WORLD WE PERFORM NUMPY OPERATIONS ON THAT FOR PRACTICE
import numpy as np
import matplotlib.pyplot as plt # we se  the little bit overview of this
# So real world scenrio is for data of the resturant [resturant_id,2021 ,2022,2023,2024] sales okey in which year
sales_data = np.array([
    [1,100,200,300,400],
    [2,500,600,700,800],
    [3,900,1000,1100,1200],
    [4,1300,1400,1500,1600],
    [5,1700,1800,1900,2000]
])
#first thing is to check thte size of the data
print(sales_data.shape)
print("print ist three resturant data ",sales_data[0:3])
print("sales ddata output",sales_data[:,1:])
print("if we printed all rows",sales_data[:])
print("if we printed all the columns ",sales_data[:,:])
print("if we print only one row  ",sales_data[0])
print(" ist column only ",sales_data[:,0])
print("total sales of every resturant per year ",np.sum(sales_data,axis = 0))  
print("total sales of every resturant per year ",np.sum(sales_data[:,1:],axis=0))
print("total sales of every resturant per year totally  in one frame then remove axis",np.sum(sales_data[:,1:]))
print("minimum sales per year",np.min(sales_data[:,1:],axis=1))
print("maximum sales per year",np.max(sales_data[:,1:],axis=0))
print("average sales per resturant",np.mean(sales_data[:,1:],axis=1))
cumsum =np.cumsum(sales_data[:,1:],axis=1)
print("cumalitive sum",cumsum)
plt.figure(figsize=(8,6))
plt.plot(np.mean(cumsum,axis=0))
plt.title("average cumulative sales acrossthe resturant")
plt.xlabel("YEars")
plt.ylabel("Sales")
plt.grid(True)
plt.show() # this will increase every time because the cumsum is always in increasing order right 

#some vector operations
vector1 = np.array([1,2,3])
vector2 = np.array([4,5,6])
print("vector addition",vector1+vector2)
print("vector subtraction",vector1-vector2)
print("vector multiplication",vector1*vector2)
print("dot product",np.dot(vector1,vector2))
angle =np.arccos(np.dot(vector1,vector2)/(np.linalg.norm(vector1)*np.linalg.norm(vector2)))
print(np.degrees(angle))
# String operations in list like vectorize means captilaize all the strings like that etc
resturant_types =np.array(["biryani","chienes"])
vectorized_upper =np.vectorize(str.upper)
print(vectorized_upper(resturant_types))
print("monthly_average",sales_data[:,1:]/12)

#Phase 4:

import numpy as np
import matplotlib.pyplot as plt
array1 = np.array([[1, 2, 3], [4, 5, 6]])
array2 = np.random.rand(3, 3)
array3 = np.zeros((4, 4))
np.save('array1.npy', array1)
np.save('array2.npy', array2)
np.save('array3.npy', array3)
loaded_array1 = np.load('array1.npy')
import matplotlib.pyplot as plt
import numpy as np

logo = plt.imread('numpy.webp')

plt.figure(figsize=(10, 5))

plt.subplot(121)
plt.imshow(logo)
plt.title("NumPy Logo")
plt.axis('off')

# create dark version
dark_logo = 1 - logo

plt.subplot(122)
plt.imshow(dark_logo)
plt.title("NumPy Dark Logo")
plt.axis('off')

plt.show()
