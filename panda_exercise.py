import numpy as np
import pandas as pd

df = pd.read_csv('data/frog_tongue_adhesion.csv', comment='#')

#Part 1
big_strike_time = df.loc[abs(df['adhesive strength (Pa)']) > 2000, 'impact time (ms)']
frog_two = df.loc[df['ID']=='II', ['impact force (mN)', 'adhesive force (mN)']]
juvenile = df.loc[(df['ID'] == 'III') | (df['ID'] == 'IV'), ['adhesive force (mN)', 'impact time (ms)']]

# Part 2
df_ID = (df.loc[:, ['ID', 'impact force (mN)', 'adhesive force (mN)']])
df_grouped = df_ID.groupby('ID')
df_calc = df_grouped.agg([np.std, np. mean])


# really inefficient way of calculating coefficient of variation
df_coeff_var = df_grouped.apply(np.std)/abs(df_grouped.apply(np.mean))

df_all =df_grouped.agg([np.mean, np.median, np.std])
df_really_all = pd.concat((df_all, df_coeff_var), axis=1)
