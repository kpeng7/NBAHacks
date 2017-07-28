GAME_DATA = {}
class Team():
    name = ""
    conference_rank = 0     #set in conference object
    division_rank = 0       #set in division object
    games_won = 0
    games_played = 0
    division = ""
    conference = ""
    opponents = {}
    points_scored = 0
    points_allowed = 0
    eliminated = None
    def __init__(self, name, division, conference, opponents_list):
        self.name = name
        self.division = division
        self.conference = conference
        for opponent in opponents_list:
            self.opponents[opponent] = [0, 0] #FORMAT = [W, L]
    
    def addGame(self, opponent, outcome):
        self.points_scored += outcome[0]
        self.points_allowed += outcome[1]
        if outcome[0] > outcome[1]:
            self.games_won += 1
            self.opponents[opponent][0] += 1
        else:
            self.opponents[opponent][1] += 1
        self.games_played += 1


class Group():
    name = ""
    teams = []
    def __init__(self, name, teams):
        self.name = name
        self.teams = teams
    
    def addTeam(self, team):
        self.teams.append(team)
        
    def rankTeams(self):
        """ADD CODE HERE"""
        pass
        
    def getName(self):
        print self.name

class Division(Group):
    
    def __init__(self, name, teams):
        Group.__init__(self, name, teams)
    
    def addGame(self, team1, team2, outcome):
        #outcome = (team1, team2)
        pass
        
    def getRank(self, team):
        pass
        

class Conference(Group):
    pass
    

# team = Team("bobcats", ["lol"])
# print team.getName()
# print team.opponents
# team.addGame("lol", "w")
# print team.opponents

div = Division("east", 'lol')
div.getName()
div.test()
