# Shawn Wang function for encode the password sting passed, shift each digit up by 3.
def encode(password):
    encoded = ''
    for i in range(len(password)):
        encoded = encoded + str((int(password[i]) + 3) if (int(password[i]) + 3 < 10) else (int(password[i]) - 7))
    return encoded


def decode(password):  # decode function in similar style to encode function
    decoded = ''
    for i in range(len(password)):
        decoded = decoded + str((int(password[i]) - 3)
                                if (int(password[i]) - 3 > -1)
                                else (int(password[i]) + 7))
    return decoded


if __name__ == '__main__':
    # encoded password can be accessed by encoded_password
    option = None
    encoded_password = ''
    while option != 3:
        # display menu and get option
        print('\nMenu\n'
              '-------------\n'
              '1. Encode\n'
              '2. Decode\n'
              '3. Quit\n')

        option = int(input('Please enter an option: '))
        if option == 1:
            encoded_password = encode(input('Please enter your password to encode: '))
            print('Your password has been encoded and stored!')
        elif option == 2:  # Decode option
            decoded_password = decode(encoded_password)
            print('The encoded password is ' + encoded_password + ', and the original password is ' + decoded_password)
        elif option == 3:  # Exit program
            break
        else:
            continue
