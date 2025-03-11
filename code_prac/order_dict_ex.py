import collections
print('Regular dictionary:')
dd: dict = {}
dd['a'] = 'A'
dd['b'] = 'B'
dd['c'] = 'C'
for k, v in dd.items():
    print(k, v)
print('unorderd dict is {0}'.format(dd))
print('\nOrderedDict:')
d = collections.OrderedDict()
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
for k, v in d.items():
    print(k, v)
print('\nOrderedDict: {0}'.format(d))
print('\nDict form: {0}'.format(dict(d)))
print('#'*49)
from string import ascii_lowercase
print(dict(zip(ascii_lowercase, range(6))))
print('#'*49)
print(collections.OrderedDict(zip(ascii_lowercase, range(7))))