def maximum3(n1,n2,n3):

    if n1>n2:
        if n1>n3:
            maxNumber = n1
        else:
            maxNumber = n3
    
    elif n2>n3:
        maxNumber = n2
    else:
        maxNumber = n3
    return maxNumber

def main():
    n1 = int(input('Enter first number: '))
    n2 = int(input('Enter second number: '))
    n3 = int(input('Enter third number : '))
    maximum = maximum3(n1,n2,n3)
    print('maximum number is: ', maximum)

if __name__ =='__main__':
    main()










