from collections import Counter

# Create a Counter from a list
data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
counter = Counter(data)

# View the counts
print(counter)  # Output: Counter({'apple': 3, 'banana': 2, 'orange': 1})

# Access count of a specific element
print(counter['apple'])  # Output: 3
print(counter['grape'])  # Output: 0 (returns 0 if the element is not found)
print(dict(counter))

counter.update(['apple', 'grape', 'banana'])
print(counter)  # Output: Counter({'apple': 4, 'banana': 3, 'orange': 1, 'grape': 1})

print(counter.most_common(1))  # Output: [('apple', 4), ('banana', 3)]
print(counter.most_common(2))  # Output: [('apple', 4), ('banana', 3)]
#########################################################################################
s = 'Vukkalam Rangaswamy Vinod'
c_name = Counter(list(s))
print(c_name.most_common(1))
########################################################################################
s = 'Vukkalam Nevaan Skandaa'
c_name = Counter(s)
print(c_name.most_common(1))
#########################################################################################
c = Counter()
print('Initial :', c)
c.update('abcdaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddd')
print('Sequence:', c)
c.update({'a': 1, 'd': 5})
print('Dict:', c)
print(c.most_common(1))
#######################################################################################
c = Counter('abcdaab')
for letter in 'abcde':
    print('{} : {}'.format(letter, c[letter]))

#######################################################################################
print(help(Counter))