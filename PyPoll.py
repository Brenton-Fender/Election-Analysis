   # Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Intialize a total vote counter and candidate list.
total_votes = 0
# Declare a list of candidates
candidate_options = []
# Declare a dictionary of candidate votes
candidate_votes = {}

# Open the election results and read the file.
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]

        # Add unique candidate names to candidate list.
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

    for candidate_name in candidate_options:
        vote_percentage = float(candidate_votes[candidate_name] / total_votes * 100)
        print(f"{candidate_name} recieved {vote_percentage: .2f}% of the votes.")

#print the candidate votes.
print(candidate_votes)






    