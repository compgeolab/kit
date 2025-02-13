import sys
import pandas as pd
import matplotlib.pyplot as plt
import zipfile
import numpy as np

# Lê os dados do arquivo especificado em 'file_path', calcula a variação de temperatura
# e exibe o nome do país seguido da temperatura correspondente.
zip_path = 'dados/temperature-data.zip'
file_name = sys.argv[1]

with zipfile.ZipFile(zip_path, 'r') as zip_file:
    df = pd.read_csv(zip_file.open(file_name), skiprows=5)
    
    df['year'] = pd.to_numeric(df['year'], downcast='integer')
    df = df.sort_values(by='year')

    # Cria um dataframe dos últimos 10 anos
    current_year = df['year'].unique()[-1]
    df = df[df['year'] >= current_year - 9]

    # Regressão linear
    coefficients = np.polyfit(df['year_decimal'], df['temperature_C'], 1)

    # Impressão de resultados
    print('%s | %.3f' % ((file_name[0].upper() + file_name[1:-4]), coefficients[0]))
