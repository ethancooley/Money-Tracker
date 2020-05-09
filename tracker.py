import sys
from function import process_file

weekdays = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

# Imports command line arguments and tests function for exceptions
try:
    major_list = process_file(sys.argv[1])
except ValueError:
    print('Error: File not found!')
    exit()
except IndexError:
    print('Error: Not enough command line arguments!')
    exit()

# Create variables for regular income/expense
income = major_list[0]
expenses = major_list[1]

# This is the day counter which starts at 0
i = 0

# Boolean value which will control while loop
loop_value = True

# Asks the user for their starting balance
try:
    starting_balance = input('Starting balance: $')
    starting_balance = float(starting_balance)

# If the input value is not a float the program will quit immediately
except ValueError:
    print('Error: Cannot convert to float!')
    loop_value = False
    exit()

# Add regular transactions
daily_balance = starting_balance
starting_balance = starting_balance + income[0] - expenses[0]
current_balance = starting_balance

# The user cannot start with a negative balance so the program quits immediately
if starting_balance <= 0:
    print('Error: Must start with positive balance!')
    loop_value = False

# The loop which will ask for certain commands
while loop_value == True:
    print()
    command = input('Enter command: ')
    # 'transaction' command
    if command == 'transaction':
        try:
            amount = input('Enter amount: $')
            amount = float(amount)
            current_balance = current_balance + amount
        except ValueError:
            print('Error: Cannot convert to float!')
        continue
    # 'next' command
    elif command == 'next':
        if current_balance < 0:
            print("Oh no! You're in debt!")
            loop_value = False
            break
        i += 1
        daily_balance = current_balance
        current_balance = current_balance + income[i % 7] - expenses[i % 7]
        print('Going to the next day...')
        continue
    # 'status' command
    elif command == 'status':
        print('Day {} ({})'.format(i, weekdays[i % 7]))
        print('Starting balance: ${:.2f}'.format(daily_balance))
        print('Current balance: ${:.2f}'.format(current_balance))
        if current_balance > daily_balance:
            print("Nice work! You're in the black.")
        elif current_balance < daily_balance:
            print("Be careful! You're in the red.")
        continue
    # 'help' command
    elif command == 'help':
        print('The available commands are:')
        print('"transaction": Record a new income or expense')
        print('"next": Move on to the next day')
        print('"status": Show a summary of how you\'re doing today')
        print('"regular": Show a summary of your regular transactions')
        print('"help": Show this help message')
        print('"quit": Quit the program')
        continue
    # 'quit' command
    elif command == 'quit':
        print('Bye!')
        loop_value = False
        break
    # 'regular' command
    elif command == 'regular':
        print('Regular Transactions:')
        print('{}: +${:.2f} -${:.2f}'.format(weekdays[0], income[0], expenses[0]))
        print('{}: +${:.2f} -${:.2f}'.format(weekdays[1], income[1], expenses[1]))
        print('{}: +${:.2f} -${:.2f}'.format(weekdays[2], income[2], expenses[2]))
        print('{}: +${:.2f} -${:.2f}'.format(weekdays[3], income[3], expenses[3]))
        print('{}: +${:.2f} -${:.2f}'.format(weekdays[4], income[4], expenses[4]))
        print('{}: +${:.2f} -${:.2f}'.format(weekdays[5], income[5], expenses[5]))
        print('{}: +${:.2f} -${:.2f}'.format(weekdays[6], income[6], expenses[6]))
        continue
    # If the user inputs an invalid command
    else:
        print('Command not found.')
        print('Use the "help" command for a list of available commands')
        continue