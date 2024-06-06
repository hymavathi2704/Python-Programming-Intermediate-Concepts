'''
Problem:
Write a recursive function called recursive_sum that takes an integer as a parameter. Return the sum of all integers between 0 and the number passed to recursive_sum.
Expected Output:
If the function call is recursive_sum(5), then the function would return 15
If the function call is recursive_sum(10), then the function would return 55'''

#Code:
def recursive_sum(n):
    # Base case: if n is 0, return 0
    if n == 0:
        return 0
    # Recursive case: return n + recursive_sum(n-1)
    else:
        return n + recursive_sum(n - 1)

# Example usage:
print(recursive_sum(5))   # Output: 15 (0 + 1 + 2 + 3 + 4 + 5 = 15)
print(recursive_sum(10))  # Output: 55 (0 + 1 + 2 + ... + 10 = 55)

