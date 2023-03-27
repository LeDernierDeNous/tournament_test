from colors.bcolors import bcolors
from model.TournamentSE import TournamentSE
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
tournamentse = TournamentSE()
tournamentse.add_team(team1)
tournamentse.add_team(team2)
tournamentse.add_team(team3)
tournamentse.add_team(team4)
tournamentse.add_team(team5)
tournamentse.add_team(team6)
tournamentse.add_team(team7)
tournamentse.add_team(team8)
tournamentse.add_team(team9)


#### Starting tournament ####
tournamentse.print_command_line_separator()
print(bcolors.OKBLUE+f'Starting tournament'+bcolors.ENDC)

# Generate matches for the tournament
tournamentse.generate_first_matches()
# Print first round of the tournament
tournamentse.print_tournament_matches()
# Play all the round of the tournament
for round_number in range(get_depth(len(tournamentse.teams))-1) :
    tournamentse.print_command_line_separator()
    print(bcolors.OKBLUE+f'Starting round {round_number+1}'+bcolors.ENDC)
    tournamentse.random_result_round()
    tournamentse.print_tournament_matches()
    tournamentse.print_command_line_separator()
    print(bcolors.OKBLUE+f'Round {round_number+1} is over, starting the next round'+bcolors.ENDC)
    tournamentse.validate_round(round_number)
    tournamentse.print_tournament_matches()

tournamentse.print_command_line_separator()
print(bcolors.OKBLUE+f'Starting final round'+bcolors.ENDC)
tournamentse.random_result_round()
tournamentse.print_tournament_matches()
tournamentse.print_command_line_separator()
print(bcolors.OKBLUE+f'Tournament is over, congratulation to the winning : '+ bcolors.OKGREEN + bcolors.BOLD +f'{tournamentse.get_winner().to_string()}'+ bcolors.ENDC)
tournamentse.print_command_line_separator()