import datetime

# Get current date and time
now = datetime.datetime.now()

# Display date and time
print("Current Date and Time:")
print("Date:", now.date())
print("Time:", now.time())

# Or display in formatted string
print("Formatted:", now.strftime("%Y-%m-%d %H:%M:%S"))
