#%% Import Python Libraries

import numpy as np
from poes.Model.poes import poes

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
