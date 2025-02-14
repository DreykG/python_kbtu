from datetime import * 
from dateutil.relativedelta import *

# 1)Write a Python program to subtract five days from current date.
dat = date.today()
print(f"From current date - 5 days, will be: {dat - timedelta(days=5)}")
# TIMEDELTA uses for minus or plus days,hour, seconds and etc.
# relativedelta(months=3) for mounths.

# 2) Write a Python program to print yesterday, today, tomorrow.
current_data = date.today()
print(f'''
Date:
Yesterday: {current_data - timedelta(days=1)}
Today: {current_data}
Tomorrow: {current_data + timedelta(days=1)}
''')


# 3) Write a Python program to drop microseconds from datetime.
current_date = datetime.today()
formated_date = current_date.strftime("%Y.%m.%d %H-%M-%S")
#strftime() need for fromating our current data. WE can drop microseconds,seconds,minutes and etc.
print(f"Current date without microseconds: {formated_date}")


# 4) Write a Python program to calculate two date difference in seconds.
current_date = datetime.today()
input("Just push ENTER when need for calculating diffirent in seconds!\n")
later_date = datetime.today()
diffirence = later_date - current_date
seconds = diffirence.total_seconds()
print(f"Diffirence between two date in seconds: {round(seconds,2)}")

#OR

date_1 = datetime(2021, 9, 8, 23, 15, 38)
date_2 = datetime(1934, 5, 21, 7, 11, 57)
diff = abs(date_1 - date_2)
print(f"Diffirence between two date in seconds: {diff.total_seconds()}")