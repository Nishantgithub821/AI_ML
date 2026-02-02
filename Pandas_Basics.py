# Remember this thing this all work do on jupyter notebook if you want to do in google colab that is your wish but from my side jupyter notebook is beneficial and if you want to install
#it watch any video on youtube to install the jupyter notebook in our system there is numirous videos easily avilable on internet from which you easily install it 
import numpy as np 
import pandas as pd
dict1 = {
    "name":["Nishant","Kaka","Golu","Anil","Pankaj"],
    "age":[21 , 23,23,22,21],
    "city":["A","B","C","D","E"],
}
df = pd.DataFrame(dict1)
df
# if we want to convert the dictonay code into different formate files like csv so we use this 
df.to_csv("NewFile.csv")
#now if we open up the file in vs code it incldes also the index so if we want to hide the index
df.to_csv("NewFile_Without_Index.csv",index=False)
#Now if we print the head of the content that is 
df.head(2) # now here 2 means from 0 to 1 and 2 is not included right 
df.tail(2) # now if we print the tail data then we also print it just like this 
df.describe() # it describes the count mean std min and much more 
# now if we want to read the file which we just created with our choice either its with index or without
read = pd.read_csv("NewFile.csv")
read # it print the data into our screen 
#now we read anything from the content okey 
read["city"] #city
read["name"] #name
read["age"]  #age
#read["age"][0] = 50 # this will cahnge the data but it given the warning so dont waorry or it 
#read # it will print that 
read = pd.read_csv("NewFile_Without_Index.csv")
read 
# now if we change the index of the data then we use 
read.index = ["F","S","TH","FO","FI"] # remember the indexing is counted and equal to the elements count
read # this way we change the index 

# Now we see some theortically part 
# Why we use the python why not the excel because it give us the funconatility to perform the list dic and tuples and also give us the libraries freely 
# and it give us the speed up result by inducling the numpy+pandas and also better storage 
# and also ecel sheet has so much limiataiotn of the data but program didnt okey 


# VERY IMP THING  [ DIFF BETWEEN SERIES AND DATAFRAME ]
# SERIES NOW SERIES REPRESENT ONE TYPE OF ONE D DATA LIKE EX IN BELOW TABLE AGE REPRESENT ONNLY INT TYPE OF DATA OR NAME
#REPRESENT ONLY STRING TYPE MEANS ONLY ONE TYPE EITHER IT STRING OR INT OR BOOL OR FLOAT ANYONE OK.
# DATAFRAME =  DATAFRAME MEANS THE BELOW GIVEN TABLE MEANS CONVERT THE DATA INTO TABUAR SPREADSHEET WHICH INCLUDES


# # ROWS AND COLUMN OKEY  Now next thing is this okey  
#lets see about series here from this cell 
ser = pd.Series(np.random.rand(34))
ser
type(ser)
# series is a datastrcture of a pandas when we give data to pandas it make indexing which
# help searching inserting in operations and also carrying the data
newdf = pd.DataFrame(np.random.rand(334,5),index=np.arange(334))
newdf.head() # if we want the head of the data
type(newdf) # it gives that it is dataframe
newdf.describe()
newdf.dtypes
newdf
newdf.head()
#newdf[0][0] = "Khiladi" # when we run this it change the first value from int into string now 
#newdf.dtypes   # by one is string another is int so it return the datatypes object of that series ok
newdf.index #return te index
newdf.columns # return the columns that is total 5 okey 
newdf.to_numpy #  right this and then shift + enter so it convert the datta into numpy array
#newdf[0][0] = 0.5
#newdf.head() # we also talk about this that if we change the number or string then that will reflect
# and datatype like in this case object is shown okey 
newdf.T # if we transpose the matrix or the data 
newdf.sort_index(axis=0, ascending=False) # sorted in the descend order in rows thats why we use =0 if we want row wise sorting 
newdf.sort_index(axis = 1 ,ascending =False) # sotring with column wise 
# if we create the excel sheet and then save it and then read by the compiler then how we do that use this 
# let assume our file name is Data 

