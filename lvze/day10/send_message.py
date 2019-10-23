import zhenzismsclient as smsclient
import random
import ssl
import xlrd


def create_code():
    code = [str(i) for i in range(10)]
    code = random.sample(code, 6)
    code = ''.join(code)
    print(code)


def get_phone_number():
    wb = xlrd.open_workbook("test_01.xlsx")
    sh = wb.sheet_by_
