
def find_pairs_with_sum(arr, target_sum):
    pairs = []
    seen = set()
    
    for num in arr:
        complement = target_sum - num
        if complement in seen:
            pairs.append((num, complement))
        seen.add(num)
    
    return pairs

# Get user input for the array and the target sum
input_arr = input("Enter the array of integers (space-separated): ").split()
array = [int(num) for num in input_arr]
target = int(input("Enter the target sum: "))

# Find and display the pairs
pairs = find_pairs_with_sum(array, target)

if pairs:
    print("Pairs with the sum of", target, "are:")
    for pair in pairs:
        print(pair[0], "+", pair[1], "=", target)
else:
    print("No pairs found with the sum of", target)
