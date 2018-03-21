name = 'My name is BOB'
hello = 'I think that we have met before. 1 time maybe?'
screw = 'This peice of wood will require 7 screws to stay properly attached.'
goodbye = "I'm going home. It is way too late. It is nearly 4 in the morning."

list = []
list.append(name)
list.append(hello)
list.append(screw)
list.append(goodbye)

def getIntegers(list):
	x = 0
	while(x<4):
		splitter = list[x]
		splitList = splitter.split()
		x = x + 1
		print (splitList)
