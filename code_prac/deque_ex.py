from collections import deque



# Create a deque from a list
dqq = deque([1, 2, 3, 5])
print(dqq)  # Output: deque([1, 2, 3])


# Append to the right
dqq.append(4)  # deque([1, 2, 3, 4])
print(dqq)
# Append to the left
dqq.appendleft(0)  # deque([0, 1, 2, 3, 4])
print(dqq)
# Pop from the right
dqq.pop()  # Output: 4, deque([0, 1, 2, 3])
print(dqq)
# Pop from the left
dqq.popleft()  # Output: 0, deque([1, 2, 3])
print(dqq)

##################################################################################

d = deque(range(10))
print('Normal:', d)
d = deque(range(10))
d.rotate(2)
print('Right rotation:', d)
d = deque(range(10))
d.rotate(-2)
print('Left rotation:', d)