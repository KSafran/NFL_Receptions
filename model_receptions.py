import download_reception_data
import pandas as pd

download_reception_data.download_season_data(2015)
download_reception_data.download_season_data(2016)
download_reception_data.download_season_data(2017)

receivers_15 = pd.read_csv('receiving_leaders_2015.csv')
receivers_16 = pd.read_csv('receiving_leaders_2016.csv')
receivers_17 = pd.read_csv('receiving_leaders_2017.csv')