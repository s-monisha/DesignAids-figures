from dxfwrite import DXFEngine as dxf
import csv
import math
from dxfwrite.const import CENTER
from math import pi, sin, cos

# arrows/lines function
def dim12_arrow(u1, u2, u3, u4, l1, l2, l3, l4, c1, c2, c3, c4):
    drawing.add(dxf.line((c1, c2), (c3, c4)))
    drawing.add(dxf.line((u1, u2), (u3, u4)))
    drawing.add(dxf.line((l1, l2), (l3, l4)))

def dim8_arrow(u11, u12, u13, u14, l11, l12, l13, l14):
    drawing.add(dxf.line((u11, u12), (u13, u14)))
    drawing.add(dxf.line((l11, l12), (l13, l14)))

def dim5_arrow(r1, (c1, c2), st1, ed1):
    drawing.add(dxf.arc(r1, (c1, c2), st1, ed1))

def dim4_arrow(l21, l22, l23, l24):
    drawing.add(dxf.line((l21, l22), (l23, l24)))

def atrace(t1, t2, t3, t4, t5, t6):
    drawing.add(dxf.trace([(t1, t2), (t3, t4), (t5, t6)]))


# input file
f=open('criticalfooting(b).csv')
lst={'A':'','D':'','a':'','Dm':'','ClearCover':'','Dia':''}
data=[row for row in csv.reader(f)]
for i in lst.keys():
    for j in range(len(data)):
            if(i==data[j][0]):
                    ans=data[j][1]
                    break;
    lst[i]=int(ans)

points_list = [((lst['A'] - lst['a']) / 2, 2*lst['D']), ((lst['A'] - lst['a']) / 2, lst['D']), (0, lst['Dm']), (0, 0), ((lst['A'] - lst['a']) / 2, 0) ,
                               (lst['A'], 0), (lst['A'], lst['Dm']), ((lst['A'] + lst['a']) / 2, lst['D']) , ((lst['A'] + lst['a']) / 2, 2*lst['D']), ((lst['A'] - 2*lst['a']) / 2, 2*lst['D']),
                               ((lst['A'] -  lst['a']) / 2, 2*lst['D']), ((lst['A'] - lst['a']) / 2 + (lst['a'] / 3), 2*lst['D']), ((lst['A'] / 2), (lst['a'] / 3) + 2*lst['D']),
                               ((lst['A'] / 2), 2*lst['D'] - (lst['a'] / 3)), ((lst['A'] + lst['a']) / 2 - (lst['a'] / 3), 2*lst['D']), ((lst['A'] + 2*lst['a']) / 2, 2*lst['D']),
                               (2, 2 + lst['Dia']), (lst['A'] - 2, 2 + lst['Dia']), (lst['A'] - 2, 2), (2, 2), (2, 2 + lst['Dia'])]


# csv points
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

# text

drawing.add(dxf.text('a', height=2.5, halign=CENTER, alignpoint=(39,34 )))
drawing.add(dxf.text('d', height=2.5, halign=CENTER, alignpoint=(24, 30)))
drawing.add(dxf.text('D\'', height=2.5, halign=CENTER, alignpoint=(-8, 5)))
drawing.add(dxf.text('A', height=2.5, halign=CENTER, alignpoint=(40.5, -7)))
drawing.add(dxf.text('d', height=2.5, halign=CENTER, alignpoint=(39, 10)))
drawing.add(dxf.text('d\'', height=2.5, halign=CENTER, alignpoint=(24, 10)))
drawing.add(dxf.text('D', height=2.5, halign=CENTER, alignpoint=(92, 10)))
drawing.add(dxf.text('Dm', height=2.5, halign=CENTER, alignpoint=(85, 3)))
drawing.add(dxf.text('2', height=2.5, halign=CENTER, alignpoint=(10, -6)))
drawing.add(dxf.text('1', height=2.5, halign=CENTER, alignpoint=(36, -6)))

# a
dim4_arrow(36, 32, 44, 32)
atrace(39, 32.5, 39, 31.5, 36, 32)
atrace(41, 32.5, 41, 31.5, 44, 32)

