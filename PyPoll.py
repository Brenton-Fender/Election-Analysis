   # Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1 Intialize a total vote counter and candidate list.
total_votes = 0
candidate_options = []

# Open the election results and read the file.
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        
        # 2. Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]

        # Add unique candidate names to candidate list.
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

#print the candidate list.
print(candidate_options)






    