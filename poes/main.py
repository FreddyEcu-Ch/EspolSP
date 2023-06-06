#%% Import Python Libraries

import numpy as np
import matplotlib.pyplot as plt
from poes.Model.poes import poes
from scipy.stats import norm, lognorm, expon, triang, uniform

#%% Test function with single values

area = 200  # acres
h = 20  # ft2
poro = 0.30
swi = 0.27
boi = 1.2

stoiip = np.round(poes(area, h, poro, swi, boi), 2)
print(f"The POES of this reservoir is {stoiip} bbl")

#%% Test function with a values array

area = np.array([200, 180, 150, 215, 201])
poro = np.array([0.30, 0.31, 0.25, 0.27, 0.12])
h = np.array([15, 18, 21, 20, 22])
swi = np.array([0.15, 0.35, 0.28, 0.33, 0.40])
boi = np.array([1.1, 1.5, 1.17, 1.25, 1.3])

stoiip_array = np.round(poes(area, h, poro, swi, boi), 2)
print(stoiip_array)


#%% Generate random value for poes parameters
# random values for porosity

porosity_norm = norm.rvs(loc=0.4, scale=0.05, size=1000)
# State mim limit
porosity_norm = np.where(porosity_norm < 0, 0, porosity_norm)
# State max limit
porosity_norm = np.where(porosity_norm > 0.4, 0.4, porosity_norm)

# Random values with lognormal distribution
porosity_log = lognorm.rvs(s=0.1, loc=0, scale=0.05, size=1000)
porosity_log = np.where(porosity_log < 0, 0, porosity_log)
porosity_log = np.where(porosity_log > 0.4, 0.4, porosity_log)

# Random value with exponential distribution
porosity_expon = expon.rvs(loc=0, scale=0.05, size=1000)
porosity_expon = np.where(porosity_expon < 0, 0, porosity_expon)
porosity_expon = np.where(porosity_expon > 0.4, 0.4, porosity_expon)

# Random values with triangular distribution
porosity_tri = triang.rvs(c=0.3, loc=0, scale=0.4, size=1000)

# Random values with uniform distribution
porosity_uni = uniform.rvs(loc=0, scale=0.4, size=1000)

#%% Visualize porosity distributions
plt.hist(porosity_tri)
plt.show()


#%%
# random values for saturation
# Random values with normal distribution
saturacion_norm = norm.rvs(loc=0.4, scale=0.05, size=1000)
# State mim limit
saturacion_norm = np.where(saturacion_norm < 0, 0, saturacion_norm)
# State max limit
saturacion_norm = np.where(saturacion_norm > 1, 1, saturacion_norm)

# Random values with lognormal distribution
saturacion_log = lognorm.rvs(s=0.1, loc=0, scale=0.05, size=1000)
saturacion_log_log = np.where(saturacion_log < 0, 0, saturacion_log)
saturacion_log = np.where(saturacion_log > 1.0, 1.0, saturacion_log)

# Random value with exponential distribution
saturacion_expon = expon.rvs(loc=0, scale=0.05, size=1000)
saturacion_expon = np.where(saturacion_expon < 0, 0, saturacion_expon)
saturacion_expon = np.where(saturacion_expon > 1.0, 1.0, saturacion_expon)

# Random values with triangular distribution
saturacion_tri = triang.rvs(c=0.3, loc=0, scale=1.0, size=1000)

# Random values with uniform distribution
saturacion_uni = uniform.rvs(loc=0, scale=1.0, size=1000)
