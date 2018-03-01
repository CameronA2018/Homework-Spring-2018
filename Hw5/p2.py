currentNumber = int(raw_input('Please supply an integer: '))

if((currentNumber % 2) == 0):
	print ('EVEN')
	print (currentNumber/2)
if((currentNumber % 2) != 0):
	print ('ODD')
	print ((currentNumber+1)*3)
