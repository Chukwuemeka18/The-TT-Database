# importing csv module
import csv

  
# csv file name
filename = "Theta Tau's UCM Class Database (Responses) - Form Responses 1.csv"
  
# initializing the titles and rows list
fields = []
rows = []
  
# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
      
    # extracting field names through first row
    fields = next(csvreader)
  
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)
  
    # get total number of rows
    print("Total no. of rows: %d"%(csvreader.line_num))
  
# printing the field names
print('Field names are:' + ', '.join(field for field in fields))
  
# printing first 5 rows
print('\nFirst 5 rows are:\n')
for row in rows[:len(rows)-1]:
    # parsing each column of a row
    for col in row:
        print("%10s"%col,end=" "),
    print('\n')


print("Test")
newRows = []
answer = True

m = 0
for i in range(0, len(rows)):
    for j in range(2, len(rows[i])):
        for k in range(0, len(newRows)):
            if rows[i][j] == newRows[k]:
                answer = False
        if answer == False:
            answer = True
        elif answer == True:
            rows.append(row)
            newRows.append(rows[i][j])
            m = m+1
        else:
            print()

print(rows[0][0])
print(rows[0][1])
print(rows[0][2])

print(rows[1][0])
print(rows[1][1])
print(rows[1][2])

print("Test2")
for n in range(0, len(newRows)):
    print(newRows[n])
    print(" ")

print(newRows[len(newRows)-1][0])
ls = newRows[len(newRows)-1].split(",")

print(ls[0])