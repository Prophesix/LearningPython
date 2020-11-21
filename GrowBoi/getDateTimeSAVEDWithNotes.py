import datetime


print 'getDateTime 1.0'
print ''
print ' ,_ o'
print '/ //\,'
print ' \>> |'
print '  \\,'
print 'Created by: Alex Biglen'
print 'Date: 03/16/2019'

currentDT = datetime.datetime.now()
print ("Current Year is: %d" % currentDT.year)
print ("Current Month is: %d" % currentDT.month)
print ("Current Day is: %d" % currentDT.day)
print ("Current Hour is: %d" % currentDT.hour)
print ("Current Minute is: %d" % currentDT.minute)
print ("Current Second is: %d" % currentDT.second)
print ("Current Microsecond is: %d" % currentDT.microsecond)