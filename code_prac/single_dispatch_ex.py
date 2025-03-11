from functools import singledispatch

@singledispatch
def process_data(data):
    raise NotImplementedError("Unsupported type")

@process_data.register
def _(data: int):
    return f"Processing integer: {data}"

@process_data.register
def _(data: str):
    return f"Processing string: {data}"

print(process_data(42))    # Outputs: Processing integer: 42
print(process_data("Hi"))  # Outputs: Processing string: Hi
