def are_brackets_balanced(code):
    stack = []
    bracket_pairs = {')': '(', '}': '{', ']': '[', '>': '<'}
    for char in code:
        if char in bracket_pairs.values():
            stack.append(char)
        elif char in bracket_pairs.keys():
            if not stack or stack[-1] != bracket_pairs[char]:
                return False
            stack.pop()
    return not stack

code = input("Enter the code snippet: ")
if are_brackets_balanced(code):
    print("All brackets are properly closed.")
else:
    print("Not all brackets are properly closed.")
