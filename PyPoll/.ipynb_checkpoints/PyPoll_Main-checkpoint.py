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
with open(os.path.abspath(r"GitHub\Python-Challenge\PyPoll\analysis\PyPoll Analysis_rjh.txt"), 'w') as file:

    file.write("Election Results\n")
    file.write("\n")
    file.write("-------------------------\n")
    file.write("\n")
    file.write(f"Total Votes: {TotVotes}\n")
    file.write("\n")
    file.write("-------------------------\n")
    file.write("\n")

    print("Election Results")
    print()
    print("-------------------------")
    print()
    print(f"Total Votes: {TotVotes}")
    print()
    print("-------------------------")
    print()

    # create a list to store tally for each candidate and set counters to 0
    vcount = {}
    TCount = []
    CCount = []

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
        format_PCNT = round(PCNT, 3)
        print(f"{CAN}: {format_PCNT}% ({count})")
        print()
        
        file.write(f"{CAN}: {format_PCNT}% ({count})\n")
        file.write("\n")
        
        TCount.append(count)
        CCount.append(CAN)

    # determine the winner
    WinCount = max(TCount)
    result = []
    index = []
    for x, item in enumerate(TCount):
        if item == WinCount:
            result.append(item)
            index.append(x)
    x = index[0]

    winner = f"Winner: {CCount[x]}"
    print("-------------------------")
    print()
    print(winner)
    print()
    print("-------------------------")
    file.write("-------------------------\n")
    file.write("\n")
    file.write(winner + "\n")
    file.write("\n")
    file.write("-------------------------\n")