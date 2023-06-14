#%% Import Python Libraries

import xlwings as xw
from scipy.stats import norm, lognorm, expon, triang, uniform
import numpy as np
import pandas as pd

from poes.Model.poes import poes
from poes.Model.utils import param_stoiip



#%% #%% Call workbook
wb = xw.Book("poes/Controller/poes.xlsm")
sheet = wb.sheet["Summary"]

#%% Call Dataframe

df = sheet["Distributions"].options(pd.DataFrame, expand="table", index=False).value
def param_stoiip(
        Distributions=(Triangular, Normal, Lognormal, Normal, Exponential),
        Loc = (400, 30, 0, 0.4, 1),
        Scale = (600, 90, 0.2, 0.2, 0.2),
        Sc = (0.3, 0, 0.8, None, None),
        Lim min = (50, 10, 0, 0, 1),
Lim max = (180, 80, 1, 1)
):








#%% Test param_stoiip function