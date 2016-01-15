from dxfwrite import DXFEngine as dxf
import csv
from dxfwrite.const import CENTER

import pdb

# input file
f = open('Uniformly deep footing.csv')
lst = {'A': '', 'D': '', 'a': ''}
data = [row for row in csv.reader(f)]
for i in lst.keys():
    for j in range(len(data)):
            if(i == data[j][0]):
                    ans = data[j][1]
                    break
    lst[i] = int(ans)

# scaling factor
scale_factor = 3

# text size
textsize = 2.5 * scale_factor

# ####################### Function Definitions #######################


def drawline(points_list):
    for i in range(len(points_list) - 1):
        if(i == 7):
            continue
        c = tuple(scale_factor*p for p in points_list[i])
        d = tuple(scale_factor*q for q in points_list[i+1])
        drawing.add(dxf.line(c, d, color=7))


def arrow(bottom_point, arrow_point, length_arrow=3):
    drawing.add(dxf.line(bottom_point, arrow_point, color=7))
    vertex = arrow_point
    left_pt = (arrow_point[0] - length_arrow / 6.0,
               arrow_point[1] - length_arrow)
    right_pt = (arrow_point[0] + length_arrow / 6.0,
                arrow_point[1] - length_arrow)
    drawing.add(dxf.trace([vertex, left_pt, right_pt]))
    return


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


# point list for creating the base.
points_list = [((lst['A']-lst['a']) / 2, 2*lst['D']),
               ((lst['A']-lst['a']) / 2, lst['D']), (0, lst['D']), (0, 0),
               (lst['A'], 0), (lst['A'], lst['D']),
               ((lst['A'] + lst['a']) / 2, lst['D']),
               ((lst['A'] + lst['a']) / 2, 2*lst['D']),
               ((lst['A'] - 2 * lst['a']) / 2, 2*lst['D']),
               ((lst['A'] - lst['a']) / 2, 2*lst['D']),
               ((lst['A'] - lst['a']) / 2 + (lst['a'] / 3), 2*lst['D']),
               ((lst['A'] / 2), (lst['a'] / 3) + 2*lst['D']),
               ((lst['A'] / 2), 2*lst['D'] - (lst['a'] / 3)),
               ((lst['A'] + lst['a']) / 2 - (lst['a'] / 3), 2*lst['D']),
               ((lst['A'] + lst['a']) / 2, 2*lst['D']),
               ((lst['A'] + 2*lst['a']) / 2, 2*lst['D'])]


string_for_csv = str()
for i in xrange(len(points_list)):
    string_for_csv = string_for_csv + str(points_list[i][0]) + "," + str(
        points_list[i][1]) + "\n"

# csv file
inp = raw_input("Enter the name of csv file you want to generate: ")
fw = open(inp+'.csv', "w")
fw.write(string_for_csv)

# dxf drawing
drawing_name = raw_input("Enter a drawing name to be created without\
 the extension dxf: ")
drawing = dxf.drawing(drawing_name+".dxf")

pdb.set_trace()

# lines
drawline(points_list)


# ################# Bed of Arrows #################

# arrow base line:
arrow_height = 10
no_of_arrows = 10

# left and right base point for arrows to create base line.
left_point = (points_list[3][0], points_list[3][1] - arrow_height)
right_point = (points_list[4][0] * scale_factor, left_point[1])
drawing.add(dxf.line(left_point, right_point, color=3))

# only x-coordinates for arrows
list_xcoordinates_for_arrows = [(right_point[0]/(no_of_arrows))*i
                                for i in xrange(no_of_arrows + 1)]

# arrow base points.
list_bottom_points = zip(list_xcoordinates_for_arrows,
                         [-arrow_height] * (no_of_arrows + 1))

# corresponding upper points.
list_arrow_points = zip(list_xcoordinates_for_arrows, [0] * (no_of_arrows + 1))
final_arrow_points = zip(list_bottom_points, list_arrow_points)

# creating arrows.
for i in range(len(final_arrow_points)):
    arrow(final_arrow_points[i][0], final_arrow_points[i][1])


# ################# Dimensionized Text #################

