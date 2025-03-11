import re

def split_alpha_numeric(s_str:str):
    # Find all sequences of either alphabetic or numeric characters
    parts = re.findall(r'[-,+]+|\d+|[-,+]+]|[a-zA-Z]+| \d+', s_str)

    return tuple(parts)

# Example usage
s = "325134134-3642346abc123def456ghi789"
result = split_alpha_numeric(s)
print(result)

s = "325134134+3642346abc123def456ghi789"
result = split_alpha_numeric(s)
print(result)

s = "-325134134+3642346abc123def456ghi789"
result = split_alpha_numeric(s)
print(result)