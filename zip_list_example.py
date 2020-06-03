
# Use zip and map or a list comprehension to make a list consisting
# the maximum value for each position. For L1, L2, and L3, you would
# end up with a list [4, 5, 3, 5].

L1 = [1, 2, 3, 4]
L2 = [4, 3, 2, 3]
L3 = [0, 5, 0, 5]

maxs = list(map(lambda k:max(k),zip(L1,L2,L3)))

print(maxs)