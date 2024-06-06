'''
Problem:
Write a function called avg that takes two parameters. Return the average of these two parameters. If the parameters are not numbers, return the string, Please use two numbers as parameters.
Expected Output:
If the function call is avg(10,25), then the function would return 17.5
If the function call is avg(10, "cat"), then the function would return Please use two numbers as parameters'''

#Code"
def avg(n1, n2):
    """Return average of two numbers
    Return a message is a non-number is passed"""
    try:
      return(n1 + n2) / 2
    except TypeError:
      return("Please use two numbers as parameters")