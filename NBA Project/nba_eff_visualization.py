from get_id import GetID

num_of_players = int(input("Welcome! Please enter the number of players you'd like to analyze." +
                           " You can only analyze up to 10: "))

# Lists for the playersIDs and corresponding names
players_IDs, players_names = [], []

# Loops through until the 'q' key is pressed or it reaches the number of players the user desired
for number in range(num_of_players):
    player_name = input("Enter in a player's full name to receive their data. " +
                        "You can quit at any time. Just enter 'q': ")
    
    if player_name == 'q':
        break
    else:
        instance = GetID(player_name)
        player_id = instance.find_id()

        players_IDs.append(player_id)
        players_names.append(player_name)

print(players_IDs, players_names)
