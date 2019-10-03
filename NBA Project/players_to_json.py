from nba_api.stats.static import players
import json

filename = 'data/all_players.json'
all_players = players.get_players()

players = list()
# All players is a list in a dictionary
for player in all_players:
    players.append(player)

with open(filename, 'w') as f:
    json.dump(players, f, indent=4)
