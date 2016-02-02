from dxfwrite import DXFEngine as dxf
import csv
import math
from dxfwrite.const import CENTER
#import pdb


# input file
f=open('Developstepfoot(a).csv')
lst={'A':'','D':'','a':'','ClearCover':'','Dia':''}
data=[row for row in csv.reader(f)]
for i in lst.keys():
    for j in range(len(data)):
            if(i==data[j][0]):
                    ans=data[j][1]
                    break;
    lst[i]=int(ans)

# text size
textsize = 2.5

# arrows/lines function
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

points_list = [((lst['A']-lst['a']) / 2, 2*lst['D']), ((lst['A']-lst['a']) / 2, lst['D']), (0, lst['D']), (0, 0),
                        (lst['A'], 0), (lst['A'], lst['D']), ((lst['A'] + lst['a']) / 2, lst['D']), ((lst['A'] + lst['a']) / 2, 2*lst['D']), ((lst['A'] - 2 *lst['a']) / 2, 2*lst['D']), ((lst['A'] -  lst['a']) / 2, 2*lst['D']), ((lst['A'] - lst['a']) / 2 + (lst['a'] / 3), 2*lst['D']),
                        ((lst['A'] / 2), (lst['a'] / 3) + 2*lst['D']),  ((lst['A'] / 2), 2*lst['D'] - (lst['a'] / 3)),
                        ((lst['A'] + lst['a']) / 2 - (lst['a'] / 3), 2*lst['D']), ((lst['A'] + lst['a'])/ 2, 2*lst['D']), ((lst['A'] + 2*lst['a']) / 2, 2*lst['D']),
               (2, 2 + lst['Dia']), (lst['A'] - 2, 2 + lst['Dia']), (lst['A'] - 2, 2), (2, 2), (2, 2 + lst['Dia'])]


string_for_csv = str()
for i in xrange(len(points_list)):
    string_for_csv = string_for_csv + str(points_list[i][0]) + "," + str(points_list[i][1]) + "\n"

# csv file
inp = raw_input("Enter the name of csv file you want to generate: ")
fw = open(inp+'.csv', "w")
fw.write(string_for_csv)

# dxf drawing
drawing_name = raw_input("Enter a drawing name to be created without the extension dxf: ")
drawing = dxf.drawing(drawing_name+".dxf")

# pdb.set_trace()
# lines
def drawline(points_list):
    for i in range(len(points_list) - 1):
        if(i==7):
            continue
        elif(i==15):
            continue
        c = tuple(points_list[i])
        d = tuple(points_list[i+1])
        drawing.add(dxf.line(c, d, color=7))

drawline(points_list)


# circle code
no_of_bars_above = 9

some_space_at_end = 5
center_to_center = ((lst['A'] - lst['ClearCover'] * 2 - some_space_at_end * 2) / float(no_of_bars_above - 1))
center_of_first_bar = (lst['ClearCover'] + some_space_at_end, lst['ClearCover'] + lst['Dia'] + lst['Dia'] / 2.0)

x_coord_of_center_of_bars = [(center_of_first_bar[0] + i * center_to_center) for i in xrange(no_of_bars_above)]
for x in x_coord_of_center_of_bars:
    drawing.add(dxf.circle(lst['Dia'] / 2.0, (x, center_of_first_bar[1])))


# text
drawing.add(dxf.text('a', height=textsize, halign=CENTER, alignpoint=(50, 33)))
drawing.add(dxf.text('D', height=textsize, halign=CENTER, alignpoint=(115, 8)))
drawing.add(dxf.text('A', height=textsize, halign=CENTER, alignpoint=(50, -10)))
drawing.add(dxf.text('4', height=textsize, halign=CENTER, alignpoint=(-10, -13)))
drawing.add(dxf.text('4', height=textsize, halign=CENTER, alignpoint=
                  (106, -4)))
drawing.add(dxf.text('y > L\U+0501',height=textsize, halign=CENTER, alignpoint=(18, -15)))
drawing.add(dxf.text('Sloped footing', height=textsize, halign=CENTER, alignpoint=(20, 33)))
drawing.add(dxf.text('Uniformly deep footing', height=textsize, halign=CENTER, alignpoint=(80, 33)))


# D
# def dim12_arrow(u1, u2, u3, u4, l1, l2, l3, l4, c1, c2, c3, c4):
dim12_arrow(108, 20, 112, 20, 110, 20, 110, 0, 108, 0, 112, 0)
atrace(109.5, 17, 110.5, 17, 110, 20)
atrace(109.5, 3, 110.5, 3, 110, 0)

# A
# def dim12_arrow(u1, u2, u3, u4, l1, l2, l3, l4, c1, c2, c3, c4):
dim12_arrow(0, -3, 0, -7, 0, -5, 100, -5, 100, -3, 100, -7)
atrace(3, -4.5, 3, -5.5, 0, -5)
atrace(97, -4.5, 97, -5.5, 100, -5)

# a
# def dim4_arrow(l21, l22, l23, l24):
dim4_arrow(45, 30, 55, 30)
atrace(48, 29.5, 48, 30.5, 45, 30)
atrace(52, 29.5, 52, 30.5, 55, 30)


# 4
dim8_arrow(102, 0, 106, 0, 104, 0, 104, -8)
atrace(103.5, -3, 104.5, -3, 104, 0)

# 4 upper
dim8_arrow(102, 2, 106, 2, 104, 2, 104, 10)
atrace(103.5, 5, 104.5, 5, 104, 2)

# 4 lft side
dim8_arrow(0, -9, 0, -13, 0, -11, -8, -11)
atrace(-3, -10.5, -3, -11.5, 0, -11)

# 4/ ld  rght side
dim8_arrow(2, -9, 2, -13, 2, -11, 45, -11)
atrace(5, -10.5, 5, -11.5, 2, -11)

# ld
dim4_arrow(45, -9, 45, -13)
atrace(42, -10.5, 42, -11.5, 45, -11)

# sloped footing
dim4_arrow(25, 20, 25, 30)
atrace(24.5, 23, 25.5, 23, 25, 20)

# uniformly deep
dim4_arrow(75, 20, 75, 30)
atrace(74.5, 23, 75.5, 23, 75, 20)
drawing.add(dxf.line((45, 20), (0, 15), layer='TESTLAYER',linetype='PHANTOMX2'))
drawing.add(dxf.line((55, 20), (100, 15), layer='TESTLAYER',linetype='PHANTOMX2'))
drawing.save()
