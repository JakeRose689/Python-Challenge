import os
import csv

file_path=("Resources/election_data.csv")

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

with open(file_path) as data:
    reader=csv.reader(data)
    header=next(reader)

    for row in reader:
        total_votes+=1

        if row[2] not in candidates:
            candidates.append(row[2])

        if row[2]=='Khan':
            khan+=1

        if row[2]=='Correy':
            correy+=1

        if row[2]=='Li':
            li+=1

        if row[2]=="O'Tooley":
            otooley+=1
        
    khan_percent=khan/total_votes
    correy_percent=correy/total_votes
    li_percent=li/total_votes
    otooley_percent=otooley/total_votes

    print(total_votes)
    print(candidates)
    print(khan)
    print(correy)
    print(li)
    print(otooley)