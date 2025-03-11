# Using the walrus operator in a lambda function
lambda_with_walrus = lambda x: (y := x + 1) * 2
print(lambda_with_walrus(5))  # Outputs: 12 (y = 5 + 1 = 6, then 6 * 2 = 12)

lambda_with_walrus_s= lambda x: (y:=  x+ 5) * 2
print(lambda_with_walrus_s(5))  # Outputs: 20 (y = 5 + 5 = 10, then 10 * 2 = 20)