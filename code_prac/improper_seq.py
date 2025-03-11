
def is_improper_sequence(s:str) -> bool:
    matching_pairs = {')': '(', '}': '{', ']': '['}
    stack:list = []
    for char in s:
        if char in matching_pairs.values():  # If it's an opening bracket
            stack.append(char)
        elif char in matching_pairs.keys():  # If it's a closing bracket
            if stack:
                if next(reversed(stack)) == matching_pairs[char]:
                    stack.pop()  # Proper matching, remove the opening bracket
                else:
                    return False  # Improper sequence
    # If stack isn't empty, it's also improperly ordered
    return len(stack) == 0


# Example usage
string = "{{}}{{[[[]]}]}"
print(is_improper_sequence(string))  # Output: True
string = '{{}}{{[[[]]]}}'
print(is_improper_sequence(string))