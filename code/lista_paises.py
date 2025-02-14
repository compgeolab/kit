# Cria uma lista dos países analisados definidos em uma variável do LaTeX
# Recebe o caminho da pasta com os arquivos na linha de comando.
# Imprime a definição da variável LaTeX.
import sys
import pathlib


# Pega a pasta de dados da linha de comando
data_folder = pathlib.Path(sys.argv[1])
# Acha todos os arquivos .csv da pasta
data_files = data_folder.glob("*.csv")
# Transforma os nomes dos arquivos em nomes dos países
countries = sorted(f.stem.replace("-", " ").title() for f in data_files)
# Gera uma string com a definição da variável
# Para inserir o character {} numa f-string, usamos {{}}
latex_variable = f"\\newcommand{{\\Paises}}{{{'; '.join(countries)}}}"
# Imprime a definição da variável
print(latex_variable)
