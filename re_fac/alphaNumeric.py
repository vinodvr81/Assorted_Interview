import re
import pdb
def mychoice(s:str):
    #pdb.set_trace()
    l1 = list()
    for x in re.findall(r'[A-Za-z]+|\d+', s):
        if  x.isdigit():
            l1.append(int(x))
        else:
            l1.append(x)
    return l1
     

l = ['AL13', 'AL3', 'AA14', 'AA4']

print(sorted(l,key=mychoice,reverse=True)) 