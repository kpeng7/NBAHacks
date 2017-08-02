from openpyxl import load_workbook
import p2

wb = load_workbook('Analytics_Attachment.xlsx')

print wb.get_sheet_names()
opponents = {}
ws = wb['Division_Info']
team_list = {}
division_list = {}
conference_list = {}

#generateTeams
for row in ws.rows:
    team1 = Team(self, row[0].value, row[1].value, row[2].value, opponents):
    team_list[row[0].value] = team1
print team_list.keys()

#generateDivisions
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
print division_list.keys()

#generateConference
current_conference = "West"
teams_west_list = []
teams_east_list = []
for team in team_list:
    if team.conference == "West":
        teams_west_list.append(team)
    elif team.conference == "East":
        teams_east_list.append(team)
west_conference = Conference(self, "West", teams_west_list)
east_conference = Conference(self, "East", teams_east_list)
conference_list["West"] = west_conference
conference_list["East"] = east_conference
print conference_list.keys()
