import os
print(os.getcwd())
print(os.listdir())
if not os.path.exists("tests"):
    os.mkdir("tests")
# os.chmod("tests",777)