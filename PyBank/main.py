import os
import csv

file_path=("Resources/budget_data.csv")

month_count=0
total_sum=0
average=0
average_list=[]
month_list=[]
increase=0
decrease=0

with open(file_path) as data:
    reader=csv.reader(data)
    header=next(reader)
    first_row=next(reader)
    first_value=int(first_row[1])
    month_count+=1
    total_sum+=first_value

    for row in reader:
        month_count+=1
        total_sum+=int(row[1])
        
        net_change=int(row[1])-first_value
        first_value=int(row[1])
        average_list.append(net_change)
        month_list+=[row[0]]

    average=round(sum(average_list)/month_count, 2)
    increase=max(average_list)
    decrease=min(average_list)
    increase_index=average_list.index(increase)
    decrease_index=average_list.index(decrease)

    Summary=(f"Financial Analysis\n"
    f"---------------------------\n"
    f"Total Months: {month_count}\n"
    f"Total: ${total_sum}\n"
    f"Average Change: ${average}\n"
    f"Greatest Increase in Profits: {month_list[increase_index]} {increase}\n"
    f"Greatest Decrease in Profits: {month_list[decrease_index]} {decrease}")

    print(Summary)
    
output_path=os.path.join("Resources", "summary.txt")

with open(output_path, 'w') as txtfile:
    txtfile.write(Summary)