name = raw_input('Please supply you whole name (first, middle, last): ')

upper_name = name.upper()

names = name.split()
first = names[0]
middle = names[1]
last = names[2]

center = len(middle)/2
midfir = middle[0:center]
midlas = middle[-center:]
whole = (first + " " + midfir + "-BOB-" + midlas + " " + last)

bakfir = names[0]
bakmid = names[1]
baklas = names[2]
back_fir = bakfir[::-1]
back_mid = bakmid[::-1]
back_las = baklas[::-1]
space = " "
back_name = back_fir + space + back_mid + space + back_las

print (upper_name)
print (back_name)
print (whole)
