from collections import defaultdict

# Create a defaultdict with default_factory int
counts = defaultdict(int)

# Access or update keys
counts['a'] += 1  # If 'a' does not exist, it's automatically initialized to 0
counts['b'] += 2

print(counts)  # Output: defaultdict(<class 'int'>, {'a': 1, 'b': 2})
print(dict(counts))

#################################################################################

# Create a defaultdict with default_factory list
grouping = defaultdict(list)

# Add items to keys
grouping['fruits'].append('apple')
grouping['fruits'].append('banana')
grouping['vegetables'].append('carrot')

print(grouping)
# Output: defaultdict(<class 'list'>, {'fruits': ['apple', 'banana'], 'vegetables': ['carrot']})
print(dict(grouping))
############################################################################################

from collections import defaultdict
data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple', 'banana', 'banana', 'banana']
counter = defaultdict(int)
for item in data:
    counter[item] += 1
print(counter)  # Output: defaultdict(<class 'int'>, {'apple': 3, 'banana': 2, 'orange': 1})
print(dict(counter))
print(counter.items())

#############################################################################################

from collections import defaultdict
data = [('fruits', 'apple'), ('fruits', 'banana'), ('vegetables', 'carrot'), ('vegetables', 'tomato')]
groups = defaultdict(list)
for category, item in data:
    groups[category].append(item)
print(groups)
# Output: defaultdict(<class 'list'>, {'fruits': ['apple', 'banana'], 'vegetables': ['carrot']})
print(dict(groups))

##############################################################################################

d = defaultdict(lambda:'default value', foo='bar')
print('d:', d)
print(dict(d))
print(d['bar'])
print(d['xtreme'])