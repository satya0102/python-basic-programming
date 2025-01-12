'''
print("hello world")


#type function
print(type(12))

#round function 
print(round(62.3345))

#eval function 
eval('20+30')


n1 = eval(input('Enter a number '))
n2 = eval(input('enter an arthematic operator '))


print("n1+n2")


costPrice = int(input('enter cost price: '))
profit = int(input('enter profit: '))
sellingPrice = costPrice + profit 
print('Selling price: ', sellingPrice )
'''


age = int(input("enter a age: "))

if age >= 18:
    print("person is elligible to vote: ")
else:
    print("person is not elligible to vote: ")
