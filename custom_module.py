# Custom Module for import

# Time Travelling Function
def generate_time_travel_message(year, destination, cost, currency):
    """
    Generates a message prompt for time travelling.
    Parameters:
    year(int): The target year for time travel.
    destination(str): The destination for the time travel.
    cost(Decimal): The cost of the time travel.
    currency(str): The currency of the cost.
    """
    
    return f"Prepare for jump! You are travelling to {destination} in the year of {year}. The cost of the trip is {currency}{cost:.2f}."



