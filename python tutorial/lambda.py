'''
A lambda function :-

a lambda function is a small anaonymous function 
 a lambda function can take any number of argumnets but can only have one expression 

Syntax 
lambda arguments : expression 
 

 '''


'''
x = lambda a : a + 10
print(x(5))

'''
'''
x = lambda a , b , c : a*b+c
print(x(5,6,6))
'''
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))




