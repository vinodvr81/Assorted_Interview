from functools import reduce

numbers = [1, 2, 3, 4]

# Multiply all numbers in the list
result = reduce(lambda x, y: x * y, numbers)
print(result)  # Outputs: 24
