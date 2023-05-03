import csv

BudgetData = open('budget_data.csv', 'r')
BudgetRead = csv.DictReader(BudgetData)
rowdata = list(BudgetRead)
RowNum = len(rowdata)
print("Total Months: " +str(RowNum))
Tot_Profit_Loss = 0
for col in rowdata:
    Tot_Profit_Loss += int(col['Profit/Losses'])

print("Total: $" + str(Tot_Profit_Loss))

BudgetData = open('budget_data.csv', 'r')
BudgetRead = csv.DictReader(BudgetData)
PLCol = [float(row['Profit/Losses']) for row in rowdata]
delta = []
for x in range(len(PLCol) -1):
    Diffs = PLCol[x+1] - PLCol[x]
    delta.append(Diffs)

avg_Diffs = sum(delta) / len(delta)

print("Average Change: $" + str(round(avg_Diffs, 2)))