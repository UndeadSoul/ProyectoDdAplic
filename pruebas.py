import time
from datetime import date
today = date.today()
# today

# today == date.fromtimestamp(time.time())

# my_birthday = date(today.year, 6, 24)
# if my_birthday < today:
#     my_birthday = my_birthday.replace(year=today.year + 1)

# my_birthday

# time_to_birthday = abs(my_birthday - today)
# time_to_birthday.days
print("dia",type(today.day))
print("mes",today.month)
print("año",today.year)

# {str(today.day)+'/'+str(today.month)+'/'+str(today.year)}