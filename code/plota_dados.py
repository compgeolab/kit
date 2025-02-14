"""
Lê os arquivos e gera gráficos em barra das regiões com as cinco maiores e cinco
menores variações de temperatura.

O caminho até o arquivo com os dados em formato CSV deve ser o primeiro
argumento da linha de comando.
"""

import sys
import pathlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# O caminho para o arquivo é recebido pela linha de comando
file_path = pathlib.Path(sys.argv[1])

# O caminho do arquivo da figura é passado pela linha de comando
fig_path = sys.argv[2]

# Lê os dados do CSV
data = pd.read_csv(file_path)

# Ordena dados pela variação de temperatura
data = data.sort_values(by="variacao_C_por_ano")

# Criando dois subplots
fig, axes = plt.subplots(2, 1, figsize=(5, 7), layout="constrained")

# Set o label do eixo y, adiciona um grid e rotaciona os nomes dos países
for ax in axes:
    ax.set_ylabel("Taxa de variação\nde temperatura (°C/ano)")
    ax.tick_params(axis='x', labelrotation=20)
    ax.grid(axis="y", linestyle="--")
    ax.set_axisbelow(True)

# Plot do top 5 maiores variações de temperatura
axes[0].bar(data["pais"].tail(5), data["variacao_C_por_ano"].tail(5), color="#666666")
axes[0].set_title("Cinco maiores variações")

# Plot do top 5 menores variações de temperatura
axes[1].bar(data["pais"].head(5), data["variacao_C_por_ano"].head(5), color="#666666")
axes[1].set_title("Cinco menores variações")

# Armazena figura em diretório passado pela linha de comando
plt.savefig(fig_path)
