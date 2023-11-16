import csv
import numpy as np

# Input data
import pandas as pd

data = np.loadtxt('pstar_data.txt')

pd.DataFrame(data).to_csv("output.csv", header=['Energy', 'Stopping_power'], index=None)