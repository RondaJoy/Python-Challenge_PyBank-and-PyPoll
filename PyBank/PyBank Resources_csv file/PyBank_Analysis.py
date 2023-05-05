import csv

# read in data from .csv file
BudgetData = open('budget_data.csv', 'r')
BudgetRead = csv.DictReader(BudgetData)
# count the rows on the spreadsheet 
rowdata = list(BudgetRead)
RowNum = len(rowdata)

# establish baseline for sum total of Profit/Losses
Tot_Profit_Loss = 0
# calculate sum total of Profit/Losses
for col in rowdata:
    Tot_Profit_Loss += int(col['Profit/Losses'])

# read in data from .csv file (again)
BudgetData = open('budget_data.csv', 'r')
BudgetRead = csv.DictReader(BudgetData)
# create list from Column B
PLCol = [float(row['Profit/Losses']) for row in rowdata]
# assign name for new list, change in B from month to month 
delta = []

for x in range(len(PLCol) -1):
    # assign new list called "Diffs" to store arithmetic values
    Diffs = PLCol[x+1] - PLCol[x]
    # append "delta" list using "Diffs" values
    delta.append(Diffs)
avg_Diffs = sum(delta) / len(delta)

# assign variable for month of greatest increased profit
MaxIncrs = max(delta)
# See README for citation, rows 37-44
result = []
index = []
for v, item in enumerate(delta):
    if item == MaxIncrs:
        result.append(item)
        index.append(v)
# establish index to locate the associated value in Column A
x = index[0] +1
# Create list from Column A
DateCol = [str(row['Date']) for row in rowdata]

# assign variable for month of greatest increased profit
MaxDecrs = min(delta)
# See README for citation, rows 52-59
result = []
index = []
for v, item in enumerate(delta):
    if item == MaxDecrs:
        result.append(item)
        index.append(v)
# establish index to locate the associated value in Column A
x = index[0] +1

# print to txt file
with open('PyBank Analysis_rjh.txt', 'w') as f:
    f.write("Total Months: " +str(RowNum) + "\n")
    f.write("Total: $" + str(Tot_Profit_Loss) + "\n")
    f.write("Average Change: $" + str(round(avg_Diffs, 2)) + "\n")
    f.write(f"Greatest Increase in Profits: {DateCol[x]} (${int(MaxIncrs)})" + "\n")
    f.write(f"Greatest Decrease in Profits: {DateCol[x]} (${int(MaxDecrs)})" + "\n")

# print to terminal
print("Total Months: " +str(RowNum))
print("Total: $" + str(Tot_Profit_Loss))
print("Average Change: $" + str(round(avg_Diffs, 2)))
print(f"Greatest Increase in Profits: {DateCol[x]} (${int(MaxIncrs)})")
print(f"Greatest Decrease in Profits: {DateCol[x]} (${int(MaxDecrs)})")
