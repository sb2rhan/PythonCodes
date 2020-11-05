import os


print(dir(os.path.sys.path))

# junk code not recommended to do
os.path.sys.path.insert(0, 'D:\\Projects\\PythonCodes\\ITStepTutorials\\Modules')

from converter import emoji_converter

if __name__ == "__main__":
    print(emoji_converter.emoji_convert('smile'))
