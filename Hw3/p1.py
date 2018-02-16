# Define Integers
int1 = 1
int2 = 2
int3 = int1 + int2
int4 = float(int1) / float(int2)

# Display Integer
print (int3)

# Display Floating Point Variable
print (int4)

# Display String Variable
print ("Hello")

# Display Boolean Variable
HoursofSleep = int(input('Please supply hours of sleep you got last night: '))
StupidPeopleDealtWith = int(input('Please supply number of stupid people dealt with: '))
HoursofHomework = int(input('Please supply hours of homework for tonight: '))

HappyCameron = HoursofSleep >= 6 and StupidPeopleDealtWith <= 2 and HoursofHomework <= 2


if(HappyCameron == False):
	HappyCameron = "Alan is Unhappy"

if(HappyCameron == True):
	HappyCameron = "Alan is Happy"

print (HappyCameron)
