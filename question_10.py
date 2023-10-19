
stack = []
n = int(input("Enter the number of elements in the stack: "))

for _ in range(n):
    element = int(input("Enter the element: "))
    stack.append(element)

min_element = min(stack)
print("Smallest element in the stack is:", min_element)
