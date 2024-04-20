# Write a program to take input of obtained marks (out of 100) in various subjects (at least 5
# subjects) of a student and calculate its Grand total, total percentage and average.

marksDict = {} # declaring a dictionary to hold the subjects and marks obtained per subject
grandTotal = 0 # declaring to hold the grand total of marks

# Taking inputs from user
numOfSubjects = int(input("Please enter number of subjects for which you enter marks: "))

if numOfSubjects < 5:
    numOfSubjects = int(input("Please enter marks for minimum 5 subjects: "))

fromTotal = numOfSubjects * 100

for i in range(numOfSubjects):
    key = input(f"Enter subject {i+1} name: ")
    value = int(input("Enter marks for subject: "))
    marksDict[key] = value
    grandTotal = grandTotal + value

print("Marks obtained in subjects: ", marksDict)
print("Grand Total", grandTotal)
print("Marks obtained from total of: ", fromTotal)

# Calculating Percentage
totalPercentage = (grandTotal * 100) / fromTotal
print("Total Percentage: ", totalPercentage)

# Calculating Average
averageMarksObtained = grandTotal / numOfSubjects
print("Average: ", averageMarksObtained)