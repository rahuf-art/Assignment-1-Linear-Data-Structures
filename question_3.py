def are_rotations(s1, s2):
    return len(s1) == len(s2) and sorted(s1) == sorted(s2)

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
result = are_rotations(string1, string2)
print("Are the strings rotations of each other?", result)
