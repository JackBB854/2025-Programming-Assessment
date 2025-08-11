import pandas
import numpy

# lists to hold ticket details
all_sweets = ["Chocolate Bar", "Bubblegum Pack", "Sherbert Line", "Candyfloss", "Nerd Pack", "Mints", "Hi-chews",
              "Gummy Bears"]
all_sweets_costs = [4.50, 3, 0.5, 3.50, 3.99, 2.99, 2.50, 3.80, ]

sweets_dict = {
    'Name': all_sweets,
    'dirtbike Price': all_sweets_costs,
}

# create dataframe / table from dictionary
sweets_frame = pandas.DataFrame(sweets_dict)

# Rearranging index
sweets_frame.index = numpy.arange(1, len(sweets_frame) + 1)

print(sweets_frame)
print()
