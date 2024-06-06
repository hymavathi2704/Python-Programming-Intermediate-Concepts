'''
Problem:
Write a recursive function called list_sum that takes a list of numbers as a parameter. Return the sum of all of the numbers in the list. Hint, the slice operator will be helpful in solving this problem.
Expected Output:
If the function call is list_sum([1, 2, 3, 4, 5]), then the function would return 15
If the function call is list_sum([10, 12.5, 10, 7]), then the function would return 39.5
'''

#Code:
def list_sum(lst):
    # Base case: if the list is empty, return 0
    if not lst:
        return 0
    # Recursive case: return the first element plus list_sum of the rest of the list
    else:
        return lst[0] + list_sum(lst[1:])

# Example usage:
print(list_sum([1, 2, 3, 4, 5]))       # Output: 15 (1 + 2 + 3 + 4 + 5 = 15)
print(list_sum([10, 12.5, 10, 7]))     # Output: 39.5 (10 + 12.5 + 10 + 7 = 39.5)
