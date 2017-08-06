import unittest
from collections import defaultdict
import random

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
    group_leader = None

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
    
    def divisionLeader(self, teams):
        division_leaders = []
        non_division_leaders = []
        for team in teams:
            if team.division_rank == 1:
                division_leaders.append(team)
            else: 
                non_division_leaders.append(team)
        return (division_leaders, non_division_leaders)
    
    def rankByRecordAgainstAll(self, teams):
        out = []
        records = {}
        record_to_team = defaultdict(list)
        for i in len(teams):
            total_games = 0
            team1 = teams[i]
            for j in range(i + 1, len(teams)):
                team2 = teams[j]
                (wins, loss) = team1.opponents[team2.name]
                total_games += wins + loss
                records[team1] += wins
                records[team2] += loss
            record_to_team[records[team1] / total_games].append(team1)
        sorted_keys = sorted(record_to_team.keys())
        for key in sorted_keys:
            out.append(record_to_team[key])
        return out
    
    def rankByDivWonLostPercentage(self, teams):
        out = []
        div_won_lost = defaultdict(list)
        division = teams[0].division
        for team in teams:
            if not team.division == division:
                return [teams]
            div_won_lost[team.division_games_won / team.division_games_played] = team
        sorted_keys = sorted(div_won_lost.keys())
        for key in sorted_keys:
            out.append(div_won_lost[key])
        return out
    
    def rankByConfWonLostPercentage(self, teams):
        out = []
        conf_won_lost = defaultdict(list)
        for team in teams:
            conf_won_lost[team.conference_games_won / team.conference_games_played] = team
        sorted_keys = sorted(conf_won_lost.keys())
        for key in sorted_keys:
            out.append(conf_won_lost[key])
        return out
    
    def rankByPlayoffEligibleInConf(self, teams, conf):
        out = []
        eligible_teams = []
        for team in conf.teams:
            if team.eligible == True:
                eligible_teams.append(team)
        record_to_team = defaultdict(list)
        for team in teams:
            total_wins = 0
            total_losses = 0
            for eligible in eligible_teams:
                if not eligible.name == team.name:
                    total_wins += team.opponents[eligible.name][0]
                    total_losses += team.opponents[eligible.name][1]
            record_to_team[total_wins/(total_wins + total_losses)].append(team)
        sorted_keys = sorted(record_to_team.keys())
        for key in sorted_keys:
            out.append(record_to_team[key])
        return out
    
    def rankByPointDifferential(self, teams):
        out = []
        point_dif = defaultdict(list)
        for team in teams:
            point_dif[team.points_scored - team.points_allowed].append(team)
        sorted_keys = sorted(point_dif.keys())
        for key in sorted_keys:
            out.append(point_dif[key])
        return out

    def settleTie(self, tied_teams, conf, opp_conf):
        if len(tied_teams) == 1:
            return tied_teams
        elif len(tied_teams) == 2:
            list_of_checks = [self.rankByRecordAgainstAll(tied_teams), \
                              self.divisionLeader(tied_teams), \
                              self.rankByDivWonLostPercentage(tied_teams), \
                              self.rankByConfWonLostPercentage(tied_teams), \
                              self.rankByPlayoffEligibleInConf(tied_teams, conf), \
                              self.rankByPlayoffEligibleInConf(tied_teams, opp_conf), \
                              self.rankByPointDifferential(tied_teams), \
                              random.shuffle(tied_teams)]
            for teams_list in list_of_checks:
                if not len(teams_list) == 1:
                    out = []
                    for teams in teams_list:
                        out.extend(self.settleTie(teams))
                    return out
