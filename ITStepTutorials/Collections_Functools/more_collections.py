# Chain map
# it literally means the chain of many maps
from collections import ChainMap

cake = {'type': 'sweet', 'pic': '🎂'}
coffee = {'type': 'drink', 'pic': '☕'}

chainmap = ChainMap(cake, coffee)

print(chainmap)
print(chainmap['type'])
print(chainmap['pic'])


# Counter
# it is used for counting elements in collections
# so we don't need to create variable named 'counter = 0'
# and count elements manually
from collections import Counter

string = 'superstringu'

count_dic = Counter(string)
# also, it sorts by frequency
print(count_dic)

# to see all elements of string in count_dic
print(list(count_dic.elements()))

# to see count of specific element:
print('Count of s is here', count_dic['s'])

# to see most frequent elements:
print('The top 3 elements', count_dic.most_common(3)) # 3 means top 3 elements (you can pass any integer)


# Default dictionary
from collections import defaultdict


sentence = 'The red fox ran over the tree in the park'
words = sentence.split()

d = defaultdict(int) # int is type of value, so it automatically inits values by 0
for word in words:
    d[word] += 1

print(d)


# Deque
# collection that has abilities of stacks and queues
# so it is optimised list-like collection
from collections import deque
import string

d = deque(string.ascii_lowercase)

for letter in d:
    print(letter, end=' ')

# Some methods

d.append('bond') # adds to the end
print(d)

d.appendleft('james') # adds to the start
print(d)

d.rotate(2) # last 2 elements are moved to the start
print(d)


# Named tuple
# used for creation of tuple-like objects like classes
from collections import namedtuple

Human = namedtuple('Human', ['fullname', 'age'])

jack = Human(fullname='Jack Brown', age=19)
print(jack)
print('Age of', jack.fullname, 'is', jack.age)


# Ordered dictionary
# keeps keys of dictionary ordered
# even when adding new pairs and deleting
from collections import OrderedDict

d = {'apple': 3, 'peach': 2, 'melon': 2}

ord_d = OrderedDict(sorted(d.items()))
print(ord_d)
