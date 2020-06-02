
d = ['good morning', 'hello', 'chair', 'python', ['music', 'flowers', 'facebook', 'instagram', 'snapchat', ['On my Own', 'monster', 'Words dont come so easily', 'lead me right']], 'Stressed Out', 'Pauver Coeur', 'Reach for Tomorrow', 'mariners song', 'Wonder sleeps here']

m_list = []
for first_inner in d:    
    if type(first_inner) is str:        
        if 'm' in first_inner:
            m_list.append(first_inner)
    elif type(first_inner) is list:
        for second_inner in first_inner:
            if type(second_inner) is str:
                if 'm' in second_inner:
                    m_list.append(second_inner)
            elif type(second_inner) is list:
                for third_inner in second_inner:
                    if type(third_inner) is str:
                        if 'm' in third_inner:
                            m_list.append(third_inner)
    
    
                        
                
        
        