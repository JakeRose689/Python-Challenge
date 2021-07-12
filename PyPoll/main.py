#Imports dependencies
import os
import csv

#Establishes a path to the CSV file to be analyzed
file_path=("Resources/election_data.csv")

#Defines initial variables to be manipulated
total_votes=0
candidates=[]
khan=0
correy=0
li=0
otooley=0
khan_percent=0
correy_percent=0
li_percent=0
otooley_percent=0

#Opens CSV file for analysis
with open(file_path) as data:
    reader=csv.reader(data)
    header=next(reader)

    #Begins for loop and calculates total votes from the CSV data
    for row in reader:
        total_votes+=1
    
    #print(total_votes)

        if row[2] not in candidates:
            candidates.append(row[2])

    #print(candidates)

        #Calculates the total number of votes per candidate
        if row[2]=='Khan':
            khan+=1

        if row[2]=='Correy':
            correy+=1

        if row[2]=='Li':
            li+=1

        if row[2]=="O'Tooley":
            otooley+=1
        
    #Calculates the percentage of votes each candidate received 
    khan_percent=round(((khan/total_votes)*100), 4)
    correy_percent=round(((correy/total_votes)*100), 4)
    li_percent=round(((li/total_votes)*100), 4)
    otooley_percent=round(((otooley/total_votes)*100), 4)

    #Assigns the 'winner' to the max of all candidate values
    winner=max(khan, correy, li, otooley)

    #Assigns the name of the candidate as a string value for the winner of the vote
    if winner == khan:
        winner_name = 'Khan'
    elif winner == correy:
        winner_name = 'Correy'
    elif winner == li:
        winner_name = 'Li'
    else:
        winner_name = "O'Tooley"

    #Creates long f statement to print to terminal in the next step
    summary=(f"Election Results\n"
    f"-------------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------------\n"
    f"{candidates[0]}: {khan_percent}% ({khan})\n"
    f"{candidates[1]}: {correy_percent}% ({correy})\n"
    f"{candidates[2]}: {li_percent}% ({li})\n"
    f"{candidates[3]}: {otooley_percent}% ({otooley})\n"
    f"-------------------------------\n"
    f"Winner: {winner_name}")

    #Prints required info to terminal
    print(summary)

#Defines the path to join for the text output
output_path=os.path.join("Analysis", "summary.txt")

#Opens and writes the output to text file
with open(output_path, 'w') as txtfile:
    txtfile.write(summary)