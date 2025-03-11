from typing import Callable  # Import Callable from typing module
from math import modf
def setprofile(func: Callable):
    print(f"Setting profile with function: {func.__name__}")
    return func

print(setprofile(modf))