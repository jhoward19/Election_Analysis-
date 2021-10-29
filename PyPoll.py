# Add our dependencies.
import csv

# Assign a variable to load a file from a path.
file_to_load = "election_results.csv"

# Assign a variable to save the file to a path.
file_to_save = "election_analysis.txt"

# Using the with statement open the file as a text file.
outfile = open(file_to_save, "w")

# Open the election results and read the file.
election_data = open(file_to_load, "r")
#To do:perform analysis
print(election_data)

# To do: read and analyze the data here.
file_reader = csv.reader(election_data)
# Read and print the header row.
headers = next(file_reader)
print(headers)