# Program extracting first column
import xlrd

loc = ("C:\\temp\\roykere_kort_1.xlsx")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)

for i in range(sheet.nrows):
    print(sheet.cell_value(i, 0))




