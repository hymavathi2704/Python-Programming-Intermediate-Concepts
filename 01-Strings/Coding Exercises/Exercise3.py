'''
Problem:
Write a program that accepts input from the user. Create another string that contains either a u, l, or - for each character of the original string. Use u when the character is uppercase, and use l when the character is lowercase. If the character is neither uppercase or lowercase, use -. Print the second string. Important, do not put a prompt when asking for user input. Just use input(). Adding a prompt will cause your program to not pass the tests.
Expected Output:
If the user inputs cat, then the output will be:
cat
lll
If the user inputs HouSE, then the output will be:
HouSE
ulluu'''

#Code:
txt = input()
second_string = ""
for char in txt:
    if char.islower():
        second_string += "l"
    elif char.isupper():
        second_string += "u"
    else:
        second_string += "-"

print(second_string)