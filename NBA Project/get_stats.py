from nba_api.stats.endpoints import playercareerstats
import json

filename = 'data/player_stats.json'

data = playercareerstats.PlayerCareerStats(player_id=2544)
data_json = data.get_dict()

with open(filename, 'w') as f:
    json.dump(data_json, f, indent=4)

with open(filename) as f:
    formatted_data = json.load(f)

    data_header = formatted_data["resultSets"][0]['headers']
    for index, header in enumerate(data_header):
        print(index, header)
