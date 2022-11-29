import xlrd
from Library.config import Config
# path = r"C:\Users\User\Documents\data.xlsx"

# def read_locators():
#     workbook = xlrd.open_workbook(path)
#     worksheet = workbook.sheet_by_name("loginpage")
#     rows = worksheet.get_rows()
#     print(rows)
#     header = next(rows)
#     for row in rows:
#         print(row)
#         header = next(rows)
#         d = {}
#         for row in rows:
#             d[row[0].value] = (row[1].value,row[2].value)
#         return d
#
# print(read_locators())

def read_locators():
    workbook = xlrd.open_workbook(Config.Data_path)
    worksheet = workbook.sheet_by_name("offers_data")
    rows = worksheet.nrows
    # print(rows)
    d={}
    for i in range(1,rows):
        row = worksheet.row_values(i)
        d[row[0]] = (row[1],row[2])
    return d

print(read_locators())



