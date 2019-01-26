import pandas as pd
import glob
import os

files = glob.glob('RL_scraping_data/full/*.csv')
df = pd.concat(
    [pd.read_csv(fp, sep=';').assign(New=os.path.basename(fp).split('.')[0]) for fp in files]
    )

df.to_csv('champ.csv', index=False, sep=',')