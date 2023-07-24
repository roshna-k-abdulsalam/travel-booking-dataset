import pandas as pd
import numpy as np

# Read the customer table CSV file
customer_table = pd.read_csv('travel-booking/customer.csv')

# Read the destination table CSV file
destination_table = pd.read_csv('travel-booking/destination.csv')


# Shuffle the rows of the customer and destination tables
shuffled_customer_table = customer_table.reindex(np.random.permutation(customer_table.index))
shuffled_destination_table = destination_table.reindex(np.random.permutation(destination_table.index))

# Determine the number of bookings to create
num_bookings = len(shuffled_customer_table)

# Create the booking table by merging customer and destination tables
booking_table = pd.DataFrame()
booking_table['booking_id'] = np.arange(1, num_bookings + 1)
booking_table['customer_id'] = shuffled_customer_table['customer_id'].tolist()
booking_table['booking_date'] = pd.date_range(start='2023-06-01', periods=num_bookings)
booking_table['destination'] = np.random.choice(shuffled_destination_table['destination'], size=num_bookings)
booking_table['number_of_passengers'] = np.random.randint(1, 6, size=num_bookings)
booking_table['cost_per_passenger'] = np.random.randint(100, 200, size=num_bookings)

# Reorder the columns if desired
booking_table = booking_table[['booking_id', 'customer_id', 'booking_date', 'destination', 'number_of_passengers', 'cost_per_passenger']]

# Load the booking table to a csv file
booking_table.to_csv('travel-booking/booking.csv')
