'''
Problem:
Write a program that reads a text file and returns the number of lines as well as the total number of characters in the file.
Expected Output:
The first two lines of your code must look like this:
import sys

test_file = sys.argv[1]
This allows for different text files to be sent to your program for testing. Hint, to open the file use with open(test_file, "r".... The TRY IT button below will send a test file to your program. You should see the following output:
4 lines
231 characters'''

#Code:
import sys

test_file = sys.argv[1]

line_count = 0
char_count = 0

with open(test_file, "r") as input_file:
    line = input_file.readline()
    while line != "":
        line_count += 1
        char_count += len(line)
        line = input_file.readline()

print("{} lines".format(line_count))
print("{} characters".format(char_count))