from dxfwrite import DXFEngine as dxf
from dxfwrite.const import CENTER
import csv
import math
#import pdb

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

def dim5_arrow(r1, (c1, c2), st1, ed1):
    drawing.add(dxf.arc(r1, (c1, c2), st1, ed1))

def dim4_arrow(l21, l22, l23, l24):
    drawing.add(dxf.line((l21, l22), (l23, l24)))

def atrace(t1, t2, t3, t4, t5, t6):
    drawing.add(dxf.trace([(t1, t2), (t3, t4), (t5, t6)]))

# input file
f=open('Sloped footing(b).csv')
lst={'A':'','D':'','a':'','Dm':''}
data=[row for row in csv.reader(f)]
for i in lst.keys():
    for j in range(len(data)):
            if(i==data[j][0]):
                    ans=data[j][1]
                    break;
    lst[i]=int(ans)

# pdb.set_trace()
points_list = [((lst['A'] - lst['a']) / 2, 2*lst['D']),
               ((lst['A'] - lst['a']) / 2, lst['D']),
               ((lst['A'] - lst['a'] - lst['D']) / 2, lst['D']),
               (0, lst['Dm']), (0, 0), ((lst['A'] - lst['a']) / 2, 0) ,
               (lst['A'], 0), (lst['A'], lst['Dm']),
               ((lst['A'] + lst['a'] + lst['D']) / 2, lst['D']) ,
               ((lst['A'] + lst['a']) / 2, lst['D']),
               ((lst['A'] + lst['a']) / 2, 2*lst['D']),
               ((lst['A'] - 2*lst['a']) / 2, 2*lst['D']),
               ((lst['A'] -  lst['a']) / 2, 2*lst['D']),
               ((lst['A'] - lst['a']) / 2 + (lst['a'] / 3), 2*lst['D']),
               ((lst['A'] / 2), (lst['a'] / 3) + 2*lst['D']),
               ((lst['A'] / 2), 2*lst['D'] - (lst['a'] / 3)),
               ((lst['A'] + lst['a']) / 2 - (lst['a'] / 3), 2*lst['D']),
               ((lst['A'] + 2*lst['a']) / 2, 2*lst['D'])]

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
            if(i==10):
                continue
            c = tuple(points_list[i])
            d = tuple(points_list[i+1])
            drawing.add(dxf.line(c, d, color=7))

drawline(points_list)

# arrow base line:

dist_of_arrow = 10
no_of_arrows = 10

left_point = 0, -dist_of_arrow
right_point = lst['A'],-dist_of_arrow
drawing.add(dxf.line(left_point,right_point, color=7))

# arrow
def arrow(bottom_point,arrow_point, length_arrow = 3):
    drawing.add(dxf.line(bottom_point,arrow_point, color= 7))
    vertex = arrow_point
    left_pt = (arrow_point[0] - length_arrow / 6.0 , arrow_point[1] - length_arrow )
    right_pt = (arrow_point[0] + length_arrow / 6.0 , arrow_point[1] - length_arrow)
    drawing.add(dxf.trace([vertex, left_pt, right_pt]))
    return
list_xcoordinates_for_arrows = [(float(lst['A'])/(no_of_arrows - 1))*i
                                for i in xrange(no_of_arrows + 1)]
list_bottom_points = zip(list_xcoordinates_for_arrows,[-dist_of_arrow] * no_of_arrows)
list_arrow_points = zip(list_xcoordinates_for_arrows,[0] * no_of_arrows)
final_arrow_points = zip(list_bottom_points,list_arrow_points)

for i in xrange(len(final_arrow_points)):
    arrow(final_arrow_points[i][0], final_arrow_points[i][1])


# text
drawing.add(dxf.text('a', height=textsize, halign=CENTER, alignpoint=(40, 34)))
drawing.add(dxf.text('D', height=textsize, halign=CENTER, alignpoint=(105, 10)))
drawing.add(dxf.text('A', height=textsize, halign=CENTER, alignpoint=(40, -18)))
drawing.add(dxf.text('p (kN/m\u00B2)', height=textsize, halign=CENTER, alignpoint=(-17, -7)))
drawing.add(dxf.text('P (kN)', height=textsize, halign=CENTER, alignpoint=(40, 58)))
drawing.add(dxf.text('Dm', height=textsize, halign=CENTER, alignpoint=(90, 3)))
drawing.add(dxf.text('D/2', height=textsize, halign=CENTER, alignpoint=(30, 30)))
drawing.add(dxf.text('D/2', height=textsize, halign=CENTER, alignpoint=(50, 30)))
drawing.add(dxf.text(u"\u03B2", height=textsize, halign=CENTER, alignpoint=(12, 10)))
drawing.add(dxf.text(u"\u03B2", height=textsize, halign=CENTER, alignpoint=(69, 10)))


# p(kN/m)
dim8_arrow(-12, 0, -8, 0, -10, 10, -10, 0)
atrace(-10.5, 3, -9.5, 3, -10, 0)

# p(kN/m)lower
dim8_arrow(-12, -10, -8, -10, -10, -10, -10, -20)
atrace(-10.5, -13, -9.5, -13, -10, -10)

# D
dim12_arrow(98, 20, 102, 20, 100, 20, 100, 0, 98, 0, 102, 0)
atrace(99.5, 17, 100.5, 17, 100, 20)
atrace(99.5, 3, 100.5, 3, 100, 0)

# A
dim12_arrow(0, -18, 0, -22, 0, -20, 80, -20, 80, -18, 80, -22)
atrace(3, -19.5, 3, -20.5, 0, -20)
atrace(77, -19.5, 77, -20.5, 80, -20)

# a
dim4_arrow(36, 32, 44, 32)
atrace(39, 32.5, 39, 31.5, 36, 32)
atrace(41, 32.5, 41, 31.5, 44, 32)

# dm
dim8_arrow(88, 10, 92, 10, 90, 10, 90, 20)
atrace(89.5, 13, 90.5, 13, 90, 10)

# dm lower
dim8_arrow(88, 0, 92, 0, 90, 0, 90, -10)
atrace(89.5, -3, 90.5, -3, 90, 0)

# beta
dim8_arrow(2, 10, 10, 10, 78, 10, 71, 10)
dim5_arrow(4.6, (0, 15), 4.1, 90)
atrace(4, 16, 5, 16, 4.5, 13)
dim5_arrow(5.1, (80, 15), 110, 170)
atrace(74.5, 16, 75.5, 16, 75, 13)

# d/2
dim8_arrow(26, 28, 34, 28, 26, 31, 26, 24)
atrace(29, 28.5, 29, 27.5, 26, 28)
atrace(33, 28.5, 33, 27.5, 36, 28)

# d/2
dim8_arrow(44, 28, 54, 28, 54, 31, 54, 24)
atrace(47, 28.5, 47, 27.5, 44, 28)
atrace(51, 28.5, 51, 27.5, 54, 28)

# p(kn)
dim4_arrow(40, 55, 40, 45)
atrace(39.5, 48, 40.5, 48, 40, 45)

drawing.save()
