from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.static import players
import json

data = commonplayerinfo.CommonPlayerInfo(player_id=2544, timeout=100)

with open('data/readable_LBJ.json') as f:
    data_json = json.load(f)

specific_data_rowHeaders = data_json["resultSets"][0]['headers']
specific_data_rowSet = data_json["resultSets"][0]['rowSet'][0]

player_data = list()
header_data = list()

for row in specific_data_rowSet:
    player_data.append(row)

for row in specific_data_rowHeaders:
    header_data.append(row)

filename = 'data/all_players.json'
all_players = players.get_players()

players = list()
# All players is a list in a dictionary
for player in all_players:
    players.append(player)

with open(filename, 'w') as f:
    json.dump(players, f)
