# Let's pull data for the top ~ 150 receivers. This includes RBs and TEs

import pandas as pd
import pull_season_data
import numpy as np

leading_2017_receivers = pd.read_html('https://www.pro-football-reference.com/years/2017/receiving.htm')[0]
leading_2017_receivers.rename(columns = {leading_2017_receivers.columns[1]: 'player'}, inplace = True)

player_lookup = pd.read_csv('player ids.csv')

data_list = []
for player in leading_2017_receivers['player']:
    if pd.isnull(player):
        break
    if player == 'Antonio Brown':
        receiver_df = pull_season_data.get_season_gamelog(player, 2017, player_lookup)
        print(receiver_df.head())
    else:
        break