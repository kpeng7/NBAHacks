from openpyxl import load_workbook
import p2

wb = load_workbook('Analytics_Attachment.xlsx')

print wb.get_sheet_names()
opponents = {}
ws = wb['Division_Info']
for row in ws.rows:
    Team1 = Team(self, row[0].value, row[1].value, row[2].value, opponents):
