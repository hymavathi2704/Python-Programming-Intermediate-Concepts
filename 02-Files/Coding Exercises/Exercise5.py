'''
Problem
Write a program that reads a comma delimited CSV file and prints all of the cities which reside in the Southern Hemisphere. Note, any latitude with a negative value is south of the equator.
Expected Output
The CSV file will look something like the one below. Note, there will be a row with header titles.
City	Country	Latitude	Longitude
Beijing	China	39	116
Perth	Australia	-57	115
Port Moresby	Papua New Guinea	-25	147
Tokyo	Japan	35	139
The first two lines of your code must look like this:
import sys, csv

test_file = sys.argv[1]
This allows for different text files to be sent to your program for testing. Hint, to open the file use with open(test_file, "r".... The TRY IT button below will send a test file to your program. You should see the following output:
The following cities are in the Southern Hemisphere: Perth, Port Moresby.'''

#Code:
import sys, csv

test_file = sys.argv[1]
cities = []

with open(test_file, "r") as input_file:
    reader = csv.reader(input_file)
    next(reader)
    for city, country, latitude, longitude in reader:
        if int(latitude) < 0:
            cities.append(city)
            
print("The following cities are in the Southern Hemisphere: ", end="")
for city in cities:
    if city == cities[-1]:
        print(city + ".")
    else:
        print(city, end=", ")