'''
Problem:
Write a program that takes input from a user. Print the first half of the string on one line, and the second half on another. In the case of a string that has an odd number of characters, the second line will have the extra character. Important, do not put a prompt when asking for user input. Just use input(). Adding a prompt will cause your program to not pass the tests.
Expected Output:
If the user inputs home, the output will be:
ho
me
If the user inputs hooray Python, the output will be:
hooray
 Python'''

#Code:
txt = input()
midpoint = len(txt) // 2
first_half = txt[:midpoint]
second_half = txt[midpoint:]
print(first_half)
print(second_half)