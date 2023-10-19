def is_palindrome(s, start, end):
    if start >= end:
        return True
    if s[start] != s[end]:
        return False
    return is_palindrome(s, start + 1, end - 1)

user_input = input("Enter a string: ")
if is_palindrome(user_input, 0, len(user_input) - 1):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
