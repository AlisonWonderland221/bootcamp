import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
import seaborn as sns

# Part A - import files
wild = np.loadtxt('data/wt_lac.csv', delimiter=',', skiprows=3)
q18m = np.loadtxt('data/q18m_lac.csv', delimiter=',', skiprows=3)
q18a = np.loadtxt('data/q18a_lac.csv', delimiter=',', skiprows=3)

iptg_wild = wild[:,0]
fold_wild = wild[:,1]
iptg_q18m = q18m[:,0]
fold_q18m = q18m[:,1]
iptg_q18a = q18a[:,0]
fold_q18a = q18a[:,1]

Rk = [141.5, 1332, 16.56]

# Part B - make plot

# # plot for wild type
# plt.loglog(iptg_wild, fold_wild, linestyle='none', marker='.', markersize=10)
# plt.loglog(iptg_q18m, fold_q18m, linestyle='none', marker='.', markersize=10)
# plt.loglog(iptg_q18a, fold_q18a, linestyle='none', marker='.', markersize=10)
# plt.legend(('wild type', 'q18m', 'q18a'), loc='lower right')
# plt.xlabel('IPTG (mM)')
# plt.ylabel('Fold Change (mM)')
# plt.show()

# Part C
def fold_change(c, RK, KdA=0.017, KdI=0.002, Kswitch=5.8):
    fold_change = ((1 + (RK * (1 + c / KdA)**2) / ((1 + c / KdA)**2 + (Kswitch * (1 + c / KdI)**2)))**-1)
    return fold_change

# Part D
theory_c_wild = np.logspace(start=-6, stop=2)
theory_fc_wild = fold_change(theory_c_wild, Rk[0], KdA=0.017, KdI=0.002, Kswitch=5.8)
theory_c_q18m = np.logspace(start=-6, stop=2)
theory_fc_q18m = fold_change(theory_c_q18m, Rk[1], KdA=0.017, KdI=0.002, Kswitch=5.8)
theory_c_q18a = np.logspace(start=-6, stop=2)
theory_fc_q18a = fold_change(theory_c_q18a, Rk[2], KdA=0.017, KdI=0.002, Kswitch=5.8)

plt.loglog(iptg_wild, fold_wild, linestyle='none', marker='.', markersize=10)
plt.loglog(iptg_q18m, fold_q18m, linestyle='none', marker='.', markersize=10)
plt.loglog(iptg_q18a, fold_q18a, linestyle='none', marker='.', markersize=10)
plt.plot(theory_c_wild, theory_fc_wild)
plt.plot(theory_c_q18m, theory_fc_q18m)
plt.plot(theory_c_q18a, theory_fc_q18a)
plt.legend(('wild type', 'q18m', 'q18a', 'wild type theory', 'q18m theory', 'q18a theory'), loc='lower right')
plt.xlabel('IPTG (mM)')
plt.ylabel('Fold Change (mM)')
plt.show()
