import csv

csv_file_path = r'C:\Users\micha\OneDrive\Documents\GitHub\python-challenge\PyPoll\Resources\election_data.csv'
output_file_path = r'C:\Users\micha\OneDrive\Documents\GitHub\python-challenge\PyPoll\Analysis\election_data_analysis.txt'

# initialize variables to store data
# total_votes = 0
# candidates = []
# vote_share = []
# votes_by_candidate = []
# winner = 0

# open and read csv file
with open(csv_file_path, "r") as file:
    lines = file.readlines()
    header = lines[0].strip().split(",")
    data = [dict(zip(header,line.strip().split(","))) for line in lines[1:]]

total_votes = len(data)

candidates = set(entry["Candidate"] for entry in data)

candidate_votes = {}
for entry in data:
    candidate = entry["Candidate"]
    candidate_votes[candidate] = candidate_votes.get(candidate, 0) + 1

percentage_votes = {candidate: votes / total_votes * 100 for candidate, votes in candidate_votes.items()}


winner = max(candidate_votes, key=candidate_votes.get)

print("Election Results")
print("-------------------")
print(f"Total Votes: {total_votes}")
print("-------------------")
for candidate in candidates:
    print(f"{candidate}: {percentage_votes[candidate]:.3f}% ({candidate_votes[candidate]})")
print("-------------------")
print(f"Winner: {winner}")
print("-------------------")

with open(output_file_path, "w") as output_file:
    output_file.write("Election Results\n")
    output_file.write("-------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("-------------------\n")
    for candidate in candidates:
        output_file.write(f"{candidate}: {percentage_votes[candidate]:.3f}% ({candidate_votes[candidate]})\n")
    output_file.write("-------------------\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("-------------------\n")
