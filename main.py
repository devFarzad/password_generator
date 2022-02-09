import string,random
while True:
    lengthPassword = input('Please enter Password length :')
    # Check if the input is a number
    if lengthPassword.isdigit():
        # List of characters to use in the password
        chars=string.ascii_letters + string.digits + '!@#$%^&*()'
        # Generate a random password
        password=''.join(random.choice(chars) for item in range(int(lengthPassword)))
        print('Your Password : {}'.format(password))
        while True:
            # Ask user :do you want to continue?
            answer = input('do you want to continue? (y/n)')
            # check answer
            if answer.lower() == 'y':
                break
            elif answer.lower() == 'n':
                print('Thank you')
                exit()
            else:
                print('Please enter y or n')
    else:
        print('Please enter number')            
