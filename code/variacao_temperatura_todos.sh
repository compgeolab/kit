# Script que calcula a variação de temperatura para cada um dos países e os
# colocar em um único arquivo.
#
# O primeiro argumento deve ser a pasta onde estão os dados CSV.
# O segundo argumeto deve ser o caminho para o arquivo de saída.

# Inicializa o arquivo de saída com a string vazia. Sem isso a gente sempre
# adicionaria no arquivo caso o script seja rodado múltiplas vezes.
# O -n diz para o echo não adicionar uma quebra de linha. Assim não ficamos com
# a primeira linha do arquivo vazia.
echo -n "" > "$2"

# O comando entre $() é rodado primeiro. Ele lista os arquivos que terminam em
# .csv na pasta dada (ls) e conta o número de linhas (wc) na resposta, dando
# o número de arquivos.
echo "Analisando $(ls "$1"/*.csv | wc -l) arquivos:"

# Para cada arquivo que termina em .csv, faça:
for file in "$1"/*.csv; do
    echo -n "  Processando $file ..."
    # Roda o script Python com o arquivo e adiciona o resultado no arquivo de
    # saída dado. O $(dirname $0) pega o diretório de desse script. Assim
    # o script Python é achado sempre, mesmo se rodarmos o script fora dessa
    # pasta.
    python "$(dirname "$0")"/variacao_temperatura.py "$file" >> "$2";
    echo " feito!"
done
echo "Processo terminado."
