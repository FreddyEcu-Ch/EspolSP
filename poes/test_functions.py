#%% Import Python Libraries

import xlwings as xw
import numpy as np
import pandas as pd
from scipy.stats import expon, lognorm, norm, triang, uniform
from poes.Model.poes import poes
from poes.Model.utils import param_stoiip





#%% #%% Call workbook
wb = xw.Book("poes/Controller/poes.xlsm")
sheet= wb.sheets["Summary"]
#%% Call Dataframe

    params = sheet[DET_VALUES].options(np.array, transpose=True).value
    sheet[POES_DET].value = poes(*params)

    Distributions = [Triangular, Normal, Lognormal, Normal, Exponential]








#%% Test param_stoiip function