#Imports dependencies
import os
import csv

#Establishes a path to the CSV file to be analyzed
file_path=("Resources/budget_data.csv")

#Defines initial variables to be manipulated
month_count=0
total_sum=0
average=0
average_list=[]
month_list=[]
increase=0
decrease=0

#Opens CSV file for analysis
with open(file_path) as data:
    reader=csv.reader(data)
    #Advances past the header row in the CSV file
    header=next(reader)
    #Grabs the first value from the first line of data, so a loop for monthly changes can be completed
    first_row=next(reader)
    first_value=int(first_row[1])
    #Corrects the initial values for total number of months and net total of profits and losses
    month_count+=1
    total_sum+=first_value

    #For loop to count the total number of months and net profits and losses
    for row in reader:
        month_count+=1
        total_sum+=int(row[1])
        
        #Creates a list of monthly average changes and each month associated with the change
        net_change=int(row[1])-first_value
        first_value=int(row[1])
        average_list.append(net_change)
        month_list+=[row[0]]

    #Calculates the average monthly change
    average=round(sum(average_list)/month_count, 2)
    #Identifies the maximum gain and loss, assigns index values for each to new variables
    increase=max(average_list)
    decrease=min(average_list)
    increase_index=average_list.index(increase)
    decrease_index=average_list.index(decrease)

    #Creates long f statement to print to terminal in the next step
    Summary=(f"Financial Analysis\n"
    f"---------------------------\n"
    f"Total Months: {month_count}\n"
    f"Total: ${total_sum}\n"
    f"Average Change: ${average}\n"
    f"Greatest Increase in Profits: {month_list[increase_index]} {increase}\n"
    f"Greatest Decrease in Profits: {month_list[decrease_index]} {decrease}")

    #Prints required info to terminal
    print(Summary)
    
#Defines the path to join for the text output
output_path=os.path.join("Analysis", "summary.txt")

#Opens and writes the output to text file
with open(output_path, 'w') as txtfile:
    txtfile.write(Summary)