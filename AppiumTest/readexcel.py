import xlrd

workbook=xlrd.open_workbook("C:\\Users\\158260\\PycharmProjects\\testscript\\AppiumTest\\excel\\Book1.xlsx")
sheet=workbook.sheet_by_name('Sheet1')

row_count=sheet.nrows
print("total number of rows",row_count)