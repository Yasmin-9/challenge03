#importing modules 
import os
import csv
from pathlib import Path

#setting a path for the file
file_path="C:/Bootcamp/ALLHW/python-challenge/PyPoll/Resources/election_data.csv"

#setting empty lists
total_votes=0
candidates = []
candidates_votes={}
winner = 0

#opening the file
with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #reading the header row first   
    header = next(csvreader)

    #iterating through the rows
    for row in csvreader:
        #looping through the rows + 1 to obtain the total votes
        total_votes=total_votes+1
        current_candidate=row[2]
        #obtaining the list of candidates, to eliminate duplicates
        if current_candidate not in candidates:
            candidates.append(current_candidate)
            candidates_votes[current_candidate]=0
        candidates_votes[current_candidate]=candidates_votes[current_candidate]+1
    #print total votes
    print("Total votes: ", total_votes) 

#determining the number of votes and percentage, using candidates_votes dictionary
    #looping through the dictionary to obtain vote count for each candidate
    for candidate in candidates_votes:
        current_vote=candidates_votes[candidate]
        #calculating vote % 
        percentage = current_vote/total_votes *100
        #determining the candidate with the highest vote count
        if current_vote > winner:
            winner = current_vote
            winner_name = candidate
        #print the list of candidate, percentage and their current vote)
        print(f"{candidate}, {percentage:.3f}, ({current_vote})")
    #print the winner name
    print("Winnner: ", winner_name)
        

# writing analysis text file    
txt_file = "C:/Bootcamp/ALLHW/python-challenge/PyPoll/analysis.txt"

with open (txt_file,"w") as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total votes: {total_votes}\n")
    file.write("-------------------------\n")
    for candidate in candidates_votes:
        file.write(f"{candidate}, {percentage:.3f}, ({current_vote})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner_name}\n")
    file.write("-------------------------\n")

    

