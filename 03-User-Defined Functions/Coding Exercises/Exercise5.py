'''
Problem:
Write a function called is_palindrome that takes a string as a parameter. The function will return True if the string is a palindrome (is the same forward and backward). The function will return False if the string is not a palindrome.
Expected Output:
If the function call is is_palindrome("level"), the the function would return True
If the function call is is_palindrome("house"), the the function would return False'''

#Code:
def is_palindrome(string):
    reversed_string= ""
    position = len(string) - 1
    while position >= 0:
        reversed_string += string[position]
        position -= 1
    if string == reversed_string:
        return True
    else:
        return False
    
# Example usage:
print(is_palindrome("level"))   # Output: True
print(is_palindrome("house"))   # Output: False
