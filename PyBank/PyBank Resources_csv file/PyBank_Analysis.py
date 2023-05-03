import csv

BudgetData = open('budget_data.csv', 'r')
BudgetRead = csv.DictReader(BudgetData)
rowdata = list(BudgetRead)
RowNum = len(rowdata)
print("Total Months: " +str(RowNum))
Tot_Profit_Loss = 0
for col in BudgetRead:
    Tot_Profit_Loss += int(col['Profit/Losses'])

print("Total: $" + str(Tot_Profit_Loss))
    