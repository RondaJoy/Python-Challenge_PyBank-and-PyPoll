import csv
import os

# read data from .csv file
with open(os.path.abspath(r"C:\Users\ronda\Documents\Bootcamp\GitHub\Python-Challenge\PyPoll\Resources\election_data.csv"), 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # skip header
    PollData = list(reader)

# tally the number of rows/votes
TotVotes = len(PollData)

# open the text file for writing
with open(os.path.abspath(r"GitHub\Python-Challenge\PyPoll\analysis\PyPoll Analysis_rjh.txt"), 'w') as f:

    f.write("Election Results\n")
    f.write("\n")
    f.write("-------------------------\n")
    f.write("\n")
    f.write(f"Total Votes: {TotVotes}\n")
    f.write("\n")
    f.write("-------------------------\n")
    f.write("\n")

    print("Election Results")
    print()
    print("-------------------------")
    print()
    print(f"Total Votes: " {TotVotes})
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

TCount = []
CCount = []
# generate output for candidate name, % of total vote, and actual # of votes
for CAN, count in vcount.items():
    PCNT = (count / TotVotes) *100
    format_PCNT = round(PCNT, 3)
    print(f"{CAN}: {format_PCNT}% ({count})")
    print()
    print("-------------------------")
    print()

    f.write(f"{CAN}: {format_PCNT}% ({count})\n")
    f.write("\n")
    f.write("-------------------------\n")
    f.write("\n")
    TCount.append(count)
    CCount.append(CAN)

WinCount = max(TCount)
result = []
index = []
for x, item in enumerate(TCount):
    if item == WinCount:
        result.append(item)
        index.append(x)
x = index[0]
print(f"Winner: {CCount[x]}")
f.write(f"Winner: {CCount[x]}\n")
