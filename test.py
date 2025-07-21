def is_palindrome(s):
    """
    Determine if a given string is a palindrome.

    Args:
    s (str): The string to check.

    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    # Remove spaces and convert to lowercase for uniformity
    cleaned_string = ''.join(s.split()).lower()
    
    # Compare the string to its reverse
    return cleaned_string == cleaned_string[::-1]

# Example usage
print(is_palindrome("A man a plan a canal Panama"))  # Output: True
print(is_palindrome("Hello"))  # Output: False
