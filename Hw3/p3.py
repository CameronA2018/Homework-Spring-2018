# Define Width and Height of a Polygon
base = float(input('Please give the base length of a polygon: '))

# Define the Formula for Area of a Square
area_square = (base**2)

# Display Area of a Square
print ("If a Square, " + str(area_square) + " units squared")

# Define the Formula of a Triangle
area_tri_pt1 = 3.0**(.5)
area_tri_pt2 = area_tri_pt1 / 4.0
area_tri_pt3 = area_tri_pt2 * (base**2.0)
# Display Area of a Triangle
print ("If an Equilateral Triangle, " + str(area_tri_pt3) + " units squared")

#Define the Formula of a Pentagon
area_pent_pt1 = (((5**.5)*2)+5)
area_pent_pt2 = ((5*area_pent_pt1)**.5)
area_pent_pt3 = ((.25*area_pent_pt2)*(base**2.0))

# Display Area of a Pentagon
print ("If a Pentagon, " + str(area_pent_pt3) + " units squared")
