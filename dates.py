#to get current date and time we need to use the datetimelibrary
from datetime import datetime

current_date = datetime.now()
# the now function returns current date and time as a datetime object

# You must convert the datetime object to a string
# before you can concatenate it to another string
print('Today is: ' + str(current_date))