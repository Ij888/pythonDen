rawHours = raw_input("Enter Hours Worked: ")
rawRate = raw_input("Enter Rate: ")
totalHours = float(rawHours)
rate = float(rawRate)

if totalHours <= 40:
	payLoad = totalHours*rate
	print (payLoad)
elif totalHours > 40:
	print (((totalHours-5)*rate) + (5*rate*1.5))
else:
	print 'DONE!!'