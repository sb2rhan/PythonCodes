#       To see unicode of symbols

# print(ord('😀'))
# print(chr(128512))

# from string import ascii_letters, ascii_lowercase, ascii_uppercase, digits

# # ready-to-use strings with all letters and numbers
# print(ascii_letters)
# print(ascii_lowercase)
# print(ascii_uppercase)
# print(digits)


#       Formatting strings

# # 1st method (not recommended to use by python)
# print('Sum of that: %d' % 10)

# # 2nd method
# print('Sum {} + {} = {}'.format(10, 4, 14))

# print('Name is {username}, age is {age}'.format(username='Mark', age='22'))

# import math
# # 4 digits after '3.'
# print('PI = {0:.4f}'.format(math.pi))

# # 3rd method
# sum = 15
# print(f'Sum is {sum}')


#       Raw strings(for parsings)

# # python will get t as \t part
# text = '\tell me '
# print(text)
# # to prevent that:
# raw_text = r'\tell me'
# print(raw_text)
# # raw strings turn off functionality
# # of special symbols like \t, \n, etc.


#       String slicing

# text = 'Thus the advantages'
# encodedText = text.encode('utf-8')
# print(encodedText) # works ok with latin letters

# text2 = 'Привет мир!'
# encodedKirill = text2.encode('utf-8')
# print(encodedKirill) # codes kirill letters
# print(encodedKirill.decode('utf-8')) # decodes those symboles


# text = 'i\'m working all day'
# # slices
# print(text[4:11]) # working
# print(text[12:])  # all day
# print(text[:4])   # i'm 

# new_str = 'I' + text[1:] + '!'
# print(new_str)


# print(new_str[::-1])
# # 1st ':' means from the start to the end
# # 2nd ':' means the step after it,
# # which is -1
# print(new_str[::-2])
# # same as previous, but goes with 2 steps


# Block docstrings
# used for documentation

'''
    Lorem ipsum, dolor sit amet consectetur adipisicing
    elit. Sit voluptatem magnam doloribus nostrum
    exercitationem, adipisci maiores facere neque
    aliquid, quisquam qui consectetur doloremque 
'''

print(__doc__) # to print the docs