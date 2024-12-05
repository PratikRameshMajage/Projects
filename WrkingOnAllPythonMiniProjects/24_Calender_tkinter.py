import calendar

# Get user input for year and month
year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))

# Create a calendar object
cal = calendar.monthcalendar(year, month)

# Print the calendar header
print(calendar.month_name[month] + " " + str(year))
print("Mo Tu We Th Fr Sa Su")

# Print the calendar body
for week in cal:
    for day in week:
        if day == 0:
            print("  ", end="")
        else:
            print("{0:2d}".format(day), end=" ")
    print()