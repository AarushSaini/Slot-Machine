import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def deposit():
    while True:
        amount = input("💰 What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("❗ Amount must be greater than 0.")
        else:
            print("❗ Please enter a valid number.")

    return amount


def get_number_of_lines():
    while True:
        lines = input(f"🎰 Enter the number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("❗ Enter a valid number of lines.")
        else:
            print("❗ Please enter a valid number.")

    return lines


def get_bet():
    while True:
        amount = input("💸 What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"❗ Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("❗ Please enter a valid number.")

    return amount

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    print("\n💎 Slot Machine Results 💎")
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()
    print()

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"❗ You do not have enough to bet that amount. Your current balance is: ${balance}")
        else:
            break

    print(f"🤑 You are betting ${bet} on {lines} lines. Total bet: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"🎉 You won ${winnings}!")
    if winning_lines:
        print(f"✨ Winning lines: ", *winning_lines)
    else:
        print("😢 No winning lines.")

    return winnings - total_bet


def main():
    print("🎰 Welcome to the Python Slot Machine! 🎰")
    balance = deposit()
    while True:
        print(f"\n💵 Current balance: ${balance}")
        answer = input("🎲 Press Enter to play (or type 'q' to quit): ").lower()
        if answer == "q":
            break
        balance += spin(balance)

    print(f"\n💸 You left with ${balance}. Thanks for playing! 💸")
    print("👋 Goodbye! See you next time!")

main()
