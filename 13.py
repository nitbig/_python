#Type casting examples

#Integer to Float
x=10
y=float(x)
print(y)      #10.0
print(type(y))   #<class 'float'>

#Float to integer
a=12.75
b=int(a)    #convert float-integer(decimal) part is removed
print(b) #12
print(type(b)) #<class 'int'>

#number to string
num=100
text=str(num)        #convert int - string
print(text)           #"100"
print(type(text))       #<class 'str'>

#string to Integer/Float

s1="50"
s2="45.67"

n1=int(s1)       #string - int
n2=float(s2)       #string - float

print(n1+10)     #60
print(n2+4.33)    #50.0


#List to Tuple(and vice versa)

lst=[1,2,3]
tpl=tuple(lst)     #list -  tuple
print(tpl)          #(1,2,3)

back_to_list=list(tpl)   #tuple -  list
print(back_to_list)       #[1,2,3]