drawing.add(dxf.text('a', height=textsize, halign=CENTER,
                     alignpoint=((points_list[0][0] +
                                  points_list[-2][0])*scale_factor/2,
                                 ((points_list[0][1] +
                                   points_list[1][1])/2)*scale_factor + 3)))

# drawing.add(dxf.text('D', height=textsize, halign=CENTER, alignpoint=(115, 8)))
# drawing.add(dxf.text('A', height=textsize, halign=CENTER,
#                      alignpoint=(50, -18)))
# drawing.add(dxf.text('P (kN)', height=textsize, halign=CENTER,
#                      alignpoint=(50, 53)))
# drawing.add(dxf.text('p (kN/m\u00B2)', height=textsize, halign=CENTER,
#                      alignpoint=(-12, -7)))

# p(kN/m)
# def dim8_arrow(u11, u12, u13, u14, l11, l12, l13, l14)
u11 = points_list[3][0] - (8 * scale_factor)
u12 = points_list[3][1]
u13 = u11 - (3 * scale_factor)
l11 = (u11 + u13) / 2
l14 = u12 + (8 * scale_factor)
dim8_arrow(u11, u12, u13, u12, l11, u12, l11, l14)
atrace(-10.5, 3, -9.5, 3, -10, 0)

# p(kN/m)lower
u11 = list_bottom_points[0][0] - (8 * scale_factor)
u12 = list_bottom_points[0][1]
l14 = u12 - (8 * scale_factor)
dim8_arrow(u11, u12, u13, u12, l11, u12, l11, l14)
atrace(-10.5, -13, -9.5, -13, -10, -10)
drawing.add(dxf.text('p (kN/m\u00B2)', height=textsize, halign=CENTER,
                     alignpoint=(l14 - (10 * scale_factor),
                                 (points_list[3][1] +
                                  (list_bottom_points[0][1] / 2)))))

# D
# def dim12_arrow(u1, u2, u3, u4, l1, l2, l3, l4, c1, c2, c3, c4):
u1 = (points_list[5][0] * scale_factor + 5 * scale_factor)
u2 = points_list[5][1] * scale_factor
u3 = u1 + 5 * scale_factor
c2 = points_list[3][1]
l1 = (u1 + u3) / 2
l2 = (u1 + u3) / 2
dim12_arrow(u1, u2, u3, u2, l1, u2, l1, c2, u1, c2, u3, c2)
atrace(109.5, 17, 110.5, 17, 110, 20)
atrace(109.5, 3, 110.5, 3, 110, 0)
drawing.add(dxf.text('D', height=textsize, halign=CENTER,
                     alignpoint=(u3, ((u2 + c2) / 2))))

# A
# def dim12_arrow(u1, u2, u3, u4, l1, l2, l3, l4, c1, c2, c3, c4):
u1 = points_list[3][0]
u2 = list_bottom_points[0][1] - 10 * scale_factor
u4 = u2 + (4 * scale_factor)
c1 = list_bottom_points[-1][0]
l2 = (u2 + u4) / 2
dim12_arrow(u1, u2, u1, u4, u1, l2, c1, l2, c1, u2, c1, u4)
atrace(3, -19.5, 3, -20.5, 0, -20)
atrace(97, -19.5, 97, -20.5, 100, -20)
drawing.add(dxf.text('A', height=textsize, halign=CENTER,
                     alignpoint=((u1 + c1) / 2, u4)))

# a
# def dim4_arrow(l21, l22, l23, l24):
dim4_arrow(45, 30, 55, 30)
atrace(48, 29.5, 48, 30.5, 45, (points_list[0][1]+points_list[1][1])/2)
atrace(52, 29.5, 52, 30.5, 55, (points_list[0][1]+points_list[1][1])/2)

# P(kn)
# def dim4_arrow(l21, l22, l23, l24):
l21 = points_list[11][0] * scale_factor
l22 = points_list[11][1] * scale_factor + (2 * scale_factor)
l24 = l22 + (5 * scale_factor)
dim4_arrow(l21, l22, l21, l24)
atrace(49.5, 48, 50.5, 48, 50, 45)
drawing.add(dxf.text('P (kN)', height=textsize, halign=CENTER,
                     alignpoint=(l21, l24 + (2 * scale_factor))))

drawing.save()
