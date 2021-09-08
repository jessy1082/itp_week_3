import openpyxl

wb = openpyxl.load_workbook("C:/Users/jessy/Desktop/Vetstech_Python/itp_week_3/day_1/lecture.xlsx")
print(type(wb))

sheet= wb['Sheet1']

for i in range(1,8):
    # on the date of A, C amount of B
    date= "A" + str(i)
    date_cell = sheet[date]

    amount = 'C' + str(i)
    amount_cell = sheet[amount]

    fruit = "B" + str(i)
    fruit_cell = sheet[fruit]

    print ("On the date of" + str(date_cell.value) + "," + 
    str(amount_cell.value) + " amount of " + fruit_cell.value + "!")