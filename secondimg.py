from dxfwrite import DXFEngine as dxf

import csv

import math



a = 8

A = 80

D = 20

Dm = 8


dist_of_arrow_from_footing_base = 10 # say
no_of_arrows = 10 # say



points_list = [((A - a) / 2, 2*D), ((A - a) / 2, D), (0, Dm), (0, 0), ((A - a) / 2, 0) , (A, 0), (A, Dm), ((A + a) / 2, D) , ((A + a) / 2, 2*D)]   

# print points_list[1]

# # print len(points_list[1])

# print len(str(points_list[1]))



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
drawing.save()
print "'" + drawing_name + ".dxf'", "file generated in the same directory"

