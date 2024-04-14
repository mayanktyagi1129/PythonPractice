# Take inputs from user
maths = int(input("Enter marks for Maths out of 100: "))
english = int(input("Enter marks for English out of 100: "))
science = int(input("Enter marks for Science out of 100: "))
hindi = int(input("Enter marks for Hindi out of 100: "))
computer = int(input("Enter marks for Computer out of 100: "))
print(maths, english, science, hindi, computer)

total = 500

totalMarksObtained = maths + english + science + hindi + computer
print("Total marks obtained: ", totalMarksObtained)

percentageObtained = (totalMarksObtained * 100) / total
print("Percentage: ", percentageObtained)

averageMarksObtained = totalMarksObtained / 5
print("Average: ", averageMarksObtained)