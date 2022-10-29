import win32com.client

from win32com.client import CDispatch

str_work_file = "C:\\Robots\\data\\test.xls"

app = win32com.client.Dispatch('Excel.Application')

app.Visible = 0
app.DisplayAlerts = 0

wb = app.Workbooks.Open(str_work_file)

for sheet in wb.Worksheets:
    print(sheet.name)

sheet1 = wb.Worksheets(sheet.name)
print(sheet1.Name)

wb.Close()
app.Quit()
