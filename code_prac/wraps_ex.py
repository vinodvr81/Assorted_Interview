from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Before the function call")
        result = func(*args, **kwargs)
        print("After the function call")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    """Greets a person by name."""
    print(f"Hello, {name}!")

say_hello("Alice")
print(say_hello.__name__)  # Outputs: say_hello
print(say_hello.__doc__)   # Outputs: Greets a person by name.
