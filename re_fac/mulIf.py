def operations(operator, x, y):
    if operator == 'add':
        return x + y
    elif operator == 'sub':
        return x - y
    elif operator == 'mul':
        return x * y
    elif operator == 'div':
        return x / y


import datetime
start_time = datetime.datetime.now()
print(operations('add',10,24))
end_time = datetime.datetime.now()
print(end_time - start_time)
