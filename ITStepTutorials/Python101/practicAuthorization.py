print('Authorization admin\n')

login = input('Enter your login: ')
password = input('Enter your password: ')

if login == 'admin' and password == '1q233jce':
    print('Welcome to the admin panel!\n')
elif not login == 'admin':
    print('Incorrect login')
else:
    print('Incorrect password')
