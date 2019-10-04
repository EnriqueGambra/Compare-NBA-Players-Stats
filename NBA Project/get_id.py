import json


class GetID:
    """Class to get the ID of players."""

    def __init__(self, player_name):
        """Initializes the GetID class"""
        self.player_name = player_name
        self.filename = 'data/all_players.json'

    def find_id(self):
        with open(self.filename) as f:
            players_data = json.load(f)

        # For every player in all_players.json use their first name as a key and the value will be their id.
        for player in players_data:
            current_name = player["full_name"]
            if self.player_name == current_name:
                return player["id"]
