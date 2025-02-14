"""
Lê os arquivos e gera gráficos em barra das regiões com as cinco maiores e cinco 
menores variações de temperatura.

O caminho até o arquivo com os dados em formato CSV deve ser o primeiro
argumento da linha de comando. As figuras são armazenadas em code/img/.
"""

import sys
import pathlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# O caminho para o arquivo é recebido pela linha de comando
file_path = pathlib.Path(sys.argv[1])

# Lê o csv ignorando comentários
data = pd.read_csv(
    file_path, comment="#", sep="|", names=["regiao", "variacao_temperatura"]
)

# Ordena dados pela variação de temperatura
data = data.sort_values(by="variacao_temperatura")

fig, ax = plt.subplots()

# Gráfico das 5 menores variações
bar_labels = data["regiao"].head(5)

ax.bar(data["regiao"].head(5), data["variacao_temperatura"].head(5), label=bar_labels)

ax.set_ylabel("Taxa de variação de temperatura (°C/ano)")
ax.set_title("Menores Variações de Temperatura")

# Salva gráfico
plt.savefig("code/img/cinco_menores_taxas")


# Gráfico das 5 maiores variações
fig, ax = plt.subplots()

bar_labels = data["regiao"].tail(5)

ax.bar(data["regiao"].tail(5), data["variacao_temperatura"].tail(5), label=bar_labels)

ax.set_ylabel("Variação de temperatura")
ax.set_title("Maiores Variações de Temperatura")
ax.legend(title="Região")

# Salva gráfico
plt.savefig("code/img/cinco_maiores_taxas")
