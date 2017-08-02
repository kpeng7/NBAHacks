from openpyxl import load_workbook
import p2

wb = load_workbook('Analytics_Attachment.xlsx')

print wb.get_sheet_names()
opponents = {}
ws = wb['Division_Info']
team_list = {}
division_list = {}

for row in ws.rows:
    team1 = Team(self, row[0].value, row[1].value, row[2].value, opponents):
    team_list[row[0].value] = team1
print team_list.keys()

for row in ws.rows:
    current_row = row[1].value
    if not division_list.has_key(current_row):
        teams_division_list = []
        for team in ws.rows:
            if team[1].value == current_row:
                new_team = Team(self, team[0].value, current_row, team[2].value, opponents):
                teams_division_list.append(new_team)
        division1 = Division(self, current_row, teams_division_list)
        division_list[current_row] = division1
