
pokemon = {'Trainer1':
          {'normal': {'rattatas':15, 'eevees': 2, 'ditto':1}, 'water': {'magikarps':3}, 'flying': {'zubats':8, 'pidgey': 12}},
          'Trainer2':
          {'normal': {'rattatas':25, 'eevees': 1}, 'water': {'magikarps':7}, 'flying': {'zubats':3, 'pidgey': 15}},
          'Trainer3':
          {'normal': {'rattatas':10, 'eevees': 3, 'ditto':2}, 'water': {'magikarps':2}, 'flying': {'zubats':3, 'pidgey': 20}},
          'Trainer4':
          {'normal': {'rattatas':17, 'eevees': 1}, 'water': {'magikarps':9}, 'flying': {'zubats':12, 'pidgey': 14}}}

r = int()
d = int()
p = int()
for key1,value1 in pokemon.items():
    if type(value1) is dict:
        for key2,value2 in value1.items():
            if type(value2) is dict:
                for key3,value3 in value2.items():
                    if key3 == 'rattatas':
                        r+=value3 
                    if key3 ==   'ditto':
                        d+=value3 
                    if key3 ==   'pidgey':
                        p+=value3                         
                    
            
        