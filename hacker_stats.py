import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.set()

bd_1975 = np.loadtxt('data/beak_depth_scandens_1975.csv')
bd_2012 = np.loadtxt('data/beak_depth_scandens_2012.csv')

bs_sample = np.random.choice(bd_1975, replace=True, size=len(bd_1975))
bs_replicate = np.mean(bs_sample)

#Generate bootstrap
n_reps = 100000
bs_replicates_1975 = np.empty(n_reps)
for i in range(n_reps):
    bs_sample = np.random.choice(bd_1975, replace=True, size=len(bd_1975))
    bs_replicates_1975[i] = np.std(bs_sample)

conf_int_1975 = np.percentile(bs_replicates_1975, [2.5, 97.5])

n_reps = 100000
bs_replicates_2012 = np.empty(n_reps)
for i in range(n_reps):
    bs_sample = np.random.choice(bd_2012, replace=True, size=len(bd_2012))
    bs_replicates_2012[i] = np.std(bs_sample)

conf_int_2012 = np.percentile(bs_replicates_2012, [2.5, 97.5])


def ecdf(data):
    '''
    Compute x, y values for an empirical distribution function
    '''
    x = np.sort(data)
    y = np.arange(1, 1+len(x)) / len(x)

    return x, y

x_1975, y_1975 = ecdf(bd_1975)
x_2012, y_2012 = ecdf(bd_2012)
x_1975_bs, y_1975_bs = ecdf(bs_sample)

# plt.plot(x_1975, y_1975, marker='.', linestyle='none')
# plt.plot(x_1975_bs, y_1975_bs, marker='.', linestyle='none')
# plt.xlabel('Beak depth (mm)')
# plt.ylabel('ECDF')
# plt.legend(('1975', 'Bootstrap'), loc='lower right')
# plt.show()
