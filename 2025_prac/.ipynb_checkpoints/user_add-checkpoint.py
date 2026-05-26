
def user_add(list1: list, len_tuple:int) -> list:
    ret_list: list = []
    if isinstance(len_tuple, int) and len_tuple == 2:
        for i in list1:
            for j in list1:
                if isinstance(i,int) and isinstance(j,int) and i+j == 6:
                    ret_list.append((i,j))
                if isinstance(i,int) and isinstance(j,int) and (j,i) in ret_list:
                    ret_list.remove((j,i))
    return ret_list
list1: list = [2,1,5,-1,7,4]
print(user_add(list1, 2))
