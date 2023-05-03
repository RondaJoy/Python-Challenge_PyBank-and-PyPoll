import csv

# read in data from .csv file
BudgetData = open('budget_data.csv', 'r')
BudgetRead = csv.DictReader(BudgetData)
# count the rows on the spreadsheet 
rowdata = list(BudgetRead)
RowNum = len(rowdata)
print("Total Months: " +str(RowNum))

# establish baseline for sum total of Profit/Losses
Tot_Profit_Loss = 0
# calculate sum total of Profit/Losses
for col in rowdata:
    Tot_Profit_Loss += int(col['Profit/Losses'])
print("Total: $" + str(Tot_Profit_Loss))

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
print("Average Change: $" + str(round(avg_Diffs, 2)))

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
print(f"Greatest Increase in Profits: {DateCol[x]} (${int(MaxIncrs)})")

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
print(f"Greatest Decrease in Profits: {DateCol[x]} (${int(MaxDecrs)})")
