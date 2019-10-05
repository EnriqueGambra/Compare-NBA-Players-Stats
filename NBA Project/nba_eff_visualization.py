from get_id import GetID

num_of_players = int(input("Welcome! Please enter the number of players you'd like to analyze." +
                           " You can only analyze up to 10: "))

if num_of_players > 10:
    print("Entered too many players. Program shutting down!")
    quit()

# Lists for the playersIDs and corresponding names
players_IDs, players_names = [], []

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

print(players_IDs, players_names)
