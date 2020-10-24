# 1
# string = input('Enter string: ')

# string = string.strip()

# lCount = 0
# uCount = 0
# for s in string:
#     if(s.islower()):
#         lCount += 1
#     elif(s.isupper()):
#         uCount += 1

# if (lCount == uCount or lCount > uCount):
#     print(string.lower())
# else:
#     print(string.upper())

# 2

while True:
    a = input('Enter first number: ')
    b = input('Enter second number: ')

    if a.isdigit() and b.isdigit():
        print(f'Sum is {int(a) + int(b)}')
        break
