#to get current date and time we need to use the datetimelibrary
from datetime import datetime, timedelta

# the now function returns current date and time as a datetime object
today = datetime.now()

print('Today is: ' + str(today))
# You can use timedelta to add or remove days, or weeks to a date
#one_day = timedelta(days=1)
#yesterday = today - one_day
#print('Yesterday was: ' + str(yesterday))

one_week = timedelta(weeks=1)
last_week = today - one_week
print('Last week was: ' + str(last_week))