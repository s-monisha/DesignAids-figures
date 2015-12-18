from dxfwrite import DXFEngine as dxf

import csv

import math

from dxfwrite.const import CENTER


a = 8

A = 80

D = 25

Dm = 15

a_ = 35


dist_of_arrow_from_footing_base = 10 
no_of_arrows = 10 



points_list = [((A - a) / 2, 2*D), ((A - a) / 2, D), ((A - a_) / 2, D), ((A - a_) / 2, Dm), (0, Dm) , (0, 0), (A, 0), (A, Dm) , ((A + a_) / 2, Dm), ((A + a_) / 2, D), ((A + a) / 2, D), ((A +a) / 2, 2*D)]     


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


length_arrow = 5
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

drawing.add(dxf.text('a', height=4.5, halign=CENTER, alignpoint=(40, 40)))
drawing.add(dxf.text('D', height=4.5, halign=CENTER, alignpoint=(105, 10)))
drawing.add(dxf.text('A', height=4.5, halign=CENTER, alignpoint=(40, -18)))
drawing.add(dxf.text('p(kn/cm)', height=4.5, halign=CENTER, alignpoint=(-30, -8)))
drawing.add(dxf.text('P(kN)', height=4.5, halign=CENTER, alignpoint=(40, 55)))
drawing.add(dxf.text('Dm', height=4.5, halign=CENTER, alignpoint=(90, 20)))
drawing.add(dxf.text('a_', height=3, halign=CENTER, alignpoint=(30, 30)))

#p(kn)
drawing.add(dxf.line((-10, 0), (-10, -10))) 
drawing.add(dxf.line((-12, 0), (-8, 0))) 
drawing.add(dxf.line((-12, -10), (-8, -10))) 
#D
drawing.add(dxf.line((100, 25), (100, 0))) 
drawing.add(dxf.line((98, 25), (102, 25)))                             
drawing.add(dxf.line((98, 0), (102, 0))) 
#A
drawing.add(dxf.line((10, -20), (70, -20))) 
drawing.add(dxf.line((10, -18), (10, -22))) 
drawing.add(dxf.line((70, -18), (70, -22))) 
#a
drawing.add(dxf.line((36, 40), (44, 40)))
#dm
drawing.add(dxf.line((90, 15), (90, 0)))                             
drawing.add(dxf.line((88, 15), (92, 15)))                             
drawing.add(dxf.line((88, 0), (92, 0))) 
#a_ line
drawing.add(dxf.line((27, 31), (55, 31))) 


drawing.save()
