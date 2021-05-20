cities = [("Delhi","Bombay"),("Chennai","Kanyakumari"),("Bombay","Goa"),("Jammu","Delhi"),("Goa","Chennai")]

def travel(intputlist:list):
    list_dummy =[]
    list_source = []
    list_dest = []
    
    dummy_dict = {}
    
    
    for i,v in enumerate(list(intputlist)):
        x,y = v
        if x in dummy_dict: 
            dummy_dict[x]+=1
        if y in dummy_dict:
            dummy_dict[y]+=1
        if x not in dummy_dict:
            dummy_dict[x] = 1
        if y not in dummy_dict:
            dummy_dict[y] = 1
    #print(dummy_dict)
    for key,value in dummy_dict.items():
        if value == 1:
            for i,v in enumerate(list(intputlist)):
                x,y = v
                if key == x:
                    list_source.append(x)

                if key == y:
                    list_dest.append(y)
    #print(list_source,list_dest)
    if list_source[0] and list_dest[0]:
        return (list_source[0],list_dest[0])
    else:
        return "ERROR"


print(travel(cities))
