from dxfwrite import DXFEngine as dxf
import csv
import math
from dxfwrite.const import CENTER

# text size
textsize = 2.5

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

# input file
f=open('Developstepfoot(b).csv')
lst={'A':'','D':'','a':'','Dm':'','a_':'','ClearCover':'','Dia':''}
data=[row for row in csv.reader(f)]
for i in lst.keys():
    for j in range(len(data)):
            if(i==data[j][0]):
                    ans=data[j][1]
                    break;
    lst[i]=int(ans)


# points_list
points_list = [((lst['A'] - lst['a']) / 2, 2*lst['D']), ((lst['A'] - lst['a']) / 2, lst['D']), ((lst['A'] - lst['a_']) / 2, lst['D']),
                              ((lst['A'] - lst['a_']) / 2, lst['Dm']), (0, lst['Dm']) , (0, 0), (lst['A'], 0), (lst['A'], lst['Dm']) ,
                              ((lst['A'] + lst['a_']) / 2, lst['Dm']), ((lst['A'] + lst['a_']) / 2, lst['D']), ((lst['A'] + lst['a']) / 2, lst['D']),
                              ((lst['A'] +lst['a']) / 2, 2*lst['D']), ((lst['A'] - 2*lst['a']) / 2, 2*lst['D']), ((lst['A'] -  lst['a']) / 2, 2*lst['D']),
                              ((lst['A'] - lst['a']) / 2 + (lst['a'] / 3), 2*lst['D']), ((lst['A'] / 2), (lst['a'] / 3) + 2*lst['D']),
                              ((lst['A'] / 2), 2*lst['D'] - (lst['a'] / 3)), ((lst['A'] + lst['a']) / 2 - (lst['a'] / 3), 2*lst['D']),
                              ((lst['A'] + 2*lst['a']) / 2, 2*lst['D']),
               (2, 2 + lst['Dia']), (lst['A'] - 2, 2 + lst['Dia']), (lst['A'] - 2, 2), (2, 2), (2, 2 + lst['Dia'])]


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
def drawline(points_list):
        for i in range(len(points_list) - 1):
                if(i==11):
                    continue
                elif(i==18):
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
drawing.add(dxf.text('a', height=textsize, halign=CENTER, alignpoint=(40, 43)))
drawing.add(dxf.text('D', height=textsize, halign=CENTER, alignpoint=(105, 10)))
drawing.add(dxf.text('A', height=textsize, halign=CENTER, alignpoint=(40, -18)))
drawing.add(dxf.text('y\' > L\U+0501', height=textsize, halign=CENTER, alignpoint=(10, -15)))
drawing.add(dxf.text('Dm', height=textsize, halign=CENTER, alignpoint=(90, 5)))
drawing.add(dxf.text('a\'', height=textsize, halign=CENTER, alignpoint=(30, 35)))
drawing.add(dxf.text('1\'', height=textsize, halign=CENTER, alignpoint=(20, 43)))
drawing.add(dxf.text('1', height=textsize, halign=CENTER, alignpoint=(36, 53)))
drawing.add(dxf.text('1\'', height=textsize, halign=CENTER, alignpoint=(22, -18)))
drawing.add(dxf.text('1', height=textsize, halign=CENTER, alignpoint=(36, -14)))


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

# 1'
drawing.add(dxf.line((22, 40), (22,-15 ), linetype='DASHED'))

# 1
drawing.add(dxf.line((36, 52), (36, -10), linetype='DASHED'))

# y' ld
drawing.add(dxf.line((0, -8), (0, -12)))
drawing.add(dxf.line((0, -10), (22, -10)))
atrace(3, -9.5, 3, -10.5, 0, -10)
atrace(19, -9.5, 19, -10.5, 22, -10)

drawing.save()
