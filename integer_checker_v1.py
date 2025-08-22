# Functions go here
def int_check(question):
    """Checks users enter an integer / float that is more than zero (or the 'xxx' exit code)"""

    error = "Oops - please enter an integer more than zero."

    while True:
        response = input(question).lower()

        # check for the exit code
        if response == "xxx":
            return response

        try:
            # Change the response to an integer and check that it's more than zero
            response = int(response)

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main Routine goes here

# loop for testing purposes
while True:
    print()

    # ask user for an integer
    my_num = int_check("Choose a number more than zero: ")
    print(f"You chose {my_num}")



