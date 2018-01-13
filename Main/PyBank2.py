
# coding: utf-8

# In[1]:


import os
import csv
import operator
from collections import Counter


# In[2]:


budgetCSV = os.path.join("raw_data", "budget_data_2.csv")



# In[3]:


date = []
revenue = []
totalMonths = 0
totalRevenue = 0
avgRevChange = 0
maxIncRev = 0
maxDecRev = 0
maxIncDate = 0
maxDecDate = 0


# In[4]:


with open(budgetCSV, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
    for row in csvreader:
        date.append(row[0])
        revenue.append(float(row[1]))
    


# In[5]:


totalRevenue = sum(revenue)
totalMonths = len(date)
avgRevChange = round(totalRevenue/totalMonths,2)
print(avgRevChange)


# In[6]:


i=0
previousMonth = 0
currentMonth = 0
while i <= totalMonths -1:
    currentMonth = revenue[i]
    if currentMonth - previousMonth >= maxIncRev:
        maxIncRev = currentMonth - previousMonth
        maxIncDate = i
    elif currentMonth - previousMonth <= maxDecRev:
        maxDecRev = currentMonth - previousMonth
        maxDecDate = i
        
    previousMonth = currentMonth
    i = i + 1

print(maxIncRev,date[maxIncDate])
print(maxDecRev,date[maxDecDate])


# In[7]:


print(str("Total Months:" + " " + str(totalMonths)))
print(str("Total Revenue:" + " " + "$" + str(totalRevenue)))
print(str("Average Revenue Change: " + "$" + str(avgRevChange)))
print(str("Greatest Increase in Revenue: " + "$" + str(maxIncRev) + " " + "on " + date[maxIncDate]))
print(str("Greatest Decrease in Revenue: " + "$" + str(maxDecRev) + " " + "on " + date[maxDecDate]))


# In[8]:


output_file = os.path.join("newBudget2.csv")

with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Financial Analysis"])
    writer.writerow(["-----------------------"])
    writer.writerow(["Total Months:" + " " + str(totalMonths)])
    writer.writerow(["Total Revenue:" + " " + "$" + str(totalRevenue)])
    writer.writerow(["Average Revenue Change: " + "$" + str(avgRevChange)])
    writer.writerow(["Greatest Increase in Revenue: " + "$" + str(maxIncRev) + " " + "on " + date[maxIncDate]])
    writer.writerow(["Greatest Decrease in Revenue: " + "$" + str(maxDecRev) + " " + "on " + date[maxDecDate]])
   
    


