from dxfwrite import DXFEngine as dxf
import csv
import math
from dxfwrite.const import CENTER

def dim12_arrow(u1, u2, u3, u4, l1, l2, l3, l4, c1, c2, c3, c4):
    drawing.add(dxf.line((c1, c2), (c3, c4)))
    drawing.add(dxf.line((u1, u2), (u3, u4)))
    drawing.add(dxf.line((l1, l2), (l3, l4)))

def dim4_arrow(l11, l12, l13, l14):
    drawing.add(dxf.line((l11, l12), (l13, l14)))

def atrace(t1, t2, t3, t4, t5, t6):
    drawing.add(dxf.trace([(t1, t2), (t3, t4), (t5, t6)]))

text_size = 2.5

# input file
f=open('Critical perimeter.csv')
lst={'A':'','a':'','d':''}
data=[row for row in csv.reader(f)]
for i in lst.keys():
    for j in range(len(data)):
            if(i==data[j][0]):
                    ans=data[j][1]
                    break;
    lst[i]=int(ans)

points_list =[(0,lst['A']), (0,0), (lst['A'],0), (lst['A'],lst['A']), (0,lst['A']),(((lst['A'] - lst['a']) / 2), ((lst['A'] + lst['a']) / 2)),
                            (((lst['A'] - lst['a']) / 2), ((lst['A'] - lst['a']) / 2)), (((lst['A'] + lst['a']) / 2), ((lst['A'] -lst['a']) / 2)),
                            (((lst['A'] + lst['a']) / 2), ((lst['A'] + lst['a']) / 2)), (((lst['A'] - lst['a']) / 2), ((lst['A'] + lst['a']) / 2)),
                            (((lst['A'] - lst['a'] - lst['d']) / 2), ((lst['A'] + lst['a'] + lst['d']) / 2)),
                            (((lst['A'] - lst['a'] - lst['d']) / 2), ((lst['A'] - lst['a'] - lst['d'] ) / 2)),
                            (((lst['A'] + lst['a'] + lst['d']) / 2), ((lst['A'] - lst['a'] - lst['d']) / 2)),
                            (((lst['A'] + lst['a'] + lst['d']) / 2), ((lst['A'] + lst['a'] + lst['d']) / 2)),
                            (((lst['A'] - lst['a'] - lst['d']) / 2), ((lst['A'] + lst['a'] + lst['d']) / 2))]

string_for_csv = str()
for i in xrange(len(points_list)):

    string_for_csv = string_for_csv + str(points_list[i][0]) + "," + str(points_list[i][1]) + "\n"


# csv file
inp = raw_input("Enter the name of csv file you want to generate: ")
fw = open(inp+".csv", "w")
fw.write(string_for_csv)

# dxf drawing
drawing_name = raw_input("Enter a drawing name to be created without the extension dxf: ")
drawing = dxf.drawing(drawing_name+".dxf")

# Squares:
drawing.add(dxf.line(points_list[0],points_list[1], color=7))
drawing.add(dxf.line(points_list[1],points_list[2], color=7))
drawing.add(dxf.line(points_list[2],points_list[3], color=7))
drawing.add(dxf.line(points_list[3],points_list[4], color=7))
drawing.add(dxf.line(points_list[4],points_list[5], color=7))
drawing.add(dxf.line(points_list[5],points_list[6], color=7))
drawing.add(dxf.line(points_list[6],points_list[7], color=7))
drawing.add(dxf.line(points_list[7],points_list[8], color=7))
drawing.add(dxf.line(points_list[8],points_list[9], color=7))
drawing.add(dxf.line(points_list[9],points_list[10], color=7))
drawing.add(dxf.line(points_list[10],points_list[11], color=7, layer='TESTLAYER',linetype='DASHEDX2'))
drawing.add(dxf.line(points_list[11],points_list[12], color=7,  layer='TESTLAYER',linetype='DASHEDX2'))
drawing.add(dxf.line(points_list[12],points_list[13], color=7,  layer='TESTLAYER',linetype='DASHEDX2'))
drawing.add(dxf.line(points_list[13],points_list[14], color=7,  layer='TESTLAYER',linetype='DASHEDX2'))

