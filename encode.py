def encode(password):
    encoded_password = ''
    for i in range(len(password)):
        if password[i] == '0':
            encoded_password += '3'
        elif password[i] == '1':
            encoded_password += '4'
        elif password[i] == '2':
            encoded_password += '5'
        elif password[i] == '3':
            encoded_password += '6'
        elif password[i] == '4':
            encoded_password += '7'
        elif password[i] == '5':
            encoded_password += '8'
        elif password[i] == '6':
            encoded_password += '9'
        elif password[i] == '7':
            encoded_password += '0'
        elif password[i] == '8':
            encoded_password += '1'
        elif password[i] == '9':
            encoded_password += '2'
    return encoded_password


def decode(enc_password):
    res = [int(x) for x in str(enc_password)]
    dec = ""
    for char in res:
        table = {3: '0', 4: '1', 5: '2', 6: '3',
                 7: '4', 8: '5', 9: '6', 0: '7',
                 1: '8', 2: '9'}
        dec += table[char]
    return dec


def main():
    pass_continue = True
    while pass_continue:
        print('''Menu  
    ------------- 
    1. Encode  
    2. Decode  
    3. Quit ''')
        option = int(input("Please enter an option: "))

        if option == 1:
            password = input("Please enter your password to encode: ")
            enc_password = encode(password)
            print("Your password has been encoded and stored!")
        elif option == 2:
            dec_password = decode(enc_password)
            print(f'The encoded password is {enc_password}, and the original password is {dec_password}.')
        elif option == 3:
            pass_continue = False


if __name__ == "__main__":
    main()
