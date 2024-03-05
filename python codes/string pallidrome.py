import re

def is_palindrome(s):
    s = re.sub(r'\W+', '', s)  # Remove non-alphanumeric characters
    s = s.lower()  # Convert to lowercase
    return s == s[::-1]  # Check if string is equal to its reverse

# Test cases
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))  # False
print(is_palindrome("A man a plan a canal Panama"))  # True