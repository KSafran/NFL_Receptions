import matplotlib.pyplot as plt
import pull_season_data

def plot_receptions(player_name, year, player_lookup, targets = False):
    '''Plots a player's receptions and optionally targets

    player_name -- a football players name, string
    year -- which season to pull, int (e.g. 2017)
    player_lookup -- the player lookup data, comes from player ids.csv
    targets -- boolean, whether or not to include targets in the plot, default = False'''
    df = pull_season_data.get_season_gamelog(player_name, year, player_lookup)
    plt.plot(df.Rk, df.Rec, color = 'green')
    if targets:
        plt.plot(df.Rk, df.Tgt, color = 'blue')
    plt.show()