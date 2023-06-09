import random
from colors.bcolors import bcolors
from model.Team import Team


class Match:
    def __init__(self, team1: Team = None, team2: Team = None):
        if team1 is None:
            self.team1 = 'TBD'
        else:
            self.team1 = team1
        if team2 is None:
            self.team2 = 'TBD'
        else:
            self.team2 = team2
        self.winner = 'TBD'

    def set_team1(self, team1: Team):
        self.team1 = team1

    def set_team1(self, team1: str):
        self.team1 = team1

    def set_team2(self, team2: Team):
        self.team2 = team2

    def set_team2(self, team2: str):
        self.team2 = team2

    def set_winner(self, team: Team):
        if team == self.team1 or team == self.team2:
            self.winner = team
            self.apply_elo_change(self.winner)

    def apply_elo_change(self, winner: Team):
        if type(self.team1) == Team and type(self.team2) == Team:
            k_factor = 32
            if winner == self.team1:
                elo_difference = self.team2.elo - self.team1.elo
                expected_score = 1 / (1 + 10 ** (elo_difference / 400))
                actual_score = 1
                self.team1.change_elo(
                    int(k_factor * (actual_score - expected_score)))
                self.team2.change_elo(
                    int(k_factor * (expected_score - actual_score)))
            else:
                elo_difference = self.team1.elo - self.team2.elo
                expected_score = 1 / (1 + 10 ** (elo_difference / 400))
                actual_score = 1
                self.team2.change_elo(
                    int(k_factor * (actual_score - expected_score)))
                self.team1.change_elo(
                    int(k_factor * (expected_score - actual_score)))
        else:
            pass

    def get_team_name(self, team_number: int):
        if team_number == 1:
            if type(self.team1) == Team:
                return self.team1.to_string()
            else:
                return self.team1
        elif team_number == 2:
            if type(self.team2) == Team:
                return self.team2.to_string()
            else:
                return self.team2
        else:
            print(f"Error: team number '{team_number}' does not exist")

    def print_match(self):
        if type(self.winner) == Team:
            print(bcolors.HEADER + f"{self.get_team_name(1)} vs. {self.get_team_name(2)} :" +
                  bcolors.OKGREEN + f" {self.winner.to_string()}"+bcolors.ENDC)
        else:
            print(bcolors.HEADER + f"{self.get_team_name(1)} vs. {self.get_team_name(2)} :" +
                  bcolors.WARNING + f" {self.winner}"+bcolors.ENDC)

    def get_random_winner(self) -> Team:
        if random.randint(0, 100) > 50:
            return self.team1
        else:
            return self.team2
