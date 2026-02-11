# Cria uma lista dos países analisados definidos em uma variável do LaTeX
# Imprime a definição da variável LaTeX.
import pathlib


data_folder = pathlib.Path("data/temperatura")
# Acha todos os arquivos .csv da pasta
data_files = data_folder.glob("*.csv")
# Transforma os nomes dos arquivos em nomes dos países
countries = sorted(f.stem.replace("-", " ").title() for f in data_files)
# Gera uma string com a definição da variável
# Para inserir o character {} numa f-string, usamos {{}}
latex_variable = f"\\newcommand{{\\Paises}}{{{'; '.join(countries)}}}"
# Imprime a definição da variável
print(latex_variable)
