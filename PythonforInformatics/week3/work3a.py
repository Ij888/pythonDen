totalHours = raw_input("Enter Hours Worked: ")
rate = raw_input("Enter Rate: ")
totalHours, rate = float(), float()

#someString = str()
#someString = 'boo ya'

if totalHours <= 40:
	payLoad = totalHours*rate
	print (payLoad)
else totalHours > 40:
	print ((payLoad) + (5*rate*1.5))
#else:
	#print 'DONE!!'