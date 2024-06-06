'''
Problem:
Write a recursive function called reverse_string that takes a string as a parameter. Return the string in reverse order. Hint, the slice operator will be helpful when solving this problem.
Expected Output:
If the function call is reverse_string("cat"), then the function would return tac
If the function call is reverse_string("house"), then the function would return esuoh'''

#Code:
def reverse_string(s):
    # Base case: if the string is empty or has one character, return itself
    if len(s) <= 1:
        return s
    # Recursive case: return the last character + reverse_string of the rest of the string
    else:
        return s[-1] + reverse_string(s[:-1])

# Example usage:
print(reverse_string("cat"))    # Output: tac
print(reverse_string("house"))  # Output: esuoh
