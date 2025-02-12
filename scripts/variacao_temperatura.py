import sys
import pandas as pd
import matplotlib.pyplot as plt
import zipfile


# Lê os dados do arquivo especificado em 'file_path', calcula a variação de temperatura
# e exibe o nome do país seguido da temperatura correspondente.
def analyze_temperature_variation(zip_path, file_name):
    with zipfile.ZipFile(zip_path, 'r') as zip_file:
        df = pd.read_csv(zip_file.open(file_name), skiprows=5)
        temperature = df['temperature_C']
        print('%s | %.2f' % (file_name[:-4].upper(), temperature.max() - temperature.min()))

zip_path = sys.argv[1]
file_name = sys.argv[2]

analyze_temperature_variation(zip_path, file_name)