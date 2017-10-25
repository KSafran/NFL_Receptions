# Let's pull data for the top ~ 150 receivers. This includes RBs and TEs

import pandas as pd
import pull_season_data
import re

def download_season_data(season, num_players = 150):
    '''Downloads a season worth of wide receiver data

    season -- an int representing what season you want to pull (e.g. 2017)
    num_players -- I want to pull the top x wide receivers (defaults to 150)

    This function requires the player ids.csv file to be in the users working
    directory. It saves a file named receiving_leaders_*season*.csv '''


    leading_receivers = pd.read_html('https://www.pro-football-reference.com/years/' + str(season) + '/receiving.htm')[0]
    leading_receivers = leading_receivers.iloc[:num_players,:]
    leading_receivers.rename(columns = {leading_receivers.columns[1]: 'player'}, inplace = True)
    leading_receivers['player'] = [str(x) for x in leading_receivers['player']]

    leading_receivers['player'] = [re.sub('[*|+]', '', x) for x in leading_receivers['player']]
    player_lookup = pd.read_csv('player ids.csv')

    data_list = []
    count = 0
    for player in leading_receivers['player']:
        count += 1
        try:
            receiver_df = pull_season_data.get_season_gamelog(player, season, player_lookup)
            receiver_df['season'] = season
            receiver_df['player'] = player
            data_list.append(receiver_df)
            if count % 10 == 0:
                print(count)
        except:
            pass


    receivers = pd.concat(data_list)
    receivers.to_csv('receiving_leaders_' + str(season) + '.csv')