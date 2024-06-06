'''
Problem:
Write a program that captures text from the user. Print the user string as many times as its length. Print as many lines of this as the length of the user input. Important, do not put a prompt when asking for user input. Just use input(). Adding a prompt will cause your program to not pass the tests.
Expected Output:
If the user types cat then the program will print:
catcatcat
catcatcat
catcatcat
If the user types tree then the program will print:
treetreetreetree
treetreetreetree
treetreetreetree
treetreetreetree'''

#Code:
txt = input()
for i in range(len(txt)):
    print(txt * len(txt))