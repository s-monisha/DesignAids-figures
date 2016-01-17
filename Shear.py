from dxfwrite import DXFEngine as dxf
import csv
import math
from dxfwrite.const import CENTER

# functions
def dim12_arrow(u1, u2, u3, u4, l1, l2, l3, l4, c1, c2, c3, c4):
    drawing.add(dxf.line((c1, c2), (c3, c4)))
    drawing.add(dxf.line((u1, u2), (u3, u4)))
    drawing.add(dxf.line((l1, l2), (l3, l4)))

def dim8_arrow(u11, u12, u13, u14, l11, l12, l13, l14):
    drawing.add(dxf.line((u11, u12), (u13, u14)))
    drawing.add(dxf.line((l11, l12), (l13, l14)))

def dim4_arrow(l21, l22, l23, l24):
    drawing.add(dxf.line((l21, l22), (l23, l24)))

def atrace(t1, t2, t3, t4, t5, t6):
    drawing.add(dxf.trace([(t1, t2), (t3, t4), (t5, t6)]))

# textsize
textsize = 2.5

# input file
f=open('shear.csv')
lst={'A':'','D':'','a':'','Dm':'','ClearCover':'','Dia':''}
data=[row for row in csv.reader(f)]
for i in lst.keys():
    for j in range(len(data)):
            if(i==data[j][0]):
                    ans=data[j][1]
                    break;
    lst[i]=int(ans)

points_list = [((lst['A'] - lst['a']) / 2, 2*lst['D']),
               ((lst['A'] - lst['a']) / 2, lst['D']),
               (0, lst['Dm']), (0, 0), ((lst['A'] - lst['a']) / 2, 0) ,
                               (lst['A'], 0), (lst['A'], lst['Dm']),
               ((lst['A'] + lst['a']) / 2, lst['D']) ,
               ((lst['A'] + lst['a']) / 2, 2*lst['D']),
               ((lst['A'] - 2*lst['a']) / 2, 2*lst['D']),
                               ((lst['A'] -  lst['a']) / 2, 2*lst['D']),
               ((lst['A'] - lst['a']) / 2 + (lst['a'] / 3), 2*lst['D']),
               ((lst['A'] / 2), (lst['a'] / 3) + 2*lst['D']),
                           ((lst['A'] / 2), 2*lst['D'] - (lst['a'] / 3)),
               ((lst['A'] + lst['a']) / 2 - (lst['a'] / 3), 2*lst['D']),
               ((lst['A'] + 2*lst['a']) / 2, 2*lst['D']),
                               (2, 2 + lst['Dia']),
               (lst['A'] - 2, 2 + lst['Dia']),
               (lst['A'] - 2, 2), (2, 2), (2, 2 + lst['Dia'])]

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

# line
def drawline(points_list):
    for i in range(len(points_list) - 1):
            if(i==8):
                continue
            elif(i==15):
                continue
            c = tuple(points_list[i])
            d = tuple(points_list[i+1])
            drawing.add(dxf.line(c, d, color=7))

drawline(points_list)

#text
drawing.add(dxf.text('a', height=textsize, halign=CENTER, alignpoint=(39,34 )))
drawing.add(dxf.text('d/2', height=textsize, halign=CENTER, alignpoint=(31, 30)))
drawing.add(dxf.text('d/2', height=textsize, halign=CENTER, alignpoint=(49, 30)))
drawing.add(dxf.text('A', height=textsize, halign=CENTER, alignpoint=(40.5, -7)))
drawing.add(dxf.text('d', height=textsize, halign=CENTER, alignpoint=(35, 10)))
drawing.add(dxf.text('d\'', height=textsize, halign=CENTER, alignpoint=(24, 10)))
drawing.add(dxf.text('d\'\'', height=textsize, halign=CENTER, alignpoint=(56, 10)))
drawing.add(dxf.text('1', height=textsize, halign=CENTER, alignpoint=(26, -4)))
drawing.add(dxf.text('1\'', height=textsize, halign=CENTER, alignpoint=(54, -4)))

# a
dim4_arrow(36, 32, 44, 32)
atrace(39, 32.5, 39, 31.5, 36, 32)
atrace(41, 32.5, 41, 31.5, 44, 32)

# d/2
drawing.add(dxf.line((26, 28), (36, 28)))
drawing.add(dxf.line((26, 31), (26, -1), layer='TESTLAYER',linetype='PHANTOMX2'))
drawing.add(dxf.trace([(29, 28.5), (29, 27.5), (26, 28)]))
drawing.add(dxf.trace([(33, 28.5), (33, 27.5), (36, 28)]))

# d/2
drawing.add(dxf.line((44, 28), (54, 28)))
drawing.add(dxf.line((54, 31), (54, -1), layer='TESTLAYER',linetype='PHANTOMX2'))
drawing.add(dxf.trace([(47, 28.5), (47, 27.5), (44, 28)]))
drawing.add(dxf.trace([(51, 28.5), (51, 27.5), (54, 28)]))

# A
dim12_arrow(0, -6, 0, -10, 0, -8, 80, -8, 80, -6, 80, -10)
atrace(3, -7.5, 3, -8.5, 0, -8)
atrace(77, -7.5, 77, -8.5, 80, -8)

# D
dim8_arrow(38, 20, 38, 3, 37, 20, 39, 20)
atrace(37.5, 17, 38.5, 17, 38, 20)
atrace(37.5, 6, 38.5, 6, 38, 3)

#a line
drawing.add(dxf.line((36, 32), (44, 32), layer='TESTLAYER',linetype='PHANTOMX2'))
drawing.add(dxf.trace([(39, 32.5), (39, 31.5), (36, 32)]))
drawing.add(dxf.trace([(41, 32.5), (41,31.5 ), (44, 32)]))
drawing.add(dxf.line((40.5, 43), (40.5, -3), layer='TESTLAYER',linetype='PHANTOMX2'))

drawing.save()
