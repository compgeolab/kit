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
    file_path, comment="#", sep="|", names=["pais", "variacao_temperatura"]
)

# Ordena dados pela variação de temperatura
data = data.sort_values(by="variacao_temperatura")

# Criando dois subplots
fig, axes = plt.subplots(2, 1, figsize=(8, 6))

# Plot do top 5 menores variações de temperatura
axes[0].bar(data["pais"].head(5), data["variacao_temperatura"].head(5))
axes[0].set_ylabel("Taxa de variação de temperatura (°C/ano)")
axes[0].set_title("Cinco menores variações")

# Plot do top 5 maiores variações de temperatura
axes[1].bar(data["pais"].tail(5), data["variacao_temperatura"].tail(5))
axes[1].set_ylabel("Taxa de variação de temperatura (°C/ano)")
axes[1].set_title("Cinco maiores variações")

# Ajusta o layout para evitar sobreposição de elementos
plt.tight_layout()

# O caminho do arquivo da figura é passado pela linha de comando
fig_path = sys.argv[2]

# Armazena figora em diretório passado pela linha de comando
plt.savefig(fig_path)