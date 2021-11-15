def operations(operator, x, y):
    return {
        'adduser': lambda: x+y,
        'subuser': lambda: x-y,
        'muluser': lambda: x*y,
        'divuser': lambda: x/y,
    }.get(operator, lambda: 'Not a valid operation')()

import datetime
start_time = datetime.datetime.now()
print(operations('adduser',10,24))
end_time = datetime.datetime.now()
print(end_time - start_time)
