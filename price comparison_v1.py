import pandas
import numpy


# Functions go here
def make_statement(statement, decoration):
    """Emphasises headings by adding decoration
    at the start and end"""

    return f"{decoration * 3} {statement} {decoration * 3}"


def string_check(question, valid_ans_list=('yes', 'no'),
                 num_letters=1):
    """Checks that users enter the full word
    or the first letter of a word from a list of valid responses"""

    while True:

        response = input(question).lower()

        for ITEM in valid_ans_list:

            # check if the response is the entire world
            if response == ITEM:
                return ITEM

            # check if it's the first letter
            elif response == ITEM[:num_letters]:
                return ITEM

        print(f"Please choose an option from {valid_ans_list}")


def instructions():
    make_statement("Instructions", "ℹ️")

    print('''
    
Welcome to 🍭 Candy land 🍭 — your virtual sweet shop!

Here’s how this tasty adventure works:

1. You’ll start by entering your name and setting a budget 
   (how much you’re allowed to spend).

2. You’ll be shown a list of delicious sweets with their prices.

3. You can keep buying sweets (by choosing their number) as long 
   as you stay within your budget.

4. If you try to buy something more expensive than what 
   you can afford, you’ll get a friendly reminder.

5. Once you can no longer afford any more sweets, the 
   program will end and say goodbye!

Let’s get snacking! 🍬🍫🍭

    ''')


def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. Please try again.")


def int_check(question, low, high):
    """Checks users enter a budget between two values"""

    error = f"Oops - please enter a number between {low} and {high}."

    while True:

        try:
            # Change the response to an integer and check that it's more than zero
            response = int(input(question))

            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


def currency(x):
    """Formats numbers as currency ($#.##)"""
    return "${:.2f}".format(x)


# Main Routine goes here

# Initialise sweet numbers
MAX_SPEND = 1000
budget = 0

# lists to hold ticket details
all_sweets = [
    "Sherbet Line",
    "Hi-Chews",
    "Mints",
    "Mystery Bag",
    "Hi-chews",
    "Turkish Delight",
    "Chocolate Bars",
    "Gummy Bears",
    "Caramel Eclairs",
    "Nerd Pack",

]

all_sweets_costs = [1, 2, 2, 2, 2, 2, 3, 4, 4, 5, ]

sweets_dict = {
    'Sweets': all_sweets,
    'Sweets Price': all_sweets_costs,
}

# create dataframe / table from dictionary
sweets_frame = pandas.DataFrame(sweets_dict)

# Rearranging index
sweets_frame.index = numpy.arange(1, len(sweets_frame) + 1)

# Program main heading
print(make_statement("Candy land", "🍭"))

# Ask user for their name (and check it's not blank)
print()
name = not_blank("Name: ")

# Ask user if they want to see the instructions
# display them if necessary
print()
want_instructions = string_check(f" Hi {name}, Do you want to see the instructions? ")

if want_instructions == "yes":
    instructions()

print()

# ask for budget
budget = int_check("what is your budget? (Maximum Budget of $20) ", 1, 20)

print(f"your budget is ${budget}")
print()

# set purchase sweets to none
purchased_sweets = []
purchased_prices = []

# created a purchased dict
purchased_dict = {
    'Sweets': purchased_sweets,
    'Prices': purchased_prices,
}

# import list of sweets
sweet_string = sweets_frame.to_string(index=False)

# loop
while budget <= MAX_SPEND:

    print()

    # display items
    print("here's a list of sweets you can select from")
    print(sweets_frame)
    print()

    # prompt user to select a row
    try:
        # ask user for choice
        choice = int_check("choose your sweet with the number of the corresponding row: ", 1, 10)

        selected_row = all_sweets[choice - 1]
        sweets_price = all_sweets_costs[choice - 1]

        if budget >= sweets_price:
            budget -= sweets_price

            purchased_sweets.append(selected_row)
            purchased_prices.append(sweets_price)

            # display choice
            print(f"your selected {selected_row} costing ${sweets_price} ")
            print(f"your new budget is ${budget} ")
            print()

        else:
            print(f"sorry the {selected_row} costing ${sweets_price} "
                  f"is above your current budget of ${budget}. Please try again.")
            continue

        if budget <= 0:
            print("You don't have enough money to make any more purchases ❌")
            print()
            break

        repurchase = string_check("Would you like to purchase another sweet ")

        if repurchase == "no":
            break

    except ValueError:
        print("Please enter a valid number")

# End of Loop

# itemised purchase list
# create dataframe / table from dictionary
purchased_frame = pandas.DataFrame(purchased_dict)

total_spent = sum(purchased_prices)

# Rearranging index
purchased_frame.index = numpy.arange(1, len(purchased_frame) + 1)
if purchased_sweets:
    print(make_statement(f"here are {name}'s purchases:", "🏧"))
    print()
    print(purchased_frame)
    print(f"Your total amount spent was :💲{total_spent}")

# create file to hold data (add .txt extension)
# file_name = "MMF_ticket_details"
# write_to = f"{file_name}.txt"

# text_file = open(write_to, "w+")

# write the item to file
# for item in to_write:
# text_file.write(item)
# text_file.write("\n")
