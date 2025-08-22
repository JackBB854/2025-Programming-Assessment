import pandas
import numpy

# lists to hold ticket details
all_sweets = ["Sherbet Line",
              "Hi-Chews",
              "Mints",
              "Mystery Bag",
              "Hi-chews",
              "Turkish Delight",
              "Chocolate Bars",
              "Gummy Bears",
              "Caramel Eclairs",
              "Nerd Pack", ]
all_sweets_costs = [1, 2, 2, 2, 2, 2, 3, 4, 4, 5, ]

sweets_dict = {
    'Name': all_sweets,
    'Sweets Price': all_sweets_costs,
}

# create dataframe / table from dictionary
sweets_frame = pandas.DataFrame(sweets_dict)

# Rearranging index
sweets_frame.index = numpy.arange(1, len(sweets_frame) + 1)

print(sweets_frame)
print()
