# This program will tell you if the paranthesis string is valid or invalid
# Date : 21st Apr, 2024
# Author : Parmod

def is_balanced(parentheses):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in parentheses:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            print(f"printing values : {mapping[char]}")
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            continue
    return not stack

# Example usage:
parentheses_str = "{[()()]}{}"
if is_balanced(parentheses_str):
    print("\nThe parentheses are balanced\n")
else:
    print("\nThe parentheses are not balanced\n")