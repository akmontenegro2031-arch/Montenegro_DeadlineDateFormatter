import calendar
event_title = input("Enter event title: ")
year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

month_name = calendar.month_name[month]
day_number = calendar.weekday(year, month, day)
day_name = calendar.day_name[day_number]

print("\nFormatted Output:")
print("Event:", event_title.upper())
print(f"Date: {month_name} {day}, {year}")
print("Year:", year)
print("Month:", month_name)
print("Day:", day)
print("Weekday:", day_name)