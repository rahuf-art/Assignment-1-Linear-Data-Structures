def prefix_to_infix(prefix_expression):
    stack = []
    for char in prefix_expression[::-1]:
        if char.isalnum():
            stack.append(char)
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            stack.append(f"({operand1}{char}{operand2})")
    return stack[0]

prefix_expression = input("Enter a prefix expression: ")
infix_expression = prefix_to_infix(prefix_expression)
print("Infix Expression:", infix_expression)
