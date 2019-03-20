import xlwt
#import openpyxl
import math
import os
import sys

def write(path, val, table_width):
    wb = xlwt.Workbook()
    sheet = wb.add_sheet("abc")
    style = xlwt.XFStyle()

    borders = xlwt.Borders()
    borders.left = xlwt.Borders.THIN
    borders.right = xlwt.Borders.THIN
    borders.top = xlwt.Borders.THIN
    borders.bottom = xlwt.Borders.THIN
    style.borders = borders

    for j in range(0, math.ceil(float(len(val))/int(table_width))):
        for i in range(0, table_width):
            val_idx = j * table_width + i
            if val_idx < len(val):
                sheet.write(j, i, val[j * table_width + i], style)
                sheet.col(i).width = 256*3
                sheet.row(j).height = 256
            else:
                sheet.write(j, i, "", style)

    wb.save(path)
    print("write done!, file: " + sys.argv[2])

def read(path):
    print("reading from:[" + sys.argv[1] + "]data:")
    with open(path, "r") as f:
        data = f.read()
        print(data)
        return data
if len(sys.argv) >= 2:
	path_txt = sys.argv[1]
else:
	path_txt = "abc.txt"
if len(sys.argv) >= 3:
	path_xls = sys.argv[2]
else:
	path_xls = "abc.xls"

table_width = 18
write(path_xls, read(path_txt), table_width)




