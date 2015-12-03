
from dxfwrite import DXFEngine as dxf
import csv
import math

a = 8
A = 50
d = 10

points_list =[(0,A), (0,0), (A,0), (A,A), (0,A),(((A - a) / 2), ((A + a) / 2)), (((A - a) / 2), ((A - a) / 2)), (((A + a) / 2), ((A -a) / 2)), (((A + a) / 2), ((A + a) / 2)), (((A - a) / 2), ((A + a) / 2)), (((A - a - d) / 2), ((A + a + d) / 2)), (((A - a - d) / 2), ((A - a - d ) / 2)), (((A + a + d) / 2), ((A - a - d) / 2)), (((A + a + d) / 2), ((A + a + d) / 2)), (((A - a - d) / 2), ((A + a + d) / 2))]  


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

# all squares are drawn below:
drawing.add(dxf.polyline(points_list[0:5], color=7))
#polyline= dxf.polyline(linetype='DOT')
drawing.add(dxf.polyline(points_list[5:10], color=7))
drawing.add(dxf.polyline(points_list[10:15], color=7))

# Now the diagonal lines: 
drawing.add(dxf.line(points_list[0],points_list[5], color= 7))
drawing.add(dxf.line(points_list[1],points_list[6], color= 7))
drawing.add(dxf.line(points_list[2],points_list[7], color= 7))
drawing.add(dxf.line(points_list[3],points_list[8], color= 7))

drawing.save()
#drawing.add(polyline)
print "'" + drawing_name + ".dxf'", "file generated in the same directory"
