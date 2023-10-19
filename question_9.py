def reverse_stack(stack):
    if not stack:
        return stack

    reversed_stack = []
    while stack:
        item = stack.pop()
        reversed_stack.append(item)

    return reversed_stack

# Get user input for the stack
stack = input("Enter elements of the stack (space-separated): ").split()
stack = [int(item) for item in stack]

reversed_stack = reverse_stack(stack)
print("Reversed Stack:", reversed_stack)
