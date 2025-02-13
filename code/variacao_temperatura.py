"""
Calcula a taxa de variação de temperatura dos últimos 5 anos para um determinado pais.

O caminho até o arquivo com os dados em formato CSV deve ser o primeiro
argumento da linha de comando. Os resultados são impressos no STDOUT.
"""

import sys
import pathlib
import pandas as pd
import numpy as np


# O caminho para o arquivo é recebido pela linha de comando
file_path = pathlib.Path(sys.argv[1])

# Read the csv ignoring the comments 
data = pd.read_csv(file_path, comment="#")

# Filter data from the last five year
last_five_years = data.year_decimal > data.year_decimal.iloc[-1] - 5

# Regressão linear
coefficients = np.polyfit(
    data.year_decimal[last_five_years], data.temperature_C[last_five_years], 1
)

# Impressão de resultados
print(f'{file_path.stem.replace("-", " ").title()} | {coefficients[0]:.3f}')
