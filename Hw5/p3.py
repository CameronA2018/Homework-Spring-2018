stuff = raw_input('Please supply a list of words separated by commas: ')
lowerStuff = stuff.lower()
words = lowerStuff.split(",")
item1 = words[0]
item2 = words[1]
item3 = words[2]
item4 = words[3]
item5 = words[4]

if((len(words)% 2) != 0):
	print ('This is ODD')
	if("llama" in lowerStuff):
		print (words)
if(len(item1)%2 != 0):
	if(len(item2)%2 != 0):
		if(len(item3)%2 != 0):
			if(len(item4)%2 != 0):
				if(len(item5)%2 != 0):
					print ('This is ODD')
