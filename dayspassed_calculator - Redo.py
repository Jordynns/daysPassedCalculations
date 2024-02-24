# Days passed calculation
# Jordyn
# Computer Programming Class - 16/02/2024

# Imports the sys module
import sys

# Array list for total months and the days
daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Function to calculate if input year is a leapyear by checking if year is divisible by 4 but not 100 or unless it is divisible by 400. If these conditions are met returns True else returns False
def leapYear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

# Function that takes the 4 arguments/functions "day, month, year, daysInMonth" 
def passed(day, month, year, daysInMonth):
    # Date validation to check if month is within 1-12 and if days are within 1-daysInMonth array list (If date is invalid print to log and exit script)
    if month < 1 or month > 12 or day < 1 or day > daysInMonth[month - 1]:
        print("Invalid date!\nPlease try again.")
        userInput()

    # Variable that takes sum of the days passed upto the user specified date.
    # sum() totals the days in the months
    # + day adds the days in current month
    # [:month-1] subtracts the current month so it doesn't total the current month during the sum calculation
    total = sum(daysInMonth[:month-1]) + day

    # If user entered month is greater than 2 (February) and leapYear function is True adds + 1 day to the total to account for the extra day in February 
    if month > 2 and leapYear(year):
        total += 1
    # Returns calulated total days passed to "total" variable
    return total

# User input function to determin the dates and leapyear status
def userInput():
    day = int(input("Enter your day: "))
    month = int(input("Enter your month (1/12): "))
    year = int(input("Enter your year: "))

    # "passed" function is called with user input arguments/functions"day, month, year, daysInMonth" then total is calculated then the total days passed is printed to log along with if it's a leap year or not
    total = passed(day, month, year, daysInMonth)
    if leapYear(year):
        print("Total days passed since the 1st of January: ", total,"\n",year, "is leap year!")
    else:
        print("Total days passed since the 1st of January: ", total,"\n",year, "is not a leap year!")

# Calls userInput function
userInput()
