import xlrd
a = xlrd.open_workbook(r'C:\Users\Administrator\Desktop\test.xls')
sheet1 = a.sheet_by_name("Sheet1")
# sheet1 = a.sheet_by_index(0)
# print(a.sheet_names())
print(sheet1)

print(sheet1.cell_value(0, 0))

for i in range(5):
    for j in range(5):
        print(sheet1.cell_value(i, j))