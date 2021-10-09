import csv
import os

# Assign a variable to load a file from a path.
file_to_load='Resources\election_results.csv'
# Assign a variable to save the file to a path.
file_to_save = ( "election_analysis.txt")
# Open the election results and read the file.
with open(file_to_load,encoding='utf-8') as election_data:
   
    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)
 
    headers = next(file_reader)
    print(headers)

    for row in file_reader:
        print(row)
     # The total number of votes cast 
     # A complete list of candidates who recieved votes
    # The percentage of votes each candidate won
    # The total number of votes each candidate won
    # The winner of the election based on popular vote


# Using the with statement open the file as a text file.
with open(file_to_save, 'w') as txt_file:

     # Write three counties to the file.
    txt_file.write("Counties in the election\n----------------\nArapahoe\nDenver\nJefferson")
