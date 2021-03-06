import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
import seaborn as sns

rc = {'lines.linewidth' : 2, 'axes.labelsize' : 18, 'axes.titlesize' : 18}
sns.set(rc=rc)

data_txt = np.loadtxt('data/collins_switch.csv', delimiter=',', skiprows=2)

# Slice out itpg and gfp
iptg = data_txt[:,0]
gfp = data_txt[:,1]
sem = data_txt[:,2]
#
# # Plot semilog igpt vs gfp
# plt.semilogx(iptg, gfp, linestyle='none', marker='.', markersize=20)
# plt.xlabel('IPTG mM')
# plt.ylabel('Normalized GFP')
# plt.title('IPTG Titration - semilog X')
# plt.ylim(-0.02, 1.02)
# plt.xlim(8e-4, 15)
# plt.show()


# # Plot log-log
# plt.loglog(iptg, gfp, linestyle='none', marker='.', markersize=20)
# plt.xlabel('IPTG mM')
# plt.ylabel('Normalized GFP')
# plt.title('IPTG Titration - Log-Log')
# plt.ylim(-0.02, 1.02)
# plt.xlim(8e-4, 15)
# plt.show()


# # Plot error bar igpt vs gfp
# plt.errorbar(iptg, gfp, yerr=sem, linestyle='none', marker='.', markersize=20)
# plt.xlabel('IPTG mM')
# plt.ylabel('Normalized GFP')
# plt.title('IPTG Titration - semilog X with Error Bars')
# plt.ylim(-0.02, 1.02)
# plt.xlim(8e-4, 15)
# plt.xscale('log')
# plt.show()
