from dxfwrite import DXFEngine as dxf
from dxfwrite.const import CENTER
import csv
import math
#import pdb


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


#input file
f=open('Sloped footing(c).csv')
lst={'A':'','D':'','a':'','Dm':''}
data=[row for row in csv.reader(f)]
for i in lst.keys():
    for j in range(len(data)):
            if(i==data[j][0]):
                    ans=data[j][1]
                    break;
    lst[i]=int(ans)

#pdb.set_trace()

points_list = [((lst['A'] - lst['a']) / 2, 2*lst['D']), ((lst['A'] - lst['a']) / 2, lst['D']), (0, lst['Dm']), (0, 0),
               ((lst['A'] - lst['a']) / 2, 0) , (lst['A'], 0), (lst['A'], lst['Dm']), ((lst['A'] + lst['a']) / 2, lst['D']) ,
               ((lst['A'] + lst['a']) / 2, 2*lst['D']), ((lst['A'] - 2*lst['a']) / 2, 2*lst['D']), ((lst['A'] -  lst['a']) / 2, 2*lst['D']),
               ((lst['A'] - lst['a']) / 2 + (lst['a'] / 3), 2*lst['D']), ((lst['A'] / 2), (lst['a'] / 3) + 2*lst['D']),
               ((lst['A'] / 2), 2*lst['D'] - (lst['a'] / 3)), ((lst['A'] + lst['a']) / 2 - (lst['a'] / 3), 2*lst['D']), ((lst['A'] + 2*lst['a']) / 2, 2*lst['D'])]


string_for_csv = str()
for i in xrange(len(points_list)):
    string_for_csv = string_for_csv + str(points_list[i][0]) + "," + str(points_list[i][1]) + "\n"

#csv file
inp = raw_input("Enter the name of csv file you want to generate: ")
fw = open(inp+".csv", "w")
fw.write(string_for_csv)

#dxf drawing
drawing_name = raw_input("Enter a drawing name to be created without the extension dxf: ")
drawing = dxf.drawing(drawing_name+".dxf")

#line
def drawline(points_list):
    for i in range(len(points_list) - 1):
            if(i==8):
                continue
            c = tuple(points_list[i])
            d = tuple(points_list[i+1])
            drawing.add(dxf.line(c, d, color=7))

drawline(points_list)

#arrow base line:
dist_of_arrow_from_footing_base = 10
no_of_arrows = 10

left_point = 0, -dist_of_arrow_from_footing_base
right_point = lst['A'],-dist_of_arrow_from_footing_base

drawing.add(dxf.line(left_point,right_point, color=7))

#arrow
def arrow(bottom_point,arrow_point, length_arrow = 3):
    drawing.add(dxf.line(bottom_point,arrow_point, color= 7))
    vertex = arrow_point
    left_pt = (arrow_point[0] - length_arrow / 6.0 , arrow_point[1] - length_arrow )
    right_pt = (arrow_point[0] + length_arrow / 6.0 , arrow_point[1] - length_arrow)
    drawing.add(dxf.trace([vertex, left_pt, right_pt]))
    return
list_xcoordinates_for_arrows = [(float(lst['A'])/(no_of_arrows - 1))*i for i in xrange(no_of_arrows + 1)]
list_bottom_points = zip(list_xcoordinates_for_arrows,[-dist_of_arrow_from_footing_base] * no_of_arrows)
list_arrow_points = zip(list_xcoordinates_for_arrows,[0] * no_of_arrows)
final_arrow_points = zip(list_bottom_points,list_arrow_points)

for i in xrange(len(final_arrow_points)):
    arrow(final_arrow_points[i][0], final_arrow_points[i][1])

# text size
textsize = 2.5

#text
drawing.add(dxf.text('a', height=2.5, halign=CENTER, alignpoint=(50, 32)))
drawing.add(dxf.text('D', height=2.5, halign=CENTER, alignpoint=(114, 12)))
drawing.add(dxf.text('A', height=2.5, halign=CENTER, alignpoint=(50, -18)))
drawing.add(dxf.text('p (kN/m\u00B2)', height=2.5, halign=CENTER, alignpoint=(-15, -7)))
drawing.add(dxf.text('P (kN)', height=2.5, halign=CENTER, alignpoint=(50, 54)))
drawing.add(dxf.text('Dm', height=2.5, halign=CENTER, alignpoint=(104, -5)))
drawing.add(dxf.text(u"\u03B2", height=2.5, halign=CENTER, alignpoint=(15, 8)))
drawing.add(dxf.text(u"\u03B2", height=2.5, halign=CENTER, alignpoint=(85, 8)))

# p(kN/m)
dim8_arrow(-12, 0, -8, 0, -10, 10, -10, 0)
atrace(-10.5, 3, -9.5, 3, -10, 0)

# p(kN/m)lower
dim8_arrow(-12, -10, -8, -10, -10, -10, -10, -20)
atrace(-10.5, -13, -9.5, -13, -10, -10)

#D
dim12_arrow(108, 20, 112, 20, 110, 20, 110, 0, 108, 0, 112,0)
atrace(109.5, 17, 110.5, 17, 110, 20)
atrace(109.5, 3, 110.5, 3, 110, 0)

#A
dim12_arrow(0, -18, 0, -22, 0, -20, 100, -20, 100, -18, 100, -22)
atrace(3, -19.5, 3, -20.5, 0, -20)
atrace(97, -19.5, 97, -20.5, 100, -20)

#a
dim4_arrow(45, 30, 55, 30)
atrace(48, 29.5, 48, 30.5, 45, 30)
atrace(52, 29.5, 52, 30.5, 55, 30)

#dm
dim12_arrow(101, 8, 105, 8, 103, 8, 103, 0, 101, 0, 105, 0)
atrace(102.5, 5, 103.5, 5, 103, 8)
atrace(102.5, 3, 103.5, 3, 103, 0)

#beta
dim8_arrow(2, 8, 12, 8, 88, 8, 98, 8)
dim5_arrow(4, (6, 15), 0, 90)
atrace(9.5, 15, 10.5, 15, 10, 12)
dim5_arrow(4, (94, 15), 100, 190)
atrace(89.5, 15, 90.5, 15, 90, 12)

#P(kn)
dim4_arrow(50, 52, 50, 45)
atrace(49.5, 48, 50.5, 48, 50, 45)

drawing.save()
