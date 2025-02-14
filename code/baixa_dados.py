"""
Baixa os dados de temperatura média mensal para diversos países.

Recebe o nome da pasta onde os dados serão baixados pela linha de comando.

O arquivo zip será baixado na pasta acima e deszipado em uma pasta
"temperatura" dentro dessa mesma pasta.

Os dados estão disponíveis em https://github.com/compgeolab/temperature-data
sob uma licença CC-BY-NC. Estes dados foram derivados dos dados produzidos pelo
Berkeley Earth (https://berkeleyearth.org/).

Utiliza a biblioteca Pooch (https://www.fatiando.org/pooch) para baixar os
dados.
"""
import sys
import pooch


destination = sys.argv[1]

# A URL e o hash MD5 foram copiados do repositório de dados
p = pooch.retrieve(
    url="https://github.com/compgeolab/temperature-data/releases/download/2025-02-11/temperature-data.zip",
    known_hash="md5:d102212049af1695b686c94ae1eea233",
    processor=pooch.Unzip(extract_dir="temperatura"),
    fname="temperature-data.zip",
    path=destination,
)
