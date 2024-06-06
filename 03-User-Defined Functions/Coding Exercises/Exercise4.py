'''
Problem:
Write a function called best_team that takes a csv file as a parameter. Read the comma-delimited CSV file specified by the variable mlb_data. The CSV file has a list of all of the MLB teams and their performance from the 2019 season. The function should return the team name for the team with the most wins. Important, the CSV file has a header of Tm,Lg,G,W,L, which stands for team name, league, games played, wins, and losses. Below are the file name and file path variables you will need for this exercise.
mlb_data = "student_folder/.exercises/mlb_data.csv"
Expected Output:
The function call should look like this, best_team(file), and the function should return HOU. However, your function will be tested with other CSV files in which different teams will have the highest win total.'''

#Code:
import csv

mlb_data = "student_folder/.exercises/mlb_data.csv"

def best_team(file):
    """Read a CSV of baseball data.
    Return the team name with the most wins"""
    with open(file, "r") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        most_wins = 0
        best_team = ""
        for row in reader:
            if int(row[3]) > most_wins:
                most_wins = int(row[3])
                best_team = row[0]
        return best_team
 # Example usage:
mlb_data = "student_folder/.exercises/mlb_data.csv"
print(best_team(mlb_data))  # Expected output: The team with the most wins, e.g., "HOU"
