#Looping through dictionary

student={
    "name": "Nitesh",
    "age": 21,
    "course": " computer science",
    "marks" : [85, 90, 88]

}
print(student)


for key in student:
    print(key, ":", student[key])

for key, value in student.items():
    print(key, "=>", value)
    
