import datetime
currentDate = datetime.date.today()

strDueDate = input("Enter a due date for the project in mm/dd/yyyy format")
dueDate = datetime.datetime.strptime(strDueDate,"%m/%d/%Y").date() # strptime puts a string into a date format
# strftime formats an existing date

daysLeft = dueDate - currentDate

print(f"You have {daysLeft} days left to finish your project.")
