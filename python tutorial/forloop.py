def summation(n):

    total = 0
    for count in range (1 , n+1):
        total += count
    return total
    

def main():
    n = int(input('Enter number of term : '))
    total = summation(n)
    print('the sum of first' , n , 'positive integer: ', total)


if __name__ =='__main__':
    main()






