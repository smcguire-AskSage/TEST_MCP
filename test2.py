# This program checks if a given string is a palindrome

def is_palindrome(s):
    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Example usage
example_string = "A man a plan a canal Panama"
if is_palindrome(example_string):
    print(f"'{example_string}' is a palindrome.")
else:
    print(f"'{example_string}' is not a palindrome.")
