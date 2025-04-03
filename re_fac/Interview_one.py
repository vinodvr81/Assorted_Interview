cities = [("Delhi","Bombay"),("Chennai","Kanyakumari"),("Bombay","Goa"),("Jammu","Delhi"),("Goa","Chennai")]

def travel(intputlist:list):
    list_dummy =[]
    list_source = []
    list_dest = []
    
    dummy_dict = {}
    
    
    for i,v in enumerate(list(intputlist)):
        x,y = v
        list_dummy.append(x)
        list_dummy.append(y)
    #print(list_dummy)
    for i,v in enumerate(list_dummy):
        if v in dummy_dict:
            dummy_dict[v]+=1
        else:
            dummy_dict[v] = 1
    #print(dummy_dict)
    for key,value in dummy_dict.items():
        if value == 1:
            for i,v in enumerate(list(intputlist)):
                x,y = v
                if key == x:
                    list_source.append(x)

                if key == y:
                    list_dest.append(y)

    if list_source[0] and list_dest[0]:
        return (list_source[0],list_dest[0])
    else:
        return "ERROR"


print(travel(cities))
