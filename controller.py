from model.Tournament import Tournament
from model.Player import Player
from model.Team import Team
from tournament_tools import *

team1 = Team("Team A")
team2 = Team("Team B")
team3 = Team("Team C")
team4 = Team("Team D")
team5 = Team("Team E")
team6 = Team("Team F")
team7 = Team("Team G")
team8 = Team("Team H")
team9 = Team("Team I")

# Add ten players to each team
for i in range(10):
    player_name = f"Player {i+1}"
    player = Player(player_name)
    team1.add_player(player)
    
for i in range(10):
    player_name = f"Player {i+1}"
    player = Player(player_name)
    team2.add_player(player)
    
for i in range(10):
    player_name = f"Player {i+1}"
    player = Player(player_name)
    team3.add_player(player)
    
for i in range(10):
    player_name = f"Player {i+1}"
    player = Player(player_name)
    team4.add_player(player)

for i in range(10):
    player_name = f"Player {i+1}"
    player = Player(player_name)
    team5.add_player(player)

# Create a tournament and add the four teams to it
tournament = Tournament()
tournament.add_team(team1)
tournament.add_team(team2)
tournament.add_team(team3)
tournament.add_team(team4)
tournament.add_team(team5)
tournament.add_team(team6)
tournament.add_team(team7)
tournament.add_team(team8)
tournament.add_team(team9)

# Generate matches for the tournament
tournament.generate_first_matches()

# Print the matches
tournament.print_tournament_matches()

# Random result
tournament.random_result_round()

# Print the matches
tournament.print_tournament_matches()