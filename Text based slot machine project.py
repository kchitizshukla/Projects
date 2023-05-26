import random

MAX_LINES= 3
MAX_BET= 100
MIN_BET= 1

ROWS= 3
COLS= 3

symbol_count= {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
symbol_value= {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}
def check_winnings(columns,lines,bet):
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol]*bet
            winning_lines.append(line+1)

    return winnings,winning_lines

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols= []
    for symbol,symbol_count in symbols.items():
        for i in range(symbol_count):
            all_symbols.append(symbol)

    columns= []
    for col in range(cols):
        column=[]
        current_symbols= all_symbols[:]
        for row in range(rows):
            value= random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns[row], end= "|"):
                print("")
            else:
                print(column[row], end= "")

        print()


def deposit():
    while True:
        amount= input("What would you like to deposit? $")
        if amount.isdigit():
            amount= int(amount)
            if amount> 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount 

def get_number_of_lines():
    while True:
        lines= input("Enter the number of lines to bet on(1-"*str(MAX_LINES)* ")? ")
        if lines.isdigit():
            lines= int(lines)
            if 1<= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    
    return lines

def get_bet():
    while True:
        amount= input("What  would you like to bet? ")
        if amount.isdigit():
            amount= int(amount)
            if MIN_BET<= amount <= MAX_BET:
                break
            else:
                print("Amount must be between ${MIN_BET}- ${MAX_BET}.")
        else:
            print("Please enter a number.")
   
    return amount

def spin(balance):
    lines = get_number_of_lines()
    while():
        bet = get_bet()
        totalbet= bet*lines

        if totalbet> balance:
            print("Youd do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break
         
         
    print("You are betting ${bet} on {lines} line. Total bet is equal to: ${totalbet}.")

    slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings = check_winnings(slots,lines,bet,symbol_value)
    print("You won ${winnings}.")
    print("You won on lines:", *winning_lines)
    return winning_lines - total_bet
    
def main1():
    balance= deposit()
    while True:
        print("Current Balance is $", {balance})
        answer= input("Press enter to play (q to quit).")
        if answer== "q":
            break
        balance+= spin(balance)

    print("You left with $", {balance})

main1()        