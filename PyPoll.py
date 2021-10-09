import csv
import os

# Assign a variable to load a file from a path.
file_to_load='Resources\election_results.csv'
# Assign a variable to save the file to a path.
file_to_save = ( "election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0
# Candidate options and candidate votes
candidate_options = []
# Declare the empty dictionary.
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# County options and candidate votes
county_options = []
# Declare the empty dictionary.
county_votes = {}
# Winning Candidate and Winning Count Tracker
winning_county = ""
cwinning_count = 0
cwinning_percentage = 0

# Open the election results and read the file.
with open(file_to_load,encoding='utf-8') as election_data:
   
    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)

    # Count of total votes.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Get the candidate name from each row
        candidate_name = row[2]
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
           # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
        
        # Get the county name from each row
        county_name = row[1]
        # If the county does not match any existing county...
        if county_name not in county_options:
            # Add it to the list of countys.
            county_options.append(county_name)
           # 2. Begin tracking that county's vote count.
            county_votes[county_name] = 0
        # Add a vote to that county's count.
        county_votes[county_name] += 1
        
# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    election_results=(
            f'\nElection Results\n'
            f'---------------------\n'
            f'Total Votes: {total_votes:,}\n'
            f'---------------------\n')
    print(election_results,end='')
    # Save the final vote count to the text file.
    txt_file.write(election_results)


    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100


        # Determine winning vote count and candidate
        # 1. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # 2. If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # 3. Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

        candidate_results=(f"{candidate_name}: {vote_percentage/100:.2%}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)

    division=(
        f"-------------------------\n"
        "-------------------------\n"
        f"Counties turnout\n")
    print(division)
    # Save the winning candidate's results to the text file.
    txt_file.write(division)


    # Determine the percentage of votes for each county by looping through the counts.
    # Iterate through the county list.
    for county_name in county_votes:
        # Retrieve vote count of a county.
        cvotes = county_votes[county_name]
        # Calculate the percentage of votes.
        cvote_percentage = float(cvotes) / float(total_votes) * 100


        # Determine winning vote count and county
        # 1. Determine if the votes are greater than the winning count.
        if (cvotes > cwinning_count) and (cvote_percentage > cwinning_percentage):
            # 2. If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            cwinning_count = cvotes
            cwinning_percentage = cvote_percentage
            # 3. Set the winning_county equal to the county's name.
            winning_county = county_name

        county_results=(f"{county_name}: {cvote_percentage/100:.2%}% ({cvotes:,})\n")
        # Print each county, their voter count, and percentage to the terminal.
        print(county_results)
        #  Save the county results to our text file.
        txt_file.write(county_results)

    winning_county_summary = (
        f"-------------------------\n"
        f"Highest turnout: {winning_county}\n"
        f"{winning_county}'s Vote Count: {cwinning_count:,}\n"
        f"Weight: {cwinning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_county_summary)
    # Save the winning county's results to the text file.
    txt_file.write(winning_county_summary)