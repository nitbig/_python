#TUPLE

"""
A tuple is an immutable(unchangeable), ordered collection 
collection of elements. Like lists, tuples can store 
heterogeneous data.

#Characteristics of Tuple
ORDERED
IMMUTABLE
ALLOWS DUPLICATES
HETEROGENEOUS ALLOWED
iNDEXING & SLICING SUPPORTED
"""

#syntax
my_tuple=(10,20,30,40)

#Note: A single-element tuple needs a comma

t1=(5,)   #Tuple
t2=(5)     #Just an integer


#Creating Tuples

tuple1=()      #Empty tuple
tuple2=(1,2,3,4,5)   #integers
tuple3=("a", "b", "c")   #Strings
tuple4=(10, "hello", 3.14, True)  #Mixed data Types
tuple5=((1,2),(3,4))   #Nested tuple


#Accessing Tuple Elements

nums=(10,20,30,40,50)

print(nums[0])    #10
print(nums[-1])    #50
print(nums[1:4])    #(20,30,40)

#Immutability of Tuples

nums=(1, 2, 3)
#nums[1] = 99    Error(can't modify)

#Tuple Methods
#only a few methods available

t=(1,2,2,3,4)

print(t.count(2))   #2-> no, of times 2 appears
print(t.index(3)) #3-> index of Element 3

#Iterating Tuples
for item in t:
    print(item)

    #use tuple when you need a fixed, read-only collection
    