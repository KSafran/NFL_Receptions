import download_reception_data
import pandas as pd
import matplotlib.pyplot
import numpy as np

# download_reception_data.download_season_data(2015)
# download_reception_data.download_season_data(2016)
# download_reception_data.download_season_data(2017)

receivers_15 = pd.read_csv('receiving_leaders_2015.csv')
receivers_16 = pd.read_csv('receiving_leaders_2016.csv')
receivers_17 = pd.read_csv('receiving_leaders_2017.csv')

all_data = pd.concat([receivers_15, receivers_16, receivers_17])

drop_these_cols = ['2PM', 'AY/A', 'Ast', 'Att', 'Att.1', 'Cmp', 'Cmp%',
                   'Ctch%', 'Int', 'Ret', 'Sk', 'TD', 'TD.1', 'TD.2',
                   'TD.3', 'TD.4', 'TD.5', 'Tkl', 'Unnamed: 0',
                   'Unnamed: 7',  'Unnamed: 8', 'Unnamed: 9',
                   'Unnamed: 10', 'Y/A', 'Y/A.1', 'Y/Rt']
all_data = all_data.drop(drop_these_cols, 1)

# First let's try an exponential smoothing model