'''
Problem:
Write a recursive function called bunny_ears that takes the number of bunnies (an integer) as a parameter. Return the number of bunny ears (2 per bunny). Do not use multiplication; instead use addition.
Expected Output:
If the function call is bunny_ears(8), then the function would return 16
If the function call is bunny_ears(0), then the function would return 0
'''

#Code:
def bunny_ears(bunnies):
    # Base case: if there are no bunnies, return 0
    if bunnies == 0:
        return 0
    # Recursive case: return 2 (ears per bunny) + bunny_ears for one less bunny
    else:
        return 2 + bunny_ears(bunnies - 1)

# Example usage:
print(bunny_ears(8))   # Output: 16 (8 bunnies * 2 ears per bunny = 16)
print(bunny_ears(0))   # Output: 0 (0 bunnies, hence 0 ears)

