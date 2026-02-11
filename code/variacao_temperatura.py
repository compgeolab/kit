"""
Calcula a taxa de variação de temperatura dos últimos 5 anos para todos os
países.

Os resultados são impressos no STDOUT.
"""

import pathlib
import pandas as pd
import numpy as np


data_folder = pathlib.Path("data/temperatura")

# Acha todos os arquivos .csv da pasta
data_files = data_folder.glob("*.csv")

# Começa a saída com um cabeçalho
print("variacao_C_por_ano,pais")

for file_path in data_files:
    # Lê o csv ignorando comentários
    data = pd.read_csv(file_path, comment="#")
    # Filtra dados dos últimos cinco anos
    last_five_years = data[data.year_decimal > data.year_decimal.iloc[-1] - 5]
    # Regressão linear
    coefficients = np.polyfit(
        last_five_years.year_decimal, last_five_years.temperature_C, 1
    )
    # Impressão de resultados
    print(f'{coefficients[0]:.3f},"{file_path.stem.replace("-", " ").title()}"')
