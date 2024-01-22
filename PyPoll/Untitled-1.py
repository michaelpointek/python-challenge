""""Pypoll Homwork Tutor Session """

import csv
import os


csv_file_path = r'C:\Users\micha\OneDrive\Documents\GitHub\python-challenge\PyPoll\Resources\election_data.csv'
output_file_path = r'C:\Users\micha\OneDrive\Documents\GitHub\python-challenge\PyPoll\Analysis\election_data_analysis.txt'

total_votes = 0

#candidate Option and vote counter
candidate_options = []
candidate_votes = {}

# Winning Cadidate And Winning Count Tracker
winning_candidate = ""
winning_count = 0


with open(csv_file_path) as election_data:
    reader = csv.reader(election_data)

    header = next(reader)

    for row in reader:
        total_votes = total_votes + 1

        candidate_name = row[2]

        candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

with open(output_file_path, "w") as txt_file:
    
    election_results = (
        f"\n\nElection Results\n"
        f"Total Votes: {total_votes}\n"
        f"---------------------------------"
    )
    print(election_results)

    txt_file.write(election_results)

    for candidate in candidate_votes:

        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes)/float(total_votes) * 100

        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")

        

