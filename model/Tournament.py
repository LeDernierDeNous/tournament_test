from model.Match import Match
from model.Team import Team

from tournament_tools import get_depth

class Tournament:
    def __init__(self):
        self.teams = []
        self.matches = []
        self.rounds = []
        self.actual_round = 0

    def add_team(self, team: Team):
        self.teams.append(team)

    def remove_team(self, team: Team):
        self.teams.remove(team)
        
    def update_team_status(self, team: Team, status: str):
        if team in self.teams:
            team.set_status(status)
        else:
            print(f"Error: team '{team.name}' not found in tournament")

    def generate_first_matches(self):
        if len(self.teams) < 2 :
            print('Error: A tournament need at least 2 teams')
            exit()
        depth = get_depth(len(self.teams))
        
        # Depth = number of rounds
        for i in range(depth):
            self.rounds.append([])
        
        range_match = int((2**depth)/2)
        for i in range(range_match):
            match = Match(self.teams[i],None)
            self.matches.append(match)
        
        for i in range(range_match):
            if len(self.teams) > i+range_match:
                self.matches[i].set_team2(self.teams[i+range_match])
            else:
                self.matches[i].set_team2('None')
        
        self.rounds[self.actual_round] = self.matches
                
    def validate_round(self,round_number: int):
        for match in self.rounds[round_number]:
            if match.winner == 'TBD':
                print(f"Error: Cannot validate the round, cause the match {match.print_match()} has the winner {match.winner}")
                exit(-1)
        self.actual_round = self.actual_round + 1
        self.matches = []
        self.rounds[self.actual_round] = 
              
    
            
    def print_tournament_matches(self):
        print ('===================================')
        for match in self.matches:
            match.print_match()
            
    def random_result_round(self):
        for match in self.matches:
            if type(match.team1) == Team and type(match.team2) == Team:
                match.set_winner(match.get_random_winner())
            elif type(match.team1) == Team and match.team2 == 'None':
                match.set_winner(match.team1)
            elif match.team1 == 'None' and type(match.team2) == Team:
                match.set_winner(match.team2)
            elif match.team1 == 'None' and match.team2 == 'None':
                match.set_winner('None')
            else:
                print(f"Error : Unexpected error, the match {match} seems to not have valid teams : {match.team1} - {match.team2} ")
            