#Give Yourself Some Space
print (''' 

''')

# Begin the Assignment
print ("Begin Problem 1")
print ('''

''')

# Display Integer Variable
raw_input ("Would you like to see an integer?")
myint = 910
print (myint)
print ('''

''')
# Display Floating Point Variable
raw_input ("Would you like to see a floating point number now as well?")
myfloat = 7.98
print (myfloat)
print ('''

''')
# Display a "Copound" String Variable
raw_input ("Now would you like to see a string variable?")
first_name = raw_input ("What is your first name?")
last_name = raw_input ("What is your last name?")
full_name = (first_name + " " + last_name)
print (full_name)
print ('''

''')
# Use the Last Variable to Create a Boolean True/False Statement
my_string = (full_name)
my_string.startswith('M' or 'm' or 'D' or 'd')
print ("If you typed any combination of Mr. Gold or David Gold, the statement below returns true. If you typed anything else, it returns false.")
print (my_string.startswith('M' or 'm' or 'D' or 'd'))

print ("End of Problem 1")
print ('''

''')
print ("Begin Problem 2")

# Define Variables
D = ("Hello ")
E = ("World!")

# Put the Variables Together
F = (D+E)

# Display the End Result
print (F)
print ("End of Problem 2")
print ('''

''')
print ("Begin Problem 3")

# Python Program for Finding the Area of a Rectangle
width = float(input('Please enter the width of a rectangle: '))
height = float(input('Please enter the height of a rectangle: '))

# Calculate the Area
Area = width * height

# Calculate the Perimeter
Perimeter = 2 * (width + height)

print ("\n Area of the Rectange is: %.2f" %Area)
print (" Perimeter of the Rectange is: %.2f" %Perimeter)

print ("End of Problem 3")
