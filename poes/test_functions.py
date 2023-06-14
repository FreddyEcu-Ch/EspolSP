#%% Import Python Libraries
import numpy as np
import matplotlib.pyplot as plt
import xlwings as xw
import pandas as pd
from scipy.stats import norm, lognorm, expon, triang, uniform



#%% #%% Call workbook

wb = xw.Book("poes/Controller/poes.xlsm")
sheet = wb.sheets("Summary")


#%% Call Dataframe

df = sheet["D15"].options(pd.DataFrame, expand="table", index=False).value
print(df)









#%% Test param_stoiip function
from poes.Model.poes from poes
from poes.Model.utils from param_stoiip