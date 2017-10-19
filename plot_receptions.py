import matplotlib.pyplot as plt
import pull_season_data

def plot_receptions(player_name, year, player_lookup, targets = False):
    df = pull_season_data.get_season_gamelog(player_name, year, player_lookup)
    plt.plot(df.Rk, df.Rec, color = 'green')
    if targets:
        plt.plot(df.Rk, df.Tgt, color = 'blue')
    plt.show()