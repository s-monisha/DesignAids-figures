from dxfwrite import DXFEngine as dxf
from dxfwrite.const import CENTER
import csv
import math

a = 10
A = 100
D = 25

column_length = 2*D 
dist_of_arrow_from_footing_base = 10 
no_of_arrows = 10 

points_list = [((A-a) / 2, 2*D), ((A-a) / 2, D), (0, D), (0, 0), (A, 0), (A, D), ((A + a) / 2, D), ((A + a) / 2, 2*D), ((A - 2*a) / 2, 2*D), ((A -  a) / 2, 2*D), ((A - a) / 2 + (a / 3), 2*D), ((A / 2), (a / 3) + 2*D),  ((A / 2), 2*D - (a / 3)), ((A + a) / 2 - (a / 3), 2*D), ((A + 2*a) / 2, 2*D)]

string_for_csv = str()
for i in xrange(len(points_list)):
    string_for_csv = string_for_csv + str(points_list[i][0]) + "," + str(points_list[i][1]) + "\n"

print string_for_csv

inp = raw_input("Enter the name of csv file you want to generate: ")
fw = open(inp+".csv", "w")

fw.write(string_for_csv)

print "'" + inp + ".csv'", "file generated in the same directory"

drawing_name = raw_input("Enter a drawing name to be created without the extension dxf: ")
drawing = dxf.drawing(drawing_name+".dxf")

# polyline= dxf.polyline()

drawing.add(dxf.polyline(points_list, color=7))

#arrow base line:

left_point = 0, -dist_of_arrow_from_footing_base
right_point = A,-dist_of_arrow_from_footing_base

drawing.add(dxf.line(left_point,right_point, color=7))


length_arrow = 3
angle_arrow = 30 # in degrees
def arrow(bottom_point,arrow_point):
    drawing.add(dxf.line(bottom_point,arrow_point, color= 7))
    drawing.add(dxf.line( (arrow_point[0] - math.sin(math.radians(angle_arrow)) * length_arrow , arrow_point[1] - math.cos(math.radians(angle_arrow)) * length_arrow ) ,arrow_point, color = 7))
    drawing.add(dxf.line( (arrow_point[0] + math.sin(math.radians(angle_arrow)) * length_arrow , arrow_point[1] - math.cos(math.radians(angle_arrow)) * length_arrow) ,arrow_point, color = 7))
    return
list_xcoordinates_for_arrows = [(float(A)/(no_of_arrows - 1))*i for i in xrange(no_of_arrows + 1)]
list_bottom_points = zip(list_xcoordinates_for_arrows,[-dist_of_arrow_from_footing_base] * no_of_arrows)
list_arrow_points = zip(list_xcoordinates_for_arrows,[0] * no_of_arrows)
final_arrow_points = zip(list_bottom_points,list_arrow_points)

for i in xrange(len(final_arrow_points)):
    arrow(final_arrow_points[i][0], final_arrow_points[i][1])


#text

drawing.add(dxf.text('a', height=3, halign=CENTER, alignpoint=(50, 33)))
drawing.add(dxf.text('D', height=3, halign=CENTER, alignpoint=(115, 8)))
drawing.add(dxf.text('A', height=3.5, halign=CENTER, alignpoint=(50, -18)))
drawing.add(dxf.text('P (kN)', height=3, halign=CENTER, alignpoint=(50, 53)))
drawing.add(dxf.text('p(kN/m ^ 2)', height=3, halign=CENTER, alignpoint=(-15, -8)))

#p(kn)
#upper
drawing.add(dxf.line((-12, 0), (-8, 0)))
drawing.add(dxf.line((-10, 10), (-10, 0)))
drawing.add(dxf.line((-10, 0), (-12, 2)))
drawing.add(dxf.line((-10, 0), (-8, 2)))
#lower
drawing.add(dxf.line((-12, -10), (-8, -10)))
drawing.add(dxf.line((-10, -10), (-10, -20)))
drawing.add(dxf.line((-10, -10), (-12, -12)))
drawing.add(dxf.line((-10, -10), (-8, -12)))
#D
drawing.add(dxf.line((110, 20), (110, 0)))
drawing.add(dxf.line((108, 20), (112, 20)))
drawing.add(dxf.line((108, 0), (112, 0)))
#d arrow
drawing.add(dxf.line((110, 20), (108, 18)))
drawing.add(dxf.line((110, 20), (112, 18)))
#d scnd arrow
drawing.add(dxf.line((110, 0), (108, 2)))
drawing.add(dxf.line((110, 0), (112, 2)))
#A
drawing.add(dxf.line((0, -20), (100, -20)))
drawing.add(dxf.line((0, -18), (0, -22)))
drawing.add(dxf.line((100, -18), (100, -22)))
#left side
drawing.add(dxf.line((0, -20), (2, -18)))
drawing.add(dxf.line((0, -20), (2, -22)))
#right side
drawing.add(dxf.line((100, -20), (98, -18)))
drawing.add(dxf.line((100, -20), (98, -22)))
#a
drawing.add(dxf.line((45, 30), (55, 30)))
#a arrw lft
drawing.add(dxf.line((45,30), (47,32)))
drawing.add(dxf.line((45,30), (47,28)))
#a arrw rght
drawing.add(dxf.line((55,30), (53,32)))
drawing.add(dxf.line((55,30), (53,28)))
#P(kn)
drawing.add(dxf.line((50, 52), (50, 45)))
drawing.add(dxf.line((50, 45), (48, 47)))
drawing.add(dxf.line((50, 45), (52, 47)))

drawing.save()

print "'" + drawing_name + ".dxf'", "file generated in the same directory"



