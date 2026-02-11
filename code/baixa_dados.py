"""
Baixa os dados de temperatura média mensal para diversos países.

O arquivo zip será baixado na pasta `data` e deszipado em uma pasta
"temperatura" dentro dessa mesma pasta.

O script deve ser rodado a partir da raiz do repositório.

Os dados estão disponíveis em https://github.com/compgeolab/temperature-data
sob uma licença CC-BY-NC. Estes dados foram derivados dos dados produzidos pelo
Berkeley Earth (https://berkeleyearth.org/).

Utiliza a biblioteca Pooch (https://www.fatiando.org/pooch) para baixar os
dados.
"""
import pooch


# A URL e o hash MD5 foram copiados do repositório de dados
p = pooch.retrieve(
    url="https://github.com/compgeolab/temperature-data/releases/download/2025-02-11/temperature-data.zip",
    known_hash="md5:d102212049af1695b686c94ae1eea233",
    processor=pooch.Unzip(extract_dir="temperatura"),
    fname="temperature-data.zip",
    path="data",
)
