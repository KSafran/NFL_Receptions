import pandas as pd
import numpy as np

def get_player_id(player_name, player_lookup):
    player = player_lookup.loc[player_lookup['player_name'] == player_name, :]
    return(player.loc[:, 'player_id'].values[0])

def create_season_url(player_id, year):
    return('https://www.pro-football-reference.com/players/'
           + player_id[0] + '/' + player_id
           + '/gamelog/' + str(year))

def get_season_gamelog(player_name, year, player_lookup):
    player_id = get_player_id(player_name=player_name, player_lookup=player_lookup)
    season_url = create_season_url(player_id = player_id, year = year)
    temp_df = pd.read_html(season_url)[0]
    # Table names are not imported correctly, let's fix that
    # Rk is the first real column, but it could be anywhere
    rk_index = np.argwhere(temp_df.columns.values == 'Rk')[0][0]
    true_names = temp_df.columns.values[rk_index:]
    output = temp_df.iloc[:, :-rk_index]
    output.columns = true_names
    return(output)