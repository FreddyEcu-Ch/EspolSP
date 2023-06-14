# Import Python libraries
import xlwings as xw
import numpy as np
import pandas as pd
from poes.Model.poes import poes


# Define variables
# Define sheets
SHEET_SUMMARY = "Summary"
SHEET_RESULTS = "Results"

# Define column names
VARIABLES = "Variables"
VALUES = "Values"
DISTRIBUTIONS = "Distributions"
LOC = "Loc"
SCALE = "Scale"
SC = "Sc"
LIM_MIN = "Lim min"
LIM_MAX = "Lim max"

# Values to write from Ms Excel
DET_VALUES = "det_values"
DF_POES = "df_poes"
REALIZATIONS = "realizations"
SEED = "seed"

# Values to read from MS Excel
POES_DET = "poes_result"
POES_PROB = "poes_prob"
POES_ARRAY = "results_array"

# Index of POES Parameters
PORO_IDX, H_IDX, AREA_IDX, SWI_IDX, BOI_IDX = 0, 1, 2, 3, 4


def main():
    wb = xw.Book.caller()
    sheet = wb.sheets[SHEET_SUMMARY]

    # Call values from Deterministic POES
    params = sheet[DET_VALUES].options(np.array, transpose=True).value
    sheet[POES_DET].value = poes(*params)


if __name__ == "__main__":
    xw.Book("poes.xlsm").set_mock_caller()
    main()
