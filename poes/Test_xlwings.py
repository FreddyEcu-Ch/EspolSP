# %% Import Python libraries

import xlwings as xw
import numpy as np
import pandas as pd

# %% Create a workbook from Python

wb = xw.Book()

# %% Define sheet

sheet = wb.sheets[0]

# %% Create a value from Python

sheet["C3"].value = "Barcelona"

# %% Call values form MS Excel to Python

values = sheet["F4:F6"].value
print(values)

# %% Create a numpy array from Ms Excel to Python

sheet["D9"].options(np.array, transpose=True).value = np.array([1, 2, 3, 4, 5])

# %% Call numpy array from MS Excel to Python

arrays = sheet["D9:D13"].value
print(arrays)

# %% Create a pandas DataFrame from Python to Ms Excel

sheet["D15"].options(pd.DataFrame, expand="table", index=False).value = pd.DataFrame(
    {
        "OilField": ["Sacha", "Auca", "Sushufindi"],
        "Well": ["Sa-1", "Auc-5", "Shu-9"],
        "Production (bopd)": [500, 650, 300],
    }
)

# %% Call dataframe from Ms Excel to Python

df = sheet["D15"].options(pd.DataFrame, expand="table", index=False).value
print(df)
