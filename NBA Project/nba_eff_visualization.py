from get_id import GetID
from get_stats import GetStats
import plotly.graph_objs as go
from plotly import offline

num_of_players = int(input("Welcome! Please enter the number of players you'd like to analyze." +
                           " You can only analyze up to 10: "))

if num_of_players > 10:
    print("Entered too many players. Program shutting down!")
    quit()

# Lists for the playersIDs and corresponding names
players_IDs, players_names, players_stats, all_stats = [], [], [], []

# Loops through until the 'q' key is pressed or it reaches the number of players the user desired
for number in range(num_of_players):
    player_name = input("Enter in a player's full name to receive their data. Names are case sensitive. " +
                        "You can quit at any time. Just enter 'q': ")

    if player_name == 'q':
        break
    else:
        instance = GetID(player_name)
        player_id = instance.find_id()

        # Catches if a players name was not entered correctly.
        if player_id is None:
            print(f'You did not enter in {player_name} correctly. {player_name} will not be included in plot!')
        else:
            players_IDs.append(player_id)
            players_names.append(player_name)

            get_stats_instance = GetStats(player_id)
            players_stats.append(get_stats_instance.stats_dict)

data = [{
    'type': 'bar',
    'x': players_names,
    'y': [player['PTS'] for player in players_stats],
    'marker':
        {
            'color': 'rgb(60, 100, 150)',
            'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'},
        },
}]

my_layout = {
    'title': "Average PPG for a Player's Career",
    'titlefont': {'size': 28},
    'xaxis': {
        'title': "Player Names",
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': "Points Per Game (PPG)",
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='data/plot_NBA.html')
