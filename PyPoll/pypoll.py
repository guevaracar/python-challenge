import csv
from collections import Counter
import operator

# Files to name for import and output into a .txt file
import_csv = "election_data_2.csv"
output_csv = "election_analysis.txt"

# Read CSV file
with open(import_csv) as pollData:
    readCSV = csv.reader(pollData, delimiter=",")
    next(readCSV, None)

    #lists
    VoterId = []
    Candidate = [] 
    
    #Append values from column for VoterId and Candidate
    for column in readCSV:

        VoterId.append(str(column[0]))
        Candidate.append((column[2]))

    #Name a variable for the total number of votes
    totalvotes = len(VoterId)
    
    cnt = Counter(Candidate)
    #print(cnt)

    cand_set = set(Candidate)
    #print(cand_set)

    #cand_name = cnt({key})
        


    #names = []
    #for x in cand_set:
    #    names.append(x)
    #print(names)
   # cand_count_votes = cnt[]
    Khan_cnt = cnt['Khan']
    Khan_percent = (Khan_cnt/totalvotes)*float(100)
    Correy_cnt = cnt['Correy']
    Correy_percent = (Correy_cnt/totalvotes)*float(100)
    Li_cnt = cnt['Li']
    Li_percent = (Li_cnt/totalvotes)*float(100)
    OTooley_cnt = cnt["O'Tooley"]
    OTooley_percent = (OTooley_cnt/totalvotes)*float(100)

    Winner = max(cnt, key=lambda key: cnt[key])

    print("'''" + "\n" + "Election Results" + "\n" + "--------------------------" + "\n" +
        "Total Votes: " + str(totalvotes) + "\n" + "--------------------------")


    
    print("Khan: {0:.1f}% ({1})".format(Khan_percent, Khan_cnt))
    print("Correy: {0:.1f}% ({1})".format(Correy_percent, Correy_cnt))
    print("Li: {0:.1f}% ({1})".format(Li_percent, Li_cnt))
    print("O'Tooley: {0:.1f}% ({1})".format(OTooley_percent, OTooley_cnt))
    print("----------------------\n Winner: ", Winner)
    #print(max({cnt}))

#dictionary = cnt
#emptylist=[]
#for key in dictionary:
#    emptylist.append(dictionary[key])

#print(emptylist)
#print(cand_set)