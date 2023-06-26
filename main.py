import time

# Get the current time in seconds
current_time = time.time()

# Format the current time as a string
current_time_formatted = time.ctime(current_time)

# Get the number of hours required from the driver
hours_required = float(input("Enter the number of hours required: "))

# Calculate the expiry time in seconds
expiry_time = current_time + (hours_required * 3600)

# Format the expiry time as a string
expiry_time_formatted = time.ctime(expiry_time)

# Calculate the charge based on the number of hours
if hours_required <= 2:
    charge = 3.50
elif hours_required <= 4:
    charge = 5.00
else:
    charge = 10.00

# Print the current time, expiry time, and charge
print("Time now:", current_time_formatted)
print("Expires:", expiry_time_formatted)
print("Charge =", charge)
