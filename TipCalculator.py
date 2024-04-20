# Tip (given in restaurant/hotel to the waiter) calculator program

# declaring variables
totalBillValue = 0
percentageTip = 0
NumOfGuests = 0
billPerGuest = 0

# taking inputs from user
totalBillValue = float(input("Enter total bill amount: "))
percentageTip = int(input("Enter percentage of tip: "))
NumOfGuests = int(input("Enter number of guests to split the bill: "))

# calculating bill per guest
billPerGuest = ((percentageTip/100)*totalBillValue + totalBillValue)/ NumOfGuests
print("*****************************************************************")
print("Welcome to the tip calculator.")
print("What was the total bill? ", totalBillValue)
print("What percentage of tip would you like to give? 10, 12 or 15? ", percentageTip)
print("How many guests are there to split the bill? ", NumOfGuests)
print("Each guest should pay: ", billPerGuest)
print("*****************************************************************")