# Days passed calculation
# Jordyn Chalmers
# Computer Programming Class - 16/02/2024

# Array list for total months and the days
daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Function to calculate if input year is a leapyear by checking if year is divisible by 4 but not 100 or unless it is divisible by 400 using the modulos operator. If these conditions are met returns True else returns False
def leapYear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

# Function that takes the 4 arguments/variables "day, month, year, daysInMonth" 
def passed(day, month, year, daysInMonth):
    # Date validation to check if month is within 1-12 and if days are within 1-daysInMonth array list (If date is invalid print to log and return "None" to "total" variable which continues the while loop for the user to enter a valid date)
    if month < 1 or month > 12 or day < 1 or day > daysInMonth[month - 1]:
        print("Invalid date!\nPlease try again.")
        return None
    # Variable that takes sum of the days passed upto the user specified date.
    # sum() totals the days in the months
    # + day adds the days in current month along with -1 to day to account for the current day
    # [:month-1] subtracts the current month so it doesn't total the current month during the sum calculation
    total = sum(daysInMonth[:month-1]) + day -1

    # Check if leapYear is True and then checks if month is greater than 2 if not return total else so +1 to total to account for the extra day in February and return total
    if leapYear(year) == True:
        if month > 2:
            total += 1
    return total
# User input function with simple while loop to determin the dates and leapyear status
def userInput():
    while True:
        day = int(input("Enter your day: "))
        month = int(input("Enter your month (1/12): "))
        year = int(input("Enter your year: "))

        # "passed" function is called with user input arguments/functions"day, month, year, daysInMonth" 
        # if "total" does not equal "None" runs leapyear check then breaks the while loop ending the script
        total = passed(day, month, year, daysInMonth)
        if total != None:
            if leapYear(year):
                print("Total days passed since the 1st of January: ", total,"\n",year, "is leap year!")
                break
            else:
                print("Total days passed since the 1st of January: ", total,"\n",year, "is not a leap year!")
                break

# Calls userInput function
userInput()
