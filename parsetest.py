from openpyxl import load_workbook

wb = load_workbook('Analytics_Attachment.xlsx')

print wb.get_sheet_names()
ws = wb['Division_Info']
for row in ws.rows:
    print row[0].value
