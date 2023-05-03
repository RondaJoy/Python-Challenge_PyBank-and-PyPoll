import csv

print("Election Results")
print()
print("-------------------------")
print()

# read data from .csv file
with open('election_data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    # skip header
    next(reader)
    PollData = list(reader)

# tally the number of rows/votes
TotVotes = len(PollData)
print("Total Votes: " +str(TotVotes))
print()
print("-------------------------")
print()

# create a list to store tally for each candidate
vcount = {}
# begin for loop to count occurrences of candidate name in Column C/2
for col in PollData:
    CAN = col[2]
    if CAN in vcount:
        vcount[CAN] += 1
    else:
        vcount[CAN] = 1

# generate output for candidate name, % of total vote, and actual # of votes
for CAN, count in vcount.items():
    PCNT = (count / TotVotes) *100
print(f"{CAN}: {PCNT:.3csvfile}% ({count})")