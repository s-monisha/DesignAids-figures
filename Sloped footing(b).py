from dxfwrite import DXFEngine as dxf

import csv

import math

import pdb

a = 8

A = 80

D = 20

Dm = 10 


dist_of_arrow_from_footing_base = 10 
no_of_arrows = 10 

pdb.set_trace()

points_list = [((A - a) / 2, 2*D), ((A - a) / 2, D), ((A - a - D) / 2, D), (0, Dm), (0, 0), ((A - a) / 2, 0) , (A, 0), (A, Dm), ((A + a + D) / 2, D) , ((A + a) / 2, D), ((A + a) / 2, 2*D),((A - 2*a) / 2, 2*D), ((A -  a) / 2, 2*D), ((A - a) / 2 + (a / 3), 2*D), ((A / 2), (a / 3) + 2*D),  ((A / 2), 2*D - (a / 3)), ((A + a) / 2 - (a / 3), 2*D), ((A + 2*a) / 2, 2*D)]

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

print "'" + drawing_name + ".dxf'", "file generated in the same directory"

#text

drawing.add(dxf.text('a', height=2.5, halign=CENTER, alignpoint=(40, 35)))
drawing.add(dxf.text('D', height=4, halign=CENTER, alignpoint=(105, 10)))
drawing.add(dxf.text('A', height=4, halign=CENTER, alignpoint=(40, -18)))
drawing.add(dxf.text('p(kN/m ^ 2)', height=3.5, halign=CENTER, alignpoint=(-20, -8)))
drawing.add(dxf.text('P (kN)', height=4, halign=CENTER, alignpoint=(40, 58)))
drawing.add(dxf.text('Dm', height=4, halign=CENTER, alignpoint=(90, 8)))
drawing.add(dxf.text('D/2', height=3, halign=CENTER, alignpoint=(30, 30)))
drawing.add(dxf.text('D/2', height=3, halign=CENTER, alignpoint=(50, 30)))


#p(kn/m)
drawing.add(dxf.line((-12, 0), (-8, 0)))
drawing.add(dxf.line((-12, -10), (-8, -10)))
#p(kn/m) arrow
drawing.add(dxf.line((-10, 10), (-10, 0)))
drawing.add(dxf.line((-10, 0), (-12, 2)))
drawing.add(dxf.line((-10, 0), (-8, 2)))
#p(kn/m) arrow
drawing.add(dxf.line((-10, -10), (-10, -20)))
drawing.add(dxf.line((-10, -10), (-12, -12)))
drawing.add(dxf.line((-10, -10), (-8, -12)))

#D
drawing.add(dxf.line((100, 25), (100, 0)))
drawing.add(dxf.line((98, 25), (102, 25)))
drawing.add(dxf.line((98, 0), (102, 0)))
#d arrow
drawing.add(dxf.line((100, 25), (98, 22)))
drawing.add(dxf.line((100, 25), (102, 22)))
#d lowr arroe
drawing.add(dxf.line((100, 0), (98, 2)))
drawing.add(dxf.line((100, 0), (102, 2)))

#A
drawing.add(dxf.line((0, -20), (80, -20)))
drawing.add(dxf.line((0, -18), (0, -22)))
drawing.add(dxf.line((80, -18), (80, -22)))
#A arrow left
drawing.add(dxf.line((0, -20), (2, -18)))
drawing.add(dxf.line((0, -20), (2, -22)))
#A arrow rght
drawing.add(dxf.line((80, -20), (78, -18)))
drawing.add(dxf.line((80, -20), (78, -22)))

#a
drawing.add(dxf.line((36, 32), (44, 32)))
#arrw
drawing.add(dxf.line((36, 32), (38, 34)))
drawing.add(dxf.line((36, 32), (38, 30)))
#rught arrw
drawing.add(dxf.line((44, 32), (42, 34)))
drawing.add(dxf.line((44, 32), (42, 30)))

#dm
drawing.add(dxf.line((88, 15), (92, 15)))
drawing.add(dxf.line((88, 0), (92, 0)))
#arrow dm
drawing.add(dxf.line((90, 20), (90, 15)))
drawing.add(dxf.line((90, 15), (88, 17)))
drawing.add(dxf.line((90, 15), (92, 17)))
#arrow dm lowr
drawing.add(dxf.line((90, 0), (90, -10)))
drawing.add(dxf.line((90, 0), (88, -2)))
drawing.add(dxf.line((90, 0), (92, -2)))

#beta
drawing.add(dxf.line((2, 10), (10, 10)))
drawing.add(dxf.line((78, 10), (70, 10)))
#beta arrw
drawing.add(dxf.line((5, 18), (5, 13)))
drawing.add(dxf.line((5, 13), (3, 15)))
drawing.add(dxf.line((5, 13), (7, 15)))
#beta scnd arrw
drawing.add(dxf.line((78, 18), (78, 13)))
drawing.add(dxf.line((78, 13), (76, 15)))
drawing.add(dxf.line((78, 13), (80, 15)))
#d/2
drawing.add(dxf.line((25, 28), (34, 28)))
drawing.add(dxf.line((25, 32), (25, 24)))
#d/2 arrw
drawing.add(dxf.line((25, 28), (27, 29)))
drawing.add(dxf.line((25, 28), (27, 27)))
#d/2 right arrw
drawing.add(dxf.line((34, 28), (32, 29)))
drawing.add(dxf.line((34, 28), (32, 27)))
#d/2
drawing.add(dxf.line((46, 28), (54, 28)))
drawing.add(dxf.line((54, 32), (54, 24)))
#d/2 scnd lft arrw
drawing.add(dxf.line((46, 28), (47, 29)))
drawing.add(dxf.line((46, 28), (47, 27)))
#d/2 scnd rght arrw
drawing.add(dxf.line((54, 28), (52, 29)))
drawing.add(dxf.line((54, 28), (52, 27)))

#p(kn)
drawing.add(dxf.line((40, 55), (40, 45)))
drawing.add(dxf.line((40, 45), (38, 48)))
drawing.add(dxf.line((40, 45), (42, 48)))

drawing.save()
