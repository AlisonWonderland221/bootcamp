import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import bootcamp_utils
sns.set()

bd_1975 = np.loadtxt('data/beak_depth_scandens_1975.csv')

x_bd_1975, y_bd_1975 = bootcamp_utils.ecdf(bd_1975)


for i in range(100):
    sample = np.random.choice(bd_1975, replace=True, size=len(bd_1975))
    x, y = bootcamp_utils.ecdf(sample)
