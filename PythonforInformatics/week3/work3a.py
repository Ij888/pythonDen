totalHours = raw_input("Enter Hours Worked: ")
rate = raw_input("Enter Rate: ")
totalHours = float()
rate = float()

payLoad = totalHours*rate

if totalHours <= 40:
	print (payLoad)
elif totalHours > 40:
	print ((payLoad) + (5*rate*1.5))
else:
	print 'DONE!!'