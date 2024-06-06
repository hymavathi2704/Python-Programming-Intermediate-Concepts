'''
Problem:
Write a function called odds_or_evens that takes a boolean and a list of integers as parameters. If the boolean parameter is True, return a list of only even numbers. If the boolean parameter isFalse, return a list of only odd numbers.
Expected Output:
If the function call is odds_or_evens(True, [13, 22, 8, 31]), the the function would return [22, 8]
If the function call is odds_or_evens(False, [13, 22, 8, 31]), the the function would return [13, 31]'''

#Code:
def odds_or_evens(my_bool, nums):
    """Returns all of the odd or
    even numbers from a list"""
    return_list = []
    for num in nums:
      if my_bool:
          if num % 2 == 0:
              return_list.append(num)
      else:
          if num % 2 != 0:
              return_list.append(num)
                
    return return_list

# Example usage:
print(odds_or_evens(True, [13, 22, 8, 31]))   # Output: [22, 8]
print(odds_or_evens(False, [13, 22, 8, 31]))  # Output: [13, 31]
