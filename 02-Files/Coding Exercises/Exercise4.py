'''
Problem:
Write a program that reads a tab delimited CSV file and prints the name of the oldest person in the file.
Expected Output:
The CSV file will look something like the one below. Note, there will be a row with header titles.
Name	Age	Career
Peter	38	Doctor
Paul	41	Lawyer
Mary	32	Systems Engineer
The first two lines of your code must look like this:
import sys, csv

test_file = sys.argv[1]
This allows for different text files to be sent to your program for testing. Hint, to open the file use with open(test_file, "r".... The TRY IT button below will send a test file to your program. You should see the following output:
The oldest person is Paul.'''

#Code:
import sys, csv

test_file = sys.argv[1]
oldest_age = 0
oldest_name = ""

with open(test_file, "r") as input_file:
    reader = csv.reader(input_file, delimiter="\t")
    next(reader)
    for name, age, career in reader:
        if int(age) > oldest_age:
            oldest_age = int(age)
            oldest_name = name
            
print("The oldest person is {}.".format(oldest_name))