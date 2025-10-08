#Slicing
#accessing parts of a string is called slicing

# str[starting_index : ending_index] #ending index not included

str= "nitish kumar"
print(str[1:4])
print(str[:5])  #prints from 0 index [0:5]
print(str[5:])    #prints till index last [5:len(str)]
print(str[5:len(str)])     #prints till last index