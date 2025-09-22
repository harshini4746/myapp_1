def is_palindrome(s):
    # Remove spaces and convert to lowercase for uniformity
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

# Example usage
text = input("Enter a string: ")
if is_palindrome(text):
    print("Palindrome")
else:
    print("Not a palindrome")