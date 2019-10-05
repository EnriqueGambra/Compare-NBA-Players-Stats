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
    data_stats = formatted_data["resultSets"][0]["rowSet"]
    games, points, rebounds, assists, field_goal_pct = [], [], [], [], []

    for row in data_stats:
        games_played = row[6]
        pts = row[26] / games_played
        rbs = row[20] / games_played
        ast = row[21] / games_played
        fg_pct = row[11]

        points.append(pts)
        rebounds.append(rbs)
        assists.append(ast)
        field_goal_pct.append(fg_pct)

    avg_points = sum(points) / len(points)
    avg_rebounds = sum(rebounds) / len(rebounds)
    avg_assists = sum(assists) / len(assists)
    avg_fg_pct = sum(field_goal_pct) / len(field_goal_pct)


print(avg_assists)
# print(avg_points, avg_rebounds, avg_assists, avg_fg_pct)