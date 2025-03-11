from typing import Callable

def ref_dec(func: Callable) -> Callable:
    def up_str(s:str)-> str:
        print("before upper")
        print("after upper {0}".format(s.upper()))
        return "success"
    return up_str


@ref_dec
def s_u(st:str):
    return st

print(s_u("telangana"))
