print([i for i in range(11,20) if i%2 !=0 ])
from functools import reduce
list1:list = [i for i in range(11,20)]
print(list(map(lambda x:x%2!=0, list1)))