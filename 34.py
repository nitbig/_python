#List in python
"""A list is a mutable, ordered collection of elements.
It can store elements of different data types(integer, string, float, even other lists)

Characteristics of Lists:--
Ordered
Mutable
Allows duplicated
Heterogeneous
Indexing & slicing supported


Syntax:

my_list=[10, 20, 30, 40]
"""
#Creating  Lists

list1=[]    #Empty list
list2=[1,2,3,4,5]   #Integers
list3=["apple", "banana", "cherry"]  #Strings
list4=[10,"Python", 3.14, True]   #mixed data types
list5=[[1,2],[3,4]]     #Nested List

#Accessing List Elements

nums=[10,20,30,40,50]

print(nums[0])  #prints element--> 10
print(nums[-1])   #Last element --> 50
print(nums[1:4])  #Slicing -> [20,30,40]

#modifying Lists
nums=[1,2,3,4]
nums[2]=99   #Change Element
print(nums)   #[1,2,99,4]

#List Methods

fruits=["apple","Banana","cherry"]

fruits.append("mango")   #add at end
fruits.insert(1, "orange")   #Insert at position
fruits.remove("banana")   #Remove element
popped = fruits.pop()     #Remove last element
fruits.sort()             #sort list
fruits.reverse()           #Reverse order
print(len(fruits))          #Length of list


for item in fruits:
    print(item)

    #Use list when you need a dyanamic, changable collection