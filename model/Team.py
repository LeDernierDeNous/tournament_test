from model.Player import Player


class Team:
    VALID_STATUSES = {'None', 'Validated', 'Participate', 'Eliminated'}

    def __init__(self, name: str, elo: int = 1000):
        self.name = name
        self.players = []
        self.status = 'None'
        self.elo = elo

    def get_status(self):
        return self.status

    def set_status(self, status: str):
        if status not in self.VALID_STATUSES:
            raise ValueError(
                f"Error: Invalid status '{status}': Team status does not exist ")
        self.status = status

    def add_player(self, player: Player):
        if player in self.players:
            print(
                f"Error: player '{player.name}' already in team '{self.name}'")
        self.players.append(player)

    def remove_player(self, player: Player):
        if player in self.players:
            self.players.remove(player)
        else:
            print(
                f"Error: player '{player.name}' not found in team '{self.name}'")

    def to_string(self) -> str:
        return self.name+' ('+str(self.elo)+')'

    def change_elo(self, change: int):
        self.elo = self.elo + change
