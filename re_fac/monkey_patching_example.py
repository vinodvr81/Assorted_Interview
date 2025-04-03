class A(object):
    def __init__(self, num):
        self.num = num
    def __add__(self, other):
        return A(self.num + other.num)

def get_num(self):
    return self.num

if __name__=="__main__":
    foo = A(42)
    A.get_num = get_num
    bar = A(6);
    print(foo.get_num())
    print(bar.get_num())
