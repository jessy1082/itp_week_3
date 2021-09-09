sheet_name = wb.sheetnames
print(sheet_name)



for i in range(1,8):
    print(i, my_sheet.cell(row = i, column =2).value)
