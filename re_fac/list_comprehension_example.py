
# 1. Below we have provided two lists of numbers, L1 and L2. Using zip and list comprehension,
# create a new list, L3, that sums the two numbers if the number from L1 is greater than 10 and 
#  the number from L2 is less than 5. This can be accomplished in one line of code.

L1 = [1, 5, 2, 16, 32, 3, 54, 8, 100]
L2 = [1, 3, 10, 2, 42, 2, 3, 4, 3]

L3 = [i+j for (i,j) in zip(L1,L2) if i>10 and j<5]

print(L3)