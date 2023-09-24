#import the modules
import os
import csv
from pathlib import Path

#setting a path for the file
file_path="C:/Bootcamp/ALLHW/challenge03/Starter_Code/PyBank/Resources/budget_data.csv"

#setting empty lists
months = []
profit = []
monthly_change = []

#opening the file
with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

#reading the header row first   
    header = next(csvreader)

#iterating through the rows
    for row in csvreader:
    #appending the rows in file to their corresponding lists
        months.append(row[0])
        profit.append(int(row[1]))

#calculate the change in 'profit/losses' over the entire period, then calculate average
    #calculate the chenge in 'profit/losses'
    for i in range(len(profit)-1):
        monthly_change.append(profit[i+1]-profit[i])


#calculating the max and min profit change 
max_increase = max(monthly_change)
max_decrease = min(monthly_change)

#determining the month of the max_increase and max_decrease, the +1 is to indicate the next month
max_increase_month = monthly_change.index(max_increase)+1
max_decrease_month = monthly_change.index(max_decrease)+1


#print statements
print(f"Total Months: {len(months)}")
print(f"Total Profit/Losses: ${sum(profit)}")
print(f"Average change: ${round(sum(monthly_change)/len(monthly_change),2)}")
print(f"Greatest Increase in Profits: {months[max_increase_month]} (${str(max_increase)})")
print(f"Greatest Decrease in Profits : {months[max_decrease_month]} (${str(max_decrease)})")

#opening the analysis text file

#txt_file= "C:/Bootcamp/ALLHW/challenge03/Starter_Code/PyBank/analysis.txt"
txt_file= Path("CHALLENGE03","Startger_Code", "PyBank", "analysis.txt")

with open(txt_file,"w") as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {len(months)}\n")
    file.write(f"Total Profit/Losses: ${sum(profit)}\n")
    file.write(f"Average change: ${round(sum(monthly_change)/len(monthly_change),2)}\n")
    file.write(f"Greatest Increase in Profits: {months[max_increase_month]} (${str(max_increase)})\n")
    file.write(f"Greatest Decrease in Profits: {months[max_decrease_month]} (${str(max_decrease)})")
               
