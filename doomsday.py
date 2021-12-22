# pylint:disable=c0103

# User input
month = input("Enter a month. ")
day = input("Enter a day within that month. ")
fullyear = input("Enter a year. ")

# Calculating the anchor day according to the year.
counter = 0

century_code = str(fullyear[:2])

if int(century_code) % 4 == 0:
    counter += 2
elif int(century_code) % 4 == 1:
    counter += 0
elif int(century_code) % 4 == 2:
    counter += 5
elif int(century_code) % 4 == 3:
    counter += 3

year = str(fullyear[-2:])

S1 = int(year) // 12
S2 = int(year) % 12
S3 = int(S2) // 4
S = S1 + S2 + S3 + counter
anchor_day = S % 7

# Accounting for leap years
DD1 = 3
DD2 = 28
if int(year) % 4 == 0:
    DD1 += 1
if int(fullyear) % 4 == 0:
    DD2 += 1

# if statements for each month
daycounter = 0

if int(month) == 1:
    daycounter = abs(int(day) - DD1)
elif int(month) == 2:
    daycounter = abs(int(day) - DD2)
elif int(month) == 3:
    daycounter = abs(int(day) - 14)
elif int(month) == 4:
    daycounter = abs(int(day) - 4)
elif int(month) == 5:
    daycounter = abs(int(day) - 9)
elif int(month) == 6:
    daycounter = abs(int(day) - 6)
elif int(month) == 7:
    daycounter = abs(int(day) - 11)
elif int(month) == 8:
    daycounter = abs(int(day) - 8)
elif int(month) == 9:
    daycounter = abs(int(day) - 5)
elif int(month) == 10:
    daycounter = abs(int(day) - 10)
elif int(month) == 11:
    daycounter = abs(int(day) - 7)
elif int(month) == 12:
    daycounter = abs(int(day) - 12)

# Covering invalid dates
if int(month) > 12:
    print("We don't have that many months")
    exit()
else:
    pass
if int(day) > 31 and (int(month) == 4 or 6 or 9 or 11):
    print("That is not a valid date.")
    exit()
else:
    pass
if int(day) > 32 and (int(month) == 1 or 3 or 5 or 7 or 8 or 10 or 12):
    print("That is not a valid date.")
    exit()
else:
    pass

if int(day) > 29 and (int(month) == 2 and int(fullyear) % 4 == 0):
    print("That is not a valid date.")
    exit()
else:
    pass

if int(day) > 28 and (int(month) == 2 and int(fullyear) % 4 != 0):
    print("That is not a valid date.")
    exit()
else:
    pass

# Final calculations
finalday = (daycounter + anchor_day) % 7
intro = "That date falls on a "
if finalday == 0:
    print(intro + "Sunday")
if finalday == 1:
    print(intro + "Monday")
if finalday == 2:
    print(intro + "Tuesday")
if finalday == 3:
    print(intro + "Wednesday")
if finalday == 4:
    print(intro + "Thursday")
if finalday == 5:
    print(intro + "Friday")
if finalday == 6:
    print(intro + "Saturday")