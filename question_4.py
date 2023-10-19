
input_string = input("Enter a string: ")
repeated_chars = set()
non_repeated_chars = []

for char in input_string:
    if char in repeated_chars:
        continue
    if char in non_repeated_chars:
        non_repeated_chars.remove(char)
        repeated_chars.add(char)
    else:
        non_repeated_chars.append(char)

if non_repeated_chars:
    print("The first non-repeated character is:", non_repeated_chars[0])
else:
    print("No non-repeated character found.")
