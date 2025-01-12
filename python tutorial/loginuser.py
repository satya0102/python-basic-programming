def authenticateUser(password):
    if password == 'satya' :
        message = 'login successful  !! \n  welcome to system'
    if password != 'satya':
        message = 'missmatch password try again! '
    return message 

def main():
    print('  LOGIN SYSTEM ')
    print("=================")
    password = input('enter password: ')
    message = authenticateUser(password)
    print(message)

if __name__ =='__main__':
    main()     












