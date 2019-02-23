# annonymous functions 
# functions like, but no name
# no return

def square(num):
    return num * num
    
# function with different layout
def square(num): return num * num
print(square(2))    

#example of a lambda
result = lambda num: num * num
print(result(9))