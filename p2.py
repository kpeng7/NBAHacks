#dictionary of date : [(winning team, losing team, score)]
GAME_DATA = {}

#once one team plays more than 41 games 

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
    
    #constructor for Group object
    def __init__(self, name, teams):
        self.name = name
        self.teams = teams
    
    #adds a team to the Group
    def addTeam(self, team):
        self.teams.append(team)
        
    #ranks teams within the Group
    def rankTeams(self):
        """ADD CODE HERE"""
        pass
    
    #adds a game to the division
    def addGame(self, team1, team2, outcome):
        #outcome = (team1, team2)
        pass
        
    #returns the rank of a given team in the division
    def getRank(self, team):
        pass
    
    def getTeamNames(self):
        return team_names

class Division(Group):
    
    #constructor for division object
    def __init__(self, name, teams):
        Group.__init__(self, name, teams)
        

class Conference(Group):
    pass
    
def main():
    # team = Team("bobcats", ["lol"])
    # print team.getName()
    # print team.opponents
    # team.addGame("lol", "w")
    # print team.opponents
    
    div = Division("east", 'lol')
    print div.name
    
if __name__ == "__main__":
    main()
