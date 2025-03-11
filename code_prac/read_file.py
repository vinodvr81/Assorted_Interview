def read_file(filename:str):
    with open(filename, "r") as fh:
        for i in fh.readlines():
            yield i.strip()

for i in read_file("test1.txt"):
    print(i)