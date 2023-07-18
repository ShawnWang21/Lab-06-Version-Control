#function for encode the password sting passed, shift each digit by 3.
def encode(password):
    encoded = ''
    for i in range(len(password)):
        encoded = encoded + str((int(password[i]) + 3) if (int(password[i])+3 < 10) else (int(password[i]) -7))
    return encoded

if __name__ == '__main__':
    #encoded password can be accessed by encoded_password
    option = None
    encoded_password = ''
    while option != 3:
        print('\nMenu\n'
              '-------------\n'
              '1. Encode\n'
              '2. Decode\n'
              '3. Quit\n')


        option = int(input('Please enter an option: '))
        if option == 1:
            encoded_password = encode(input('Please enter your password to encode: '))
            print('Your password has been encoded and stored!')
        elif option == 2:
            pass
        elif option == 3:
            break
        else:
            continue