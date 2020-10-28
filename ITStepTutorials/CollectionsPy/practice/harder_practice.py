import re


file_ = open('ITStepTutorials\\CollectionsPy\\practice\\words.txt', 'r')
file_content = file_.read()

pattern = re.compile(r'\s+')
matched = pattern.split(file_content)

matched_set = set(matched)
word_count = {}

for item in matched:
    word_count[item] = matched.count(item)
print(word_count)
