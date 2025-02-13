# create initial version of Time Traveler's Toolkit

import custom_module as cm
import datetime as dt
import decimal as decimal
from random import randint, choice


# Set current date and time
date = dt.datetime.today()
time = dt.datetime.now().time()

# Retrieve current date and time
print(f"Today's date is {date.strftime('%Y-%M-$D')}. The current {time.strftime('%H:%M')}.")
current_year = date.year

# Base cost for Time Travel
base_cost = decimal.Decimal(1500.00)
target_year = int(input("Enter the year you wish to visit: "))
difference = abs(target_year - current_year)
cost_multiplier = decimal('1.5')
final_cost = base_cost + (decimal(difference) * cost_multiplier)
final_cost = final_cost.quantize(decimal('0.01'))

# Randomly select a destination
destinations = ["Ancient Rome", "Medieval Europe", "The Distant Future", "Jurassic Era", "Renaissance Italy"]
selected_destination = choice(destinations)

# Generate and display the time travel message
message = cm.generate_time_travel_message(target_year, selected_destination, final_cost)
print("\n" + message)

