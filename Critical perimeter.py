from dxfwrite import DXFEngine as dxf
from dxfwrite.const import CENTER
import csv
import math
import pdb
a = 8
A = 50
d = 10

points_list =[(0,A), (0,0), (A,0), (A,A), (0,A),(((A - a) / 2), ((A + a) / 2)), (((A - a) / 2), ((A - a) / 2)), (((A + a) / 2), ((A -a) / 2)), (((A + a) / 2), ((A + a) / 2)), (((A - a) / 2), ((A + a) / 2)), (((A - a - d) / 2), ((A + a + d) / 2)), (((A - a - d) / 2), ((A - a - d ) / 2)), (((A + a + d) / 2), ((A - a - d) / 2)), (((A + a + d) / 2), ((A + a + d) / 2)), (((A - a - d) / 2), ((A + a + d) / 2))]  

pdb.set_trace()

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

# squares:
drawing.add(dxf.polyline(points_list[0:5], color=7))
drawing.add(dxf.polyline(points_list[5:10], color=7))
drawing.add(dxf.polyline(points_list[10:15], color=7))

# diagonal lines: 
drawing.add(dxf.line(points_list[0],points_list[5], color= 7))
drawing.add(dxf.line(points_list[1],points_list[6], color= 7))
drawing.add(dxf.line(points_list[2],points_list[7], color= 7))
drawing.add(dxf.line(points_list[3],points_list[8], color= 7))

print "'" + drawing_name + ".dxf'", "file generated in the same directory"

#text added
drawing.add(dxf.text('A', height=3.5, halign=CENTER, alignpoint=(94, 40)))
drawing.add(dxf.text('A', height=3.5, halign=CENTER, alignpoint=(40, -8)))
drawing.add(dxf.text('a', height=2, halign=CENTER, alignpoint=(60, 41)))
drawing.add(dxf.text('d/2', height=2, halign=CENTER, alignpoint=(47, 21)))
drawing.add(dxf.text('a', height=2, halign=CENTER, alignpoint=(38, 21)))
drawing.add(dxf.text('d/2', height=2, halign=CENTER, alignpoint=(33, 21)))
drawing.add(dxf.text('d/2', height=2, halign=CENTER, alignpoint=(60, 46)))
drawing.add(dxf.text('d/2', height=2, halign=CENTER, alignpoint=(60, 32)))
drawing.add(dxf.text('1', height=3, halign=CENTER, alignpoint=(30, 52)))
drawing.add(dxf.text('1\'', height=3, halign=CENTER, alignpoint=(50, 52)))
drawing.add(dxf.text('1', height=3, halign=CENTER, alignpoint=(30, 17)))
drawing.add(dxf.text('1\'', height=3, halign=CENTER, alignpoint=(50, 17)))
#A right
drawing.add(dxf.line((90, 80), (90, 0)))
drawing.add(dxf.line((88, 80), (92, 80)))
drawing.add(dxf.line((88, 0), (92, 0)))
#A right uppr arrw
drawing.add(dxf.line((90, 80), (88, 78)))
drawing.add(dxf.line((90, 80), (92, 78)))
#A rght bttm arrw
drawing.add(dxf.line((90, 0), (88, 2)))
drawing.add(dxf.line((90, 0), (92, 2)))

#A bttom
drawing.add(dxf.line((0, -10), (80, -10)))
drawing.add(dxf.line((0, -8), (0, -12)))
drawing.add(dxf.line((80, -8), (80, -12)))
#A lft bttm arrw
drawing.add(dxf.line((0, -10), (2, -8)))
drawing.add(dxf.line((0, -10), (2, -12)))
#A rght bttm arrw
drawing.add(dxf.line((80, -10), (78, -8)))
drawing.add(dxf.line((80, -10), (78, -12)))

#center lines
drawing.add(dxf.line((40, 80), (40, 0), layer='TESTLAYER',linetype='PHANTOMX2'))
drawing.add(dxf.line((0, 40), (80, 40), layer='TESTLAYER',linetype='PHANTOMX2'))
#d/2
drawing.add(dxf.line((55, 49), (55, 45)))
drawing.add(dxf.line((49, 45), (58, 45)))
drawing.add(dxf.line((52, 49), (58, 49)))
#d/2 arrw upper
drawing.add(dxf.line((55, 49), (54, 48)))
drawing.add(dxf.line((55, 49), (56, 48)))
#d/2 arrw lwr
drawing.add(dxf.line((55, 45), (54, 46)))
drawing.add(dxf.line((55, 45), (56, 46)))

#a
drawing.add(dxf.line((55, 45), (55, 36)))
drawing.add(dxf.line((49, 36), (58, 36)))
#a uppr arrw
drawing.add(dxf.line((55, 45), (54, 44)))
drawing.add(dxf.line((55, 45), (56, 44)))
#a lwr arrw
drawing.add(dxf.line((55, 36), (54, 37)))
drawing.add(dxf.line((55, 36), (56, 37)))

#d/2
drawing.add(dxf.line((55, 36), (55, 31)))
drawing.add(dxf.line((52, 31), (58, 31)))
#d/2 uppr arrw
drawing.add(dxf.line((55, 36), (54, 35)))
drawing.add(dxf.line((55, 36), (56, 35)))
#d/2 lwr arrw
drawing.add(dxf.line((55, 31), (54, 32)))
drawing.add(dxf.line((55, 31), (56, 32)))

#d/2 bttm line
drawing.add(dxf.line((31, 25), (36, 25)))
#d/2 rght bttm
drawing.add(dxf.line((36, 31), (36, 23)))
#d/2 bttm lft line
drawing.add(dxf.line((31, 27), (31, 23)))
#d/2 bttm lft arrw
drawing.add(dxf.line((31, 25), (32, 24)))
drawing.add(dxf.line((31, 25), (32, 26)))
#d/2 bttm rght arrw
drawing.add(dxf.line((36, 25), (35, 24)))
drawing.add(dxf.line((36, 25), (35, 26)))
#a bttm line
drawing.add(dxf.line((36, 25), (44, 25)))
drawing.add(dxf.line((44, 31), (44, 22)))
#d/2 bttm line rght
drawing.add(dxf.line((44, 25), (49, 25)))
drawing.add(dxf.line((49, 23), (49, 27)))
#d/2 bttm line lft arrw
drawing.add(dxf.line((44, 25), (45, 24)))
drawing.add(dxf.line((44, 25), (45, 26)))
#d/2 bttm line lft arrw
drawing.add(dxf.line((49, 25), (48, 24)))
drawing.add(dxf.line((49, 25), (48, 26)))
#a bttm lft arrw
drawing.add(dxf.line((36, 25), (37, 24)))
drawing.add(dxf.line((36, 25), (37, 26)))
# a bttm rght arrw
drawing.add(dxf.line((44, 25), (43, 24)))
drawing.add(dxf.line((44, 25), (43, 26)))

drawing.save()

