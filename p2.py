import unittest

#dictionary of date : [(winning team, losing team, score)]
GAME_DATA = {}

#once one team plays more than 41 games 

class Tests(unittest.TestCase):
    def testAddGame(self):
        team1 = Team("name", "division", "conference", ["name2"])
        team2 = Team("name2", "division", "conference", ["name"])
        team1.addGame(team2, (100, 50))
        self.assertEqual(team1.games_won, 1)
        self.assertEqual(team1.games_played, 1)
        self.assertEqual(team1.division_games_won, 1)
        self.assertEqual(team1.division_games_played, 1)
        self.assertEqual(team1.conference_games_won, 1)
        self.assertEqual(team1.conference_games_played, 1)
        self.assertEqual(team1.opponents["name2"], [1, 0])
        self.assertEqual(team1.points_scored, 100)
        self.assertEqual(team1.points_allowed, 50)
        
    def testSameConference(self):
        team1 = Team("name", "division", "conference", [])
        team2 = Team(None, None, "conference", [])
        team3 = Team("", "", "", [])
        self.assertEqual(sameConference(team1, team2), True)
        self.assertEqual(sameConference(team1, team3), False)

class Team():
    name = ""
    conference_rank = 0     #set in conference object
    division_rank = 0       #set in division object
    games_won = 0
    games_played = 0
    division = ""
    conference = ""
    division_games_won = 0
    division_games_played = 0
    conference_games_won = 0
    conference_games_played = 0
    opponents = {}          #dict of opponents names (str): [number of wins, number of losses]
    points_scored = 0
    points_allowed = 0
    eliminated = None

    #constructor for Team object
    def __init__(self, name, division, conference, opponents_list):
        self.name = name
        self.division = division
        self.conference = conference
        for opponent in opponents_list:
            self.opponents[opponent] = [0, 0] #FORMAT = [W, L]

    #adds a game played to the team
    def addGame(self, opponent, outcome):
        won = False
        if outcome[0] > outcome[1]:
            won = True
        self.points_scored += outcome[0]
        self.points_allowed += outcome[1]
        if won:
            self.games_won += 1
            self.opponents[opponent.name][0] += 1
        else:
            self.opponents[opponent.name][1] += 1
        if self.division == opponent.division:
            self.division_games_played += 1
            if won:
                self.division_games_won += 1
        if self.conference == opponent.conference:
            self.conference_games_played += 1
            if won:
                self.conference_games_won += 1
        self.games_played += 1

class Group():
    name = ""
    teams = []
    team_names = []
    group_leaders = []

    #constructor for Group object
    def __init__(self, name, teams):
        self.name = name
        self.teams = teams
        for team in teams:
            self.team_names.append(team.name)

    #adds a team to the Group
    def addTeam(self, team):
        self.teams.append(team)

    #ranks teams within the Group
    def rankTeams(self):
        pass

    #updates Group to get the new group leaders
    def updateGroup(self):
        #outcome = (team1, team2)
        pass

    #returns the rank of a given team in the division
    def getRank(self, team):
        pass

    def getTeamNames(self):
        return self.team_names

class Division(Group):

    #constructor for division object
    def __init__(self, name, teams):
        Group.__init__(self, name, teams)
        
    def rankTeams(self):
        ranked_dict = {}
        for team in self.teams:
            ranked_dict[team.name] = float(team.division_games_won)/float(team.division_games_played)
        ranked = sorted(ranked_dict.keys())
        self.leaders.


class Conference(Group):
    pass

def generateTeams():
    #returns dictionary of team name : team object
    pass

def generateDivisions():
    #returns dictionary of division name : division object
    pass

def sameConference(team1, team2):
    return team1.conference == team2.conference

def sameDivision(team1, team2):
    return team1.division == team2.division
    
def updateSeason((winning_team, losing_team, score), teams, divisions, conferences):
    team1 = teams[winning_team]
    team2 = teams[losing_team]
    team1.addGame(team2, score)
    team2.addGame(team1, [score[1], score[0]])
    if sameConference(team1, team2):
        conferences[team1.conference].updateGroup()
    if sameDivision(team1, team2):
        divisions[team1.division].updateGroup()
        
    

def main():
    teams = generateTeams()
    divisions = generateDivisions()
    for date in GAME_DATA.keys():
        for game in GAME_DATA[date]:
            updateSeason(game, teams)
            
    # team = Team("bobcats", ["lol"])
    # print team.getName()
    # print team.opponents
    # team.addGame("lol", "w")
    # print team.opponents

    div = Division("east", 'lol')
    print div.name

if __name__ == "__main__":
    unittest.main()
    main()
