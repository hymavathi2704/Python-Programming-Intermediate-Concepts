'''
Problem:
Write a program that reads a comma delimited CSV file with four columns and returns the average of each column in the file.
Expected Output:
The first two lines of your code must look like this:
import sys

test_file = sys.argv[1]
This allows for different text files to be sent to your program for testing. Hint, to open the file use with open(test_file, "r".... The TRY IT button below will send a test file to your program. You should see the following output:
10.0 8.0 6.0 20.0'''

#Code:
import sys, csv

test_file = sys.argv[1]

total1 = 0
total2 = 0
total3 = 0
total4 = 0
row_count = 0

with open(test_file, "r") as input_file:
    reader = csv.reader(input_file)
    for num1, num2, num3, num4 in reader:
        row_count += 1
        total1 += int(num1)
        total2 += int(num2)
        total3 += int(num3)
        total4 += int(num4)

print("{} {} {} {}".format(total1/row_count, total2/row_count, total3/row_count, total4/row_count))