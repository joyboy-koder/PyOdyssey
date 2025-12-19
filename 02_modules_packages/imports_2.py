import random
import math
import datetime
import calendar
import os


courses = ['Math', 'Science', 'English', 'Art']

random_choice = random.choice(courses)
print(random_choice)

rads = math.radians(90)
print(rads)

today = datetime.date.today()
print(today)

isLeap = calendar.isleap(2020)
print(isLeap)

print(os.__file__)