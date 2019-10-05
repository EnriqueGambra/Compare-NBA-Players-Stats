from nba_api.stats.endpoints import playercareerstats
import json


class GetStats:
    """Class that will compute and return the statistics for a given player ID"""

    def __init__(self, player_id):
        """Initializes the GetStats class"""
        self.player_id = player_id
        self.filename = 'data/player_stats.json'
        self._create_file()
        self._open_file()

    def _create_file(self):
        """Method that will create the correct corresponding JSON file according to the player id passed."""
        data = playercareerstats.PlayerCareerStats(player_id=self.player_id)
        data_json = data.get_dict()

        with open(self.filename, 'w') as f:
            json.dump(data_json, f, indent=4)

    def _open_file(self):
        """Method that will open the JSON file and call a helper method to extract the data."""
        with open(self.filename) as f:
            formatted_data = json.load(f)

        data_stats = formatted_data["resultSets"][0]["rowSet"]

        self._compute_stats(data_stats)

    def _compute_stats(self, data):
        """Method that will compute the averages of all necessary stats that we want."""
        games, points, rebounds, assists, field_goal_pct = [], [], [], [], []

        for row in data:
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

        self.stats_dict = {
            'PTS': avg_points,
            'REB': avg_rebounds,
            'AST': avg_assists,
            'FG_PCT': avg_fg_pct
        }