#             team1 = tied_teams[0]
#             team2 = tied_teams[1]
#             team1_vs_team2_record = team1.opponents                     #team 1 (wins, losses) against team2
#             if not float(team1_vs_team2_record[0]) / (team1_vs_team2_record[1]) == 1:
#                 if float(team1_vs_team2_record[0]) / (team1_vs_team2_record[1]) < 1:
#                     #team 1 less wins than team 2
#                     return [team2, team1]
#                 else:
#                     return [team1, team2]
#             elif team1.division_rank == 1 or team2.division_rank == 1 and not team1.division_rank == team2.division_rank :
#                 if team1.division_rank == 1:
#                     return [team1, team2]
#                 else:
#                     return [team2, team1]
#             elif team1.division == team2.division and not team1.division_games_won / team1.division_games_played == team2.division_games_won / team2.division_games_played:
#                 if team1.division_games_won / team1.division_games_played > team2.division_games_won / team2.division_games_played:
#                     return [team1, team2]
#                 else:
#                     return [team2, team1]
#             elif not team1.conference_games_won / team1.conference_games_played == team2.conference_games_won / team2.conference_games_played:
#                 if team1.conference_games_won / team1.conference_games_played > team2.conference_games_won / team2.conference_games_played:
#                     return [team1, team2]
#                 else:
#                     return [team2, team1]
#             elif 0:
#                 pass
#             else:
#                 pass
                
        else:
            list_of_checks = [self.divisionLeader(tied_teams), \
                              self.rankByRecordAgainstAll(tied_teams), \
                              self.rankByDivWonLostPercentage(tied_teams), \
                              self.rankByConfWonLostPercentage(tied_teams), \
                              self.rankByPlayoffEligibleInConf(tied_teams, conf), \
                              self.rankByPointDifferential(tied_teams), \
                              random.shuffle(tied_teams)]
            
            for teams_list in list_of_checks:
                if not len(teams_list) == 1:
                    out = []
                    for teams in teams_list:
                        out.extend(self.settleTie(teams))
                    return out
            
#             teams_list = self.divisionLeader(tied_teams)
#             if not len(teams_list) == 1:
#                 out = []
#                 for teams in teams_list:
#                     out.extend(self.settleTie(teams))
#                 return out
#             teams_list = self.rankByRecordAgainstAll(tied_teams)
#             if not len(teams_list) == 1:
#                 out = []
#                 for teams in teams_list:
#                     out.extend(self.settleTie(teams))
#                 return out
#             teams_list = self.rankByDivWonLostPercentage(tied_teams)
#             if not len(teams_list) == 1:
#                 out = []
#                 for teams in teams_list:
#                     out.extend(self.settleTie(teams))
#                 return out
#             teams_list = self.rankByConfWonLostPercentage(tied_teams)
#             if not len(teams_list) == 1:
#                 out = []
#                 for teams in teams_list:
#                     out.extend(self.settleTie(teams))
#                 return out
#             teams_list = self.rankByPlayoffEligibleInConf(tied_teams, conf)
#             if not len(teams_list) == 1:
#                 out = []
#                 for teams in teams_list:
#                     out.extend(self.settleTie(teams))
#                 return out
#             teams_list = self.rankByPointDifferential(tied_teams)
#             if not len(teams_list) == 1:
#                 out = []
#                 for teams in teams_list:
#                     out.extend(self.settleTie(teams))
#                 return out
#             return random.shuffle(tied_teams)

class Division(Group):

    #constructor for division object
    def __init__(self, name, teams):
        Group.__init__(self, name, teams)
        
    def rankTeams(self):
        ranked_dict = {}
        for team in self.teams:
            ranked_dict[float(team.division_games_won)/float(team.division_games_played)].append(team)
        ranked = sorted(ranked_dict.keys())
        if len(ranked_dict[ranked[0]]) == 1:
            self.group_leader = ranked_dict[ranked[0]][0].name
        else:
            self.group_leader = self.settleTie(ranked_dict[ranked[0]])


class Conference(Group):
    #constructor for conference object
    def __init__(self, name, teams):
        Group.__init__(self, name, teams)
        
    def rankTeams(self):
        ranked_dict = {}
        for team in self.teams:
            ranked_dict[float(team.conference_games_won)/float(team.conference_games_played)].append(team)
        ranked = sorted(ranked_dict.keys())
        if len(ranked_dict[ranked[0]]) == 1:
            self.group_leader = ranked_dict[ranked[0]][0].name
        else:
            self.group_leader = self.settleTie(ranked_dict[ranked[0]])
    

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
    if sameDivision(team1, team2):
        divisions[team1.division].updateGroup()
    if sameConference(team1, team2):
        conferences[team1.conference].updateGroup()

        
    

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
