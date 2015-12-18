from dxfwrite import DXFEngine as dxf

import csv

import math

#a = 8
a = input("enter a: ")

#A = 80

A = input("enter A: ")

#D = 20

D = input("enter D: ")

#Dm = 10 

Dm = input("enter Dm: ")

if a < A/3 :
	print("A is always greater")

elif D < A/3 :
	print("D is greater than a")

else:
	print("wrong output")

#print('no. a',a, '!')



points_list = [((A - a) / 2, 2*D), ((A - a) / 2, D), (0, Dm), (0, 0), ((A - a) / 2, 0) , (A, 0), (A, Dm), ((A + a) / 2, D) , ((A + a) / 2, 2*D)]  


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

print "'" + drawing_name + ".dxf'", "file generated in the same directory"

#text
drawing.add(dxf.text('a', height=2, halign=CENTER, alignpoint=(38,35 )))
drawing.add(dxf.text('d/2', height=2, halign=CENTER, alignpoint=(30, 30)))
drawing.add(dxf.text('d/2', height=2, halign=CENTER, alignpoint=(50, 30)))
drawing.add(dxf.text('A', height=2, halign=CENTER, alignpoint=(38, -8)))
drawing.add(dxf.text('d', height=2, halign=CENTER, alignpoint=(35, 10)))
drawing.add(dxf.text('d\'', height=2, halign=CENTER, alignpoint=(27, 10)))
drawing.add(dxf.text('d\'\'', height=2, halign=CENTER, alignpoint=(56, 10)))
drawing.add(dxf.text('1', height=2, halign=CENTER, alignpoint=(25, -4)))
drawing.add(dxf.text('1\'', height=2, halign=CENTER, alignpoint=(54, -4)))

#a
drawing.add(dxf.line((36, 32), (44, 32)))
#arrw
drawing.add(dxf.line((36, 32), (37, 33)))
drawing.add(dxf.line((36, 32), (37, 31)))
#rught arrw
drawing.add(dxf.line((44, 32), (43, 33)))
drawing.add(dxf.line((44, 32), (43, 31)))

#d/2
drawing.add(dxf.line((25, 28), (34, 28)))
drawing.add(dxf.line((25, 32), (25, 0), layer='TESTLAYER',linetype='PHANTOMX2'))
#d/2 arrw
drawing.add(dxf.line((25, 28), (26, 29)))
drawing.add(dxf.line((25, 28), (26, 27)))
#d/2 right arrw
drawing.add(dxf.line((34, 28), (33, 29)))
drawing.add(dxf.line((34, 28), (33, 27)))
#d/2
drawing.add(dxf.line((46, 28), (54, 28)))
drawing.add(dxf.line((54, 32), (54, 0), layer='TESTLAYER',linetype='PHANTOMX2'))
#d/2 scnd lft arrw
drawing.add(dxf.line((46, 28), (47, 29)))
drawing.add(dxf.line((46, 28), (47, 27)))
#d/2 scnd rght arrw
drawing.add(dxf.line((54, 28), (53, 29)))
drawing.add(dxf.line((54, 28), (53, 27)))

#A
drawing.add(dxf.line((0, -5), (80, -5)))
drawing.add(dxf.line((0, -2), (0, -8)))
drawing.add(dxf.line((80, -2), (80, -8)))
#A arrow left
drawing.add(dxf.line((0, -5), (2, -3)))
drawing.add(dxf.line((0, -5), (2, -7)))
#A arrow rght
drawing.add(dxf.line((80, -5), (78, -3)))
drawing.add(dxf.line((80, -5), (78, -7)))

#D line
drawing.add(dxf.line((38, 20), (38, 0)))
#D uppr arrw
drawing.add(dxf.line((38, 20), (37, 19)))
drawing.add(dxf.line((38, 20), (39, 19)))
#D lwr arrw
drawing.add(dxf.line((38, 0), (37, 1)))
drawing.add(dxf.line((38, 0), (39, 1)))

#a line
drawing.add(dxf.line((41, 41), (41, 0), layer='TESTLAYER',linetype='PHANTOMX2'))


drawing.save()

