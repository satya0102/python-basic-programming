def main():
    total =0
    number = input('Enter a number: ')
    while number != '':
        total+= int(number)
        number = input('Enter a number: ')
    print('Sum of all input number is: ', total)


if __name__ =='__main__':
    main()



