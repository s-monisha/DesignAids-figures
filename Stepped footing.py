from dxfwrite import DXFEngine as dxf
import csv
import math
from dxfwrite.const import CENTER

a = 8
A = 80
D = 25
Dm = 15
a_ = 35

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


points_list = [((A - a) / 2, 2*D), ((A - a) / 2, D), ((A - a_) / 2, D),
               ((A - a_) / 2, Dm), (0, Dm) , (0, 0), (A, 0), (A, Dm) ,
               ((A + a_) / 2, Dm), ((A + a_) / 2, D), ((A + a) / 2, D),
               ((A +a) / 2, 2*D), ((A - 2*a) / 2, 2*D), ((A -  a) / 2, 2*D),
               ((A - a) / 2 + (a / 3), 2*D), ((A / 2), (a / 3) + 2*D),
               ((A / 2), 2*D - (a / 3)), ((A + a) / 2 - (a / 3), 2*D),
               ((A + 2*a) / 2, 2*D)]


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

# lines
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
drawing.add(dxf.line(points_list[10],points_list[11], color=7))
drawing.add(dxf.line(points_list[12],points_list[13], color=7))
drawing.add(dxf.line(points_list[13],points_list[14], color=7))
drawing.add(dxf.line(points_list[14],points_list[15], color=7))
drawing.add(dxf.line(points_list[15],points_list[16], color=7))
drawing.add(dxf.line(points_list[16],points_list[17], color=7))
drawing.add(dxf.line(points_list[17],points_list[18], color=7))

# arrow base line:
dist_of_arrow = 10
no_of_arrows = 10

left_point = 0, -dist_of_arrow
right_point = A,-dist_of_arrow

drawing.add(dxf.line(left_point,right_point, color=7))

# arrow
def arrow(bottom_point,arrow_point, length_arrow = 3):
    drawing.add(dxf.line(bottom_point,arrow_point, color= 7))
    vertex = arrow_point
    left_pt = (arrow_point[0] - length_arrow / 6.0 , arrow_point[1] - length_arrow )
    right_pt = (arrow_point[0] + length_arrow / 6.0 , arrow_point[1] - length_arrow)
    drawing.add(dxf.trace([vertex, left_pt, right_pt]))
    return
list_xcoordinates_for_arrows = [(float(A)/(no_of_arrows - 1))*i
                                for i in xrange(no_of_arrows + 1)]
list_bottom_points = zip(list_xcoordinates_for_arrows,[-dist_of_arrow] * no_of_arrows)
list_arrow_points = zip(list_xcoordinates_for_arrows,[0] * no_of_arrows)
final_arrow_points = zip(list_bottom_points,list_arrow_points)

for i in xrange(len(final_arrow_points)):
    arrow(final_arrow_points[i][0], final_arrow_points[i][1])


# text size
textsize = 2.5

drawing.add(dxf.text('a', height=textsize, halign=CENTER, alignpoint=(40, 43)))
drawing.add(dxf.text('D', height=textsize, halign=CENTER, alignpoint=(105, 10)))
drawing.add(dxf.text('A', height=textsize, halign=CENTER, alignpoint=(40, -18)))
drawing.add(dxf.text('p (kN/m\u00B2)', height=textsize, halign=CENTER, alignpoint=(-16, -7)))
drawing.add(dxf.text('P (kN)', height=textsize, halign=CENTER, alignpoint=(40, 63)))
drawing.add(dxf.text('Dm', height=textsize, halign=CENTER, alignpoint=(90, 5)))
drawing.add(dxf.text('a\'', height=textsize, halign=CENTER, alignpoint=(30, 35)))
drawing.add(dxf.text('1\'', height=textsize, halign=CENTER, alignpoint=(20, 43)))
drawing.add(dxf.text('2\'', height=textsize, halign=CENTER, alignpoint=(10, 43)))
drawing.add(dxf.text('1\'', height=textsize, halign=CENTER, alignpoint=(22, -25)))
drawing.add(dxf.text('2\'', height=textsize, halign=CENTER, alignpoint=(10, -25)))

# p(kn/m)
dim8_arrow(-12, 0, -8, 0, -10, 0, -10, 10)
atrace(-10.5, 3, -9.5, 3, -10, 0)

# p(kn/m) lower
dim8_arrow(-12, -10, -8, -10, -10, -10, -10, -20)
atrace(-10.5, -13, -9.5, -13, -10, -10)

# D
dim12_arrow(98, 25, 102, 25, 100, 25, 100, 0, 98, 0, 102, 0)
atrace(99.5, 22, 100.5, 22, 100, 25)
atrace(99.5, 3, 100.5, 3, 100, 0)

# A
dim12_arrow(0, -18, 0, -22, 0, -20, 80, -20, 80, -18, 80, -22)
atrace(3, -19.5, 3, -20.5, 0, -20)
atrace(77, -19.5, 77, -20.5, 80, -20)

# a
dim4_arrow(36, 40, 44, 40)
atrace(39, 40.5, 39, 39.5, 36, 40)
atrace(41, 40.5, 41, 39.5, 44, 40)

# dm
dim8_arrow(88, 15, 92, 15, 90, 15, 90, 24)
atrace(89.5, 18, 90.5, 18, 90, 15)
# dm lower
dim8_arrow(88, 0, 92, 0, 90, 0, 90, -10)
atrace(89.5, -3, 90.5, -3, 90, 0)

# a_ line
dim4_arrow(22, 31, 57, 31)
atrace(25, 31.5, 25, 30.5, 22, 31)
atrace(54, 31.5, 54, 30.5, 57, 31)

#p(kn)
dim4_arrow(40, 62, 40, 53)
atrace(39.5, 56, 40.5, 56, 40, 53)

# 1'
drawing.add(dxf.line((22, 40), (22,-20 ), layer='TESTLAYER',linetype='CENTER'))
# 2'
drawing.add(dxf.line((10, 40), (10, -20), layer='TESTLAYER',linetype='CENTER'))

drawing.save()
