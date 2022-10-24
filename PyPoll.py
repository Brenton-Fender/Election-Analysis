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
# Winning candidate and winning coutn tracker.
winning_candidate = ""
winnning_count = 0
winning_percentage = 0

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

# Save the results to the text file.
with open(file_to_save, 'w') as txt_file:

    election_results = (
        f'\n'
        f'Election Results\n'
        f'-------------------------\n'
        f'Total Votes: {total_votes:,}\n'
        f'-------------------------\n')

    print(election_results, end='')

    # Save the final vot count to the text file.
    txt_file.write(election_results)

    for candidate_name in candidate_options:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes / total_votes * 100)
        candidate_results = (f"{candidate_name}: {vote_percentage: .1f}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
            
        # Determine winning vote count, winning percentage, and candidate.
        if votes > winnning_count and vote_percentage > winning_percentage:
            winnning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f'-------------------------\n'
        f'Winner: {winning_candidate}\n'
        f'Winning Vote Count: {winnning_count: ,}\n'
        f'Winning Percentage: {winning_percentage: .1f}%\n'
        '-------------------------\n')
        
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)
   









    