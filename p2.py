GAME_DATA = {}
class Team():
    name = ""
    conference_rank = 0
    division_rank = 0
    games_won = 0
    games_played = 0
    division = ""
    conference = ""
    opponents = {}
    points_scored = 0
    points_allowed = 0
    def __init__(self, name, opponents_list):
        self.name = name
        for opponent in opponents_list:
            self.opponents[opponent] = [0, 0] #FORMAT = [W, L]

    def getName(self):
        return self.name
    
    def setConferenceRank(self, rank):
        self.conference_rank = rank
        
    def getConferenceRank(self):
        return self.conference_rank
    
    def setDivisionRank(self, rank):
        self.division_rank = rank
    
    def getDivisionRank(self):
        return self.division_rank
    
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
    def __init__(self, name):
        self.name = name
    
    def addTeam(self, team):
        self.teams.append(team)
        
    def rankTeams(self):
        """ADD CODE HERE"""
        pass
        
    def getName(self):
        print self.name

class Division(Group):
    pass
    

class Conference(Group):
    pass
    

team = Team("bobcats", ["lol"])
print team.getName()
print team.opponents
team.addGame("lol", "w")
print team.opponents

div = Division("east")
div.getName()
div.test()
