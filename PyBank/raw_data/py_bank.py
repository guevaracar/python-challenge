import csv
from statistics import mean

#file loaded and file output
loaded_file = 'budget_data_1.csv'
new_file = 'budget_analysis_1.txt'

#Read CSV file in reader
with open('budget_data_1.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    next(readCSV, None)        
    
    #lists
    dates = []
    revenues = []
    
    for row in readCSV:
        date = row[0]
        revenue = row[1]
        
        dates.append(date)
        revenues.append(int(revenue))

    #row_count = len()    
   

    print(revenue_change)
    print("'''''''" + '\n' + 'Financial Analysis' + '\n' + "------------------------")
    print('\n' + "Total Months: ", len(dates))
    print("Total Revenue: $" + sum(revenues))

    revenue_change = []
    for i in range(len(revenues) -1):
        revenue_change = [revenues[i+1] - revenues[i]] 
        print("Average Revenue Change: $", mean(revenue_change)
        print("Greatest Increase in Revenue: $", max(revenue_change))
        print("Greatest Decrease in Revenue: $", min(revenue_change))

    