# Diagonal lines:
drawing.add(dxf.line(points_list[0],points_list[5], color= 7))
drawing.add(dxf.line(points_list[1],points_list[6], color= 7))
drawing.add(dxf.line(points_list[2],points_list[7], color= 7))
drawing.add(dxf.line(points_list[3],points_list[8], color= 7))

# text
drawing.add(dxf.text('A', height=text_size, halign=CENTER, alignpoint=(115, 50)))
drawing.add(dxf.text('A', height=text_size, halign=CENTER, alignpoint=(50, -8)))
drawing.add(dxf.text('a', height=text_size, halign=CENTER, alignpoint=(85, 52)))
drawing.add(dxf.text('d/2', height=text_size, halign=CENTER, alignpoint=(85, 65)))
drawing.add(dxf.text('a', height=text_size, halign=CENTER, alignpoint=(48, 21)))
drawing.add(dxf.text('d/2', height=text_size, halign=CENTER, alignpoint=(35, 21)))
drawing.add(dxf.text('d/2', height=text_size, halign=CENTER, alignpoint=(64, 21)))
drawing.add(dxf.text('d/2', height=text_size, halign=CENTER, alignpoint=(85, 34)))
drawing.add(dxf.text('1', height=text_size, halign=CENTER, alignpoint=(30, 73)))
drawing.add(dxf.text('1\'', height=text_size, halign=CENTER, alignpoint=(70,73 )))
drawing.add(dxf.text('1', height=text_size, halign=CENTER, alignpoint=(30, 17)))
drawing.add(dxf.text('1\'', height=text_size, halign=CENTER, alignpoint=(70, 17)))


# A upperright
dim12_arrow(108, 100, 112, 100, 110, 100, 110, 0, 108, 0, 112, 0)
atrace(109.5, 97, 110.5, 97, 110, 100)
atrace(109.5, 3, 110.5, 3, 110, 0)

# A bottom
dim12_arrow(0, -8, 0, -12, 0, -10, 100, -10, 100, -8, 100, -12)
atrace(3, -9.5 , 3, -10.5 , 0, -10)
atrace(97, -9.5, 97, -10.5, 100, -10)

# Center lines
drawing.add(dxf.line((50, 100), (50, 0), layer='TESTLAYER',linetype='CENTER'))
drawing.add(dxf.line((0, 50), (100, 50), layer='TESTLAYER',linetype='CENTER'))

# d/2
dim12_arrow(77, 70, 82, 70,80, 70, 80, 60, 68, 60, 82, 60)
atrace(79.5, 67, 80.5, 67, 80, 70)
atrace(79.5, 63, 80.5, 63, 80, 60)

# a
dim4_arrow(80, 60, 80, 40)
atrace(79.5, 57, 80.5, 57,80, 60)
atrace(79.5, 43, 80.5, 43,80, 40)

# d/2
dim12_arrow(77, 30, 82, 30, 80, 40, 80, 30, 68, 40, 82, 40)
atrace(79.5, 33, 80.5, 33, 80, 30)
atrace(79.5, 37, 80.5, 37, 80, 40)

# d/2 bottom
dim12_arrow(30, 27, 30,23, 30, 25, 40, 25, 40, 31, 40, 23)
atrace(33, 24.5, 33, 25.5, 30, 25)
atrace(37, 24.5, 37, 25.5, 40, 25)

# a bottom
dim4_arrow(40, 25, 60, 25)
atrace(43, 24.5, 43, 25.5, 40, 25)
atrace(57, 24.5, 57, 25.5, 60, 25)

# d/2 bottom
dim12_arrow(70, 23, 70, 27, 60, 25, 70, 25, 60, 31, 60, 22)
atrace(63, 24.5, 63, 25.5, 60, 25)
atrace(67, 24.5, 67, 25.5, 70, 25)

drawing.save()
