from collections import namedtuple

# Define a namedtuple for representing a point in 2D space
Point = namedtuple('Point', ['x', 'y'])

# Create instances of the namedtuple
p1 = Point(10, 20)
p2 = Point(x=5, y=15)

# Access fields using names
print(p1.x)  # Output: 10
print(p1.y)  # Output: 20

# Access fields using indices (like a regular tuple)
print(p1[0])  # Output: 10
print(p1[1])  # Output: 20

# Check equality
print(p1 == Point(10, 20))  # Output: True