# d
dim4_arrow(10, 28, 36, 28)
atrace(13, 28.5, 13, 27.5, 10, 28)
atrace(33, 28.5, 33, 27.5, 36, 28)
drawing.add(dxf.line((10, 31), (10, -3), layer='TESTLAYER',linetype='PHANTOMX2'))

# A
dim12_arrow(0, -6, 0, -10, 0, -8, 80, -8, 80, -6, 80, -10)
atrace(3, -7.5, 3, -8.5, 0, -8)
atrace(77, -7.5, 77, -8.5, 80, -8)

# D line
dim8_arrow(38, 20, 38, 3, 37, 20, 39, 20)
atrace(37.5, 17, 38.5, 17, 38, 20)
atrace(37.5, 6, 38.5, 6, 38, 3)

# a line
drawing.add(dxf.line((36, 32), (44, 32), layer='TESTLAYER',linetype='PHANTOMX2'))
drawing.add(dxf.trace([(39, 32.5), (39, 31.5), (36, 32)]))
drawing.add(dxf.trace([(41, 32.5), (41,31.5 ), (44, 32)]))
drawing.add(dxf.line((40.5, 43), (40.5, -3), layer='TESTLAYER',linetype='PHANTOMX2'))

# D'
drawing.add(dxf.line((22, 13), (-7, 13), layer='TESTLAYER',linetype='PHANTOMX2'))
drawing.add(dxf.line((-5, 0), (-5, 13)))
drawing.add(dxf.line((-7, 0), (-3, 0)))
drawing.add(dxf.trace([(-5.5, 3), (-4.5, 3), (-5, 0)]))
drawing.add(dxf.trace([(-5.5, 10), (-4.5, 10), (-5, 13)]))

# d'
drawing.add(dxf.line((20, 13), (20, 3)))
drawing.add(dxf.trace([(19.5, 6), (20.5, 6), (20, 3)]))
drawing.add(dxf.trace([(19.5, 10), (20.5, 10), (20, 13)]))

# dm
drawing.add(dxf.line((83, 8), (87, 8)))
drawing.add(dxf.line((83, 0), (87, 0)))
drawing.add(dxf.line((85, 8), (85, 16)))
drawing.add(dxf.line((85, 0), (85, -8)))
drawing.add(dxf.trace([(84.5, 11), (85.5, 11), (85, 8)]))
drawing.add(dxf.trace([(84.5, -3), (85.5, -3), (85, 0)]))


# D
drawing.add(dxf.line((90, 20), (90, 0)))
drawing.add(dxf.line((88, 0), (92, 0)))
drawing.add(dxf.line((88, 20), (92, 20)))
drawing.add(dxf.trace([(89.5, 17), (90.5, 17), (90, 20)]))
drawing.add(dxf.trace([(89.5, 3), (90.5, 3), (90, 0)]))

# 1
drawing.add(dxf.line((36, 42), (36, -3), layer='TESTLAYER',linetype='PHANTOMX2'))

# circle code
def fill_circle(radius, center, fineness = 36):
    circle_points = [((center[0] + radius * cos(2 * pi / fineness * i)),
                      (center[1] + radius * sin(2 * pi / fineness * i)))
                     for i in xrange(fineness + 1)]
    for i in xrange(fineness):
        drawing.add(dxf.trace([circle_points[i], circle_points[i + 1],
                               center]))
    return

no_of_bars_above = 9
some_space_at_end = 2
center_to_center = ((lst['A'] - lst['ClearCover'] * 2 - some_space_at_end
                     * 2) / float(no_of_bars_above - 1))

center_of_first_bar = (lst['ClearCover'] + some_space_at_end,
                       lst['ClearCover'] + lst['Dia'] + lst['Dia'] / 2.0)

x_coord_of_center_of_bars = [(center_of_first_bar[0] + i * center_to_center)
                             for i in xrange(no_of_bars_above)]

for x in x_coord_of_center_of_bars:
    fill_circle(lst['Dia'] / 2.0, (x, center_of_first_bar[1]),
                fineness = 36)

drawing.save()
