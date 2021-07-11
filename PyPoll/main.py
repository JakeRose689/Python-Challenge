import os
import csv

file_path=("Resources/election_data.csv")

total_votes=0
candidates=[]


with open(file_path) as data:
    reader=csv.reader(data)
    header=next(reader)

    for row in reader:
        total_votes+=1

        if row[2] not in candidates:
            candidates.append(row[2])


    print(total_votes)
    print(candidates)