from model.Match import Match
from model.Team import Team
from model.Tournament import Tournament

from tournament_tools import get_depth

class TournamentSE(Tournament):
    def __init__(self):
        self.teams = []
        self.matches = []
        self.rounds = []
        self.actual_round = 0

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
                print(f"Error: Cannot validate the round, cause the match {match.print_match()} has the unexpected winner {match.winner}")
                exit(-1)
        self.actual_round = self.actual_round + 1
        self.matches = []
        for match_number in range(int(len(self.rounds[self.actual_round-1])/2)):
            new_match = Match(self.rounds[self.actual_round-1][match_number*2].winner,self.rounds[self.actual_round-1][(match_number*2)+1].winner)
            self.rounds[self.actual_round].append(new_match)
        self.matches = self.rounds[self.actual_round]
    
    def get_winner(self) -> Team:
        if self.tournament_is_over():
            return self.matches[0].winner
            