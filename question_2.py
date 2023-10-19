def reverse_array_in_place(arr):
    n = len(arr)
    for i in range(n // 2):
        arr[i], arr[n - 1 - i] = arr[n - 1 - i], arr[i]

# Get user input for the array
input_arr = input("Enter the array of elements (space-separated): ").split()
array = [int(num) for num in input_arr]

reverse_array_in_place(array)
print("Reversed array:", array)
