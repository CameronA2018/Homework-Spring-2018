inputString = raw_input('Please supply a sentence of words. If there are any capital words, I will find them and show them to you. ')

splitInput = inputString.split()

Upper = inputString.upper()

splitUP = Upper.split()

w = len(splitInput)
y = w - w
x = 0

returnlist = []

while(y < w):
	UPsplit = splitUP[y]
	Inputsplit = splitInput[y]
	if(UPsplit == Inputsplit):
		returnlist.append(splitInput[x])
	y = y + 1
	x = x + 1
print (returnlist)
