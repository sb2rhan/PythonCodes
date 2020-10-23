import emojis # module for working with emojis
import re


print(emojis.encode(':heart: :snake:'))

emojis_dict = {
    'smile': ':smile:',
    'expressionless': ':expressionless:',
    'smiling_imp': ':smiling_imp:',
    'snake': ':snake:'
}

def emoji_convert(string):
    pattern = re.compile(r'\s')
    words = pattern.split(string)
    result = ''
    for word in words:
        result += ' ' + emojis.encode(emojis_dict.get(word, word))
    return result
