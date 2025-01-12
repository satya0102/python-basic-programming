#with the while loop we can execute a set of character as long as a condition is true 
i = 1
while i< 6:
    print(i)
    i += 1



#the break ststement 
# with the break statement we can stop the loop even if the while condition is true 

i = 1
while i<5:
    print(i)
    if i== 3:
        break
    i += 1


#continue ststement 
# with the continue statement we can stop the current iteration and continue with the next 

i = 0
while i < 8:
    i += 1
    if i == 5:
        continue
    print(i) 


#the else statement 
# with the else statement we can run a block of code once when the condition no longer is true 
i = 1
while i < 6 :
    print(i)
    i += 1
else:
    print("i is no longer less than 6 ")


    





