# Days passed calculation
# Jordyn Chalmers
# Computer Programming Class - 16/02/2024
# Imports calendar module
import calendar
# Imports datetime module
import datetime

# Function to calculate days passed from 1st of January
# Is called with user_date variable as arg
def passed_days_soy(dates):
    # Variable to set the start date as 1st of January
    start = datetime.datetime(dates.year, 1, 1)
    # Calculates the difference between user input and 1st of January
    passed = (dates - start).days
    # Returns passed object data
    return passed

# Simple print to log welcome
print("Welcome to my days passed calculator!")

# User input to specify "Custom" or "Current" date
confirm = str(input("Do you wish to use a custom date or current date? (Custom/Current): ")).lower()

# If block if user input is "custom" for custom input dates
if confirm == "custom":
    # User inputs for calculations
    day = int(input("Enter your day: "))
    month = int(input("Enter your month: "))
    year = int(input("Enter your year: "))
# Elif block if user input is "current" for current dates as input using datetime module
elif confirm == "current":
    day = datetime.datetime.now().day
    month = datetime.datetime.now().month
    year = datetime.datetime.now().year

# Uses the calendar module to check if user inputed year is a leap year then print to console
if calendar.isleap(year):
    print(year, "is a leap year!")
else:
    print(year, "is not a leap year!")

# Creates datetime object with user inputs
user_date = datetime.datetime(year, month, day)

# Calls function using user_date as argument
passed = passed_days_soy(user_date)
print("Number of days passed since January 1st:", passed)
