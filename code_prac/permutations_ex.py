from itertools import permutations, combinations_with_replacement

def per_ex():
    dum_list: list = []
    perms = permutations('ABC')
    for val in perms:
        dum_list.append("".join(val))
    return tuple(set(dum_list))

print(per_ex())
##################################################################################
def comb_with_rep_ex():
    dum_list:list = []
    comb = combinations_with_replacement(list('ABC'),3)
    for val in comb:
        dum_list.append("".join(val))
    return tuple(set(dum_list))

print(comb_with_rep_ex())