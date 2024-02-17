# Days passed calculation
# Jordyn
# Computer Programming Class - 16/02/2024

# Imports the sys module
import sys

# Function to calculate if input year is a leapyear by checking if year is divisible by 4 but not 100 or unless it is divisible by 400. If these conditions are met returns True else returns False
def leapYear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

# Function that takes the 4 arguments "day, month, year, daysinMonth" 
def passed(day, month, year, daysinMonth):
    # Date validation to check if month is within 1-12 and if days are within 1-daysinMonth array list (If date is invalid print to log and exit script)
    if month < 1 or month > 12 or day < 1 or day > daysinMonth[month - 1]:
        print("Invalid date!\nExiting script.")
        sys.exit()

    # Variable that takes sum of the days passed upto the user specified date.
    # sum() totals the days in the months
    # + day adds the days in current month
    total = sum(daysinMonth[:month-1]) + day

    # If user entered month is greater than 2 (February) and leapYear function is True adds + 1 day to the total to account for the extra day in February 
    if month > 2 and leapYear(year):
        total += 1
    # Returns calulated total days passed to "total" variable
    return total

# Array list for total months and their days
daysinMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# User input to determin the dates
day = int(input("Enter your day: "))
month = int(input("Enter your month: "))
year = int(input("Enter your year: "))

# "passed" function is called with user input arguments "day, month, year, daysinMonth" then total is calculated then the total days passed is printed to log along with if it's a leap year or not
total = passed(day, month, year, daysinMonth)
if leapYear(year):
    print("Total days passed since the 1st of January: ", total,"\n",year, "is leap year!")
else:
    print("Total days passed since the 1st of January: ", total,"\n",year, "is not a leap year!")
