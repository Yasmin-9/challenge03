#importing modules 
import os
import csv
from pathlib import Path

#setting a path for the file
file_path="C:/Bootcamp/ALLHW/challenge03/Starter_Code/PyPoll/Resources/election_data.csv"

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
        if current_candidate not in candidates:
            candidates.append(current_candidate)
            candidates_votes[current_candidate]=0
        candidates_votes[current_candidate]=candidates_votes[current_candidate]+1
    #print total votes
    print("Total votes: ", total_votes) 
    #print the list of candidates
    #print(candidates) (not needed) 
    #print the number of candidates votes
    #print(candidates_votes)(not needed)

    for candidate in candidates_votes:
        current_vote=candidates_votes[candidate]
        percentage = current_vote/total_votes *100
        if current_vote > winner:
            winner = current_vote
            winner_name = candidate
        #print the list of candidate, percentage and their current vote)
        #print(candidate,percentage, current_vote)
        print(f"{candidate}, {percentage:.3f}, ({current_vote})")
    #print the winner name
    #print(winner_name, winner)
    print("Winnner: ", winner_name)
        
    
txt_file = "C:/Bootcamp/ALLHW/challenge03/Starter_Code/PyPoll/analysis.txt"

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

    

