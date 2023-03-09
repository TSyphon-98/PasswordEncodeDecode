password = str(input('Please enter a 8-digit password: '))
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
print(encoded_password)