newdf.head()
newdf[0]
type(newdf[0]) # tells us the type 
# so ths below concept is abuot the view if we assign the newdf2 = newdf then if we make changes 
newdf2 = newdf # then that means the  changes we print with the help of the newdf2 also thats the 
newdf2[0][0] = 5678 # concept of view 
newdf # then we print 

# now we see the copy 
newdf3 = newdf.copy() # this is our copy syntax it make a copy 
newdf3
# now we see the loc function 
newdf.loc[0,0] = 8907
newdf.head(2)

newdf.columns = list("ABCDE") # it convert the  
newdf
newdf.head(2)
newdf.loc[1,"B"]= 87086
newdf
newdf.drop("E",axis=1) # remove column from table okey

#newdf.drop(0,axis=0,inplace=True) # if we use inplace =True then it remvoe from orignal tabel 
newdf # otherwise we only cahnge in imaginary means in copy not in orignal 
newdf.reset_index(drop=True, inplace=True)
newdf.drop(1, inplace=True)
newdf

# if we want some set of column then 
newdf.reset_index(drop=True, inplace=True)
newdf.loc[[1,2], ['C','D']]# so 1 2 are the rows and the C and D are the Columns okey 

newdf.head()
# if we want all rowss and columns 
newdf.loc[:,["C","D"]] # it returns all the rows of C and D okey 
newdf.loc[[1,2,3] ,:] # it returns the all columns in respectively 1 and 2 okey 

# now we see how we run the complex queries here also okey so let see 
newdf.loc[(newdf["E"]<0.1) & (newdf["C"]>0.1)]
newdf.head(6)

newdf.iloc[[0,5],[3,2]] #iloc access with number
#Note If we access the name then we use the loc 
#Note And if we acess the number then we use the iloc
newdf.head(3)
newdf.drop([0]) # if we drop one row 
newdf.drop([6,10], axis=0 ,inplace=True)# if we drop one column 


newdf.head(3)
newdf.reset_index() #if we reset the indexing ten we use this 
newdf.reset_index(drop=True) # if we remove the index column also which was bydefault added in table by the compiler 
newdf.head(3)
newdf["E"].isnull() # it returns where the null is found in the table okey 
newdf["E"] = None # it assign the all values to the newdf E to None all the column okey 
newdf
#But never use that upper suntadx best  use to this is with the help of loc funtion how let see 
#now we do all the rows and one column that is E None right so all rows means : and one column that is E
# So :,E so 
newdf.loc[:, ["E"]] = 40 # like this way we set the value okey 
newdf
newdf.loc[2] = 444; # just take an example 
newdf
# always use loc and iloc when we dont understand nothing  
df = pd.DataFrame({
    "name": ["Alfred", "Batman", "Catwoman"],
    "toy": [np.nan, "Batmobile", "Bullwhip"],
    "born": [pd.NaT, pd.Timestamp("1940-04-25"), pd.NaT]
})
df.head()
df.dropna()
df.dropna(how="all")
df.dropna(how="all",axis=1)
df.drop_duplicates(subset=["name"]) # if we drop the duplicates  # it doesnt take asix parameter
df.drop_duplicates(subset=["name"] ,keep="first")
df.drop_duplicates(subset=["name"],keep="last")
df.drop_duplicates(subset=["name"],keep=False)
df.shape
df.info()
df["name"].value_counts(dropna = False)
df.notnull()

Data = pd.read_excel("Data.xlsx"), sheet_name="sheet2")
Data
#quiz Crete a dataframe which contains only inefers with 3 rows and 2 columns # run follwoing dataframe methods on them :
df.describe()

df.mean()
df.corr()
df.count()
df.max()
df.min()
df.meadian()
df.std()
