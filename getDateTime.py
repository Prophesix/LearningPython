import datetime


print ('getDateTime 1.0')
print ('')
print (' ,_ o')
print ('/ //\,')
print (' \>> |')
print ('  \\,')
print ('Created by: Alex Biglen')
print ('Date: 03/16/2019')

currentDT = datetime.datetime.now()
print ("Current Year is: %d" % currentDT.year)
print ("Current Month is: %d" % currentDT.month)
print ("Current Day is: %d" % currentDT.day)
print ("Current Hour is: %d" % currentDT.hour)
print ("Current Minute is: %d" % currentDT.minute)
print ("Current Second is: %d" % currentDT.second)
print ("Current Microsecond is: %d" % currentDT.microsecond)

#----NOTES ON PYTHON DATES----

#%a	Locale’s abbreviated weekday name.
#%A	Locale’s full weekday name.
#%b	Locale’s abbreviated month name.
#%B	Locale’s full month name.
#%c	Locale’s appropriate date and time representation.
#%d	Day of the month as a decimal number [01,31].
#%H	Hour (24-hour clock) as a decimal number [00,23].
#%I	Hour (12-hour clock) as a decimal number [01,12].
#%j	Day of the year as a decimal number [001,366].
#%m	Month as a decimal number [01,12].
#%M	Minute as a decimal number [00,59].
#%p	Locale’s equivalent of either AM or PM.
#%S	Second as a decimal number [00,61].
#%U	Week number of the year (Sunday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Sunday are considered to be in week 0.
#%w	Weekday as a decimal number [0(Sunday),6].
#%W	Week number of the year (Monday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Monday are considered to be in week 0.
#%x	Locale’s appropriate date representation.
#%X	Locale’s appropriate time representation.
#%y	Year without century as a decimal number [00,99].
#%Y	Year with century as a decimal number.
#%z	Time zone offset indicating a positive or negative time difference from UTC/GMT of the form +HHMM or -HHMM, where H represents decimal hour digits and M represents decimal minute digits [-23:59, +23:59].
#%Z	Time zone name (no characters if no time zone exists).
#%%	A literal '%' character.