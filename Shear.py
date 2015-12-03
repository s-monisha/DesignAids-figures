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

drawing.save()
print "'" + drawing_name + ".dxf'", "file generated in the same directory"
