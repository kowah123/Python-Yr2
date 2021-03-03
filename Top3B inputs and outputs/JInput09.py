# Enter two doubles representing the length and width of a rectangle.
#  Calculate and display (1) the area and (2) the perimeter.
# e.g.
#   1. Area of the rectangle = 12 sq. metres
#   2. Perimeter of the rectangle = 14 metres.

# length = 4 sq.metres
# width = 3 metres

length = int(input("length :"))
width = int(input("width :"))

print("Area of the rectangle = " + str(length *  width) + " sq.meter")
print("Perimeter of the rectangle = " + str(2 * (length + width)) + " metres.")