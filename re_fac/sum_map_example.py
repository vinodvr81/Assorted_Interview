def sumSquares(L=list()):
    return sum(list(map(lambda k:k*k,L)))

nums = [3, 2, 2, -1, 1]

print(sumSquares(nums))