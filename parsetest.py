from openpyxl import load_workbook
import p2

wb = load_workbook('Analytics_Attachment.xlsx')

print wb.get_sheet_names()
opponents = {}
ws = wb['Division_Info']
games = wb['2016_17_NBA_Scores']
team_list = {}
division_list = {}
conference_list = {}
GAME_DATA = {}


#generateTeams
for row in ws.rows:
    team1 = Team(self, row[0].value, row[1].value, row[2].value, opponents):
    team_list[row[0].value] = team1
print team_list.keys()

#generateDivisions
for team in team_list:
    current_division = team.division
    if not division_list.has_key(current_division):
        teams_division_list = []
        for team_temp in team_list:
            if team_temp.division == current_division:
                teams_division_list.append(team_temp)
        division_temp = Division(self, current_division, teams_division_list)
        division_list[current_division] = division1
print division_list.keys()

#generateConference
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

#generateGame_Data
for row in games.rows:
    current_date = row[0].value
    if not GAME_DATA.has_key(current_date):
        games_list = []
        for row_temp in games.rows:
            game = (row[1].value, row[2].value, (row[3].value, row[4].value))
            games_list.append(game)
        GAME_DATA[current_date] = games_list
print GAME_DATA.keys()
