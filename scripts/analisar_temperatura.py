import sys
import pandas as pd
import matplotlib.pyplot as plt
import zipfile

zip_path = sys.argv[1]

data = dict()

# Lê a pasta zip
with zipfile.ZipFile(zip_path, 'r') as zip_file:
    # Itera sobre cada arquivo dentro da pasta zip
    for file in zip_file.namelist():
        if file != 'README.md': # Evita o README.md
            # No dicionário, atribui a cada arquivo os dados correspondentes
            data[file[:-4]] = pd.read_csv(zip_file.open(file), skiprows=5)

for name in data.keys():
    df = data[name]
    plt.plot(df['year_decimal'], df['temperature_C'])

plt.savefig('plots/teste.png')