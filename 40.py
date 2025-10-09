#Removing Items 
student={
    "name": "Nitesh",
    "age": 21,
    "course": " computer science",
    "marks" : [85, 90, 88]

}
student.pop("course")  #remove by key
# student.popitem()      #Remove the last inserted item
# del student["marks"]    #Delete specific key
# student.clear()           #Remove all items 

print(student)