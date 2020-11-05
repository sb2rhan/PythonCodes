# 'w' mode removes the previous data in the file
f = open('text.txt', 'w')
print(f)
f.write('Hello, World!\n')
f.write('Hi there! ')
f.write('How are you?')
f.close()

file_reader = open('text.txt', 'r')
print(file_reader)
print(file_reader.read()) # reads the whole file
file_reader.close()

file_writer = open('text.txt', 'a+') # will append new text
file_writer.writelines(['Hi there!\n', 'What are you doing?\n'])
file_writer.seek(0) # put cursor to the beginning
data = file_writer.readlines()
file_writer.close()

print('The latest data:', data)


# Context manager
# it automatically closes the file
with open('text.txt', 'r') as opened_file:
    string = opened_file.readline()
    print('First line:', string)

print('Is this file closed now:', opened_file.closed)

# when we read a file encoding might be unsupported, so we can specify encoding:
with open('text.txt', 'r', encoding='utf-8') as opened_file:
    lines = opened_file.readlines()
    print(lines)
