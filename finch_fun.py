import numpy as np
import seaborn as scs
import matplotlib.pyplot as plt
import pandas as pd

def ecdf(data):
    '''
    Compute x, y values for an empirical distribution function
    '''
    x = np.sort(data)
    y = np.arange(1, 1+len(x)) / len(x)

    return x, y

df = pd.read_csv('data/grant_complete.csv', comment='#')

# Part D

# Pull out data with parameters
df_beaks_f = df.loc[(df['year'] == 1987) & (df['species'] == 'fortis'), ['beak depth (mm)']]
df_beaks_s = df.loc[(df['year'] == 1987) & (df['species'] == 'scanden'), ['beak depth (mm)']]

#Calculate ECDF
ecdf_beaks_fx, ecdf_beaks_fy = ecdf(df_beaks_f)
ecdf_beaks_sx, ecdf_beaks_sy = ecdf(df_beaks_s)

#Plot
# plt.plot(ecdf_beaks_fx, ecdf_beaks_fy, marker = '.', linestyle = 'none')
# plt.plot(ecdf_beaks_sx, ecdf_beaks_sy, marker = '.', linestyle = 'none')
# plt.xlabel('Beak Depth (mm)')
# plt.ylabel('ECDF')

# plt.show()

#Part E

df_beaks_f = df.loc[(df['year'] == 1987) & (df['species'] == 'fortis'), ['beak depth (mm)', 'beak length (mm)']]
df_beaks_s = df.loc[(df['year'] == 1987) & (df['species'] == 'scandens'), ['beak depth (mm)', 'beak length (mm)']]

plt.plot(df_beaks_f['beak depth (mm)'], df_beaks_f['beak length (mm)'], marker ='.', linestyle='none', color='blue')
plt.plot(df_beaks_s['beak depth (mm)'], df_beaks_s['beak length (mm)'], marker ='.', linestyle='none', color='red')

plt.show()
