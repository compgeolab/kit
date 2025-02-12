import sys
import os
import pandas as pd
import matplotlib.pyplot as plt

# Lê os dados do arquivo especificado em 'file_path', calcula a variação de temperatura
# e exibe o nome do país seguido da temperatura correspondente.
def analyze_temperature(file_path):
    df = pd.read_csv(file_path)