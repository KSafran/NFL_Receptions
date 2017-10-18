# Each player has a unique player id in pro football reference. This is useful for
# looking up player's stats. We want to be able to just type a player's name and get
# their ID.

import pandas as pd

player_lookup = pd.read_csv('player ids.csv')

def get_player_id(player_name, player_lookup):
    player = player_lookup.loc[player_lookup['player_name'] == player_name, :]
    return(player.loc[player['active'] == 1, 'player_id'].values[0])