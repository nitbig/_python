"""| Feature         | List ([])                  | Tuple (`()`)                   |
| --------------- | ---------------------------- | ------------------------------ |
| **Mutability**  | Mutable                      | Immutable                      |
| **Syntax**      | `[]`                         | `()`                           |
| **Methods**     | Many (append, remove, etc.)  | Few (count, index)             |
| **Performance** | Slower                       | Faster                         |
| **Use case**    | When data needs modification | When data should stay constant |
"""

#Example Showing Difference

#List
l=[1,2,3]
l[0]=100
print(l) #[100, 2, 3]  allowed

#Tuple
t=(1,2,3) 
#t[0]=100 Error
