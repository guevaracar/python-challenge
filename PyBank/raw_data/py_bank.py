import csv
from statistics import mean

#file loaded and file output
loaded_file = 'budget_data_1.csv'
loaded_file2 = 'budget_data_2.csv'
new_file = 'budget_analysis_1.txt'

#Read CSV file in reader
with open(loaded_file, newline='') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    next(readCSV, None)     
    csvlist = list(readCSV)   
    
    #lists
    dates = []
    revenues = []
    
    #append values into list via for loop
    for row in csvlist:
        dates.append(row[0])
        revenues.append(int(row[1]))   

    #for loop to store revenue change into a list
    revenue_change = []   
    revenue_change = [revenues[i+1] - revenues[i] for i in range(len(revenues) -1)]

    #average revenue and total revenue
    avg_revenue = mean(revenue_change)
    total_revenue = sum(revenues)

    #Greatest increase and decrease variables. 
    max_increase = max(revenue_change)
    max_decrease = min(revenue_change)
    max_month = None
    min_month = None

    #find the max and min month from for loops
    value = None
    for x in csvlist:
        if value is None:
            value = int(x[1])
            continue
        if int(x[1]) - value == max_decrease:
            min_month = x[0]
        value = int(x[1])

    value2 = None
    for _ in csvlist:
        if value2 is None:
            value2 = int(_[1])
            continue
        if abs(int(_[1]) - value2) == max_increase:
            max_month = _[0]
        value2 = int(_[1])
    
    avg_revenue = mean(revenue_change)
    total_revenue = sum(revenues)
    print("'''''''" + '\n' + 'Financial Analysis' + '\n' + "------------------------")
    print('\n' + "Total Months: ", len(dates))
    print(f"Total Revenue: ${total_revenue}")
    print(f"Average Revenue Change: ${avg_revenue}")
    print(f"Greatest Increase in Revenue: {max_month} ${max_increase}")
    print(f"Greatest Decrease in Revenue: {min_month} ${max_decrease}")
