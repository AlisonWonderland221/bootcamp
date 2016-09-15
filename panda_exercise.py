import numpy as np
import pandas as pd

df = pd.read_csv('data/frog_tongue_adhesion.csv', comment='#')

big_strike_time = df.loc[abs(df['adhesive strength (Pa)']) > 2000, 'impact time (ms)']
frog_two = df.loc[df['ID']=='II', ['impact force (mN)', 'adhesive force (mN)']]
juvenile = df.loc[(df['ID'] == 'III') | (df['ID'] == 'IV'), ['adhesive force (mN)', 'impact time (ms)']]

df_ID = (df.loc[:, ['ID', 'impact force (mN)', 'adhesive force (mN)']])
df_grouped = df_ID.groupby('ID')


def coeff_of_var(data):
    num = df.grouped(np.std)
    denom = abs(df.grouped(np.mean))
    coeff_of_var = num / denom
    return coeff_of_var

df_var_I = coeff_of_var(df_impact_I)
df_var_II = coeff_of_var(df_impact_II)
df_var_III = coeff_of_var(df_impact_III)
df_var_IV = coeff_of_var(df_impact_IV)
