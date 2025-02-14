# Script que calcula a variação de temperatura para cada um dos países e os
# colocar em um único arquivo CSV.
#
# O primeiro argumento deve ser a pasta onde estão os dados CSV.
# O resultado será impresso na tela.

# Inicializa a saída com o nome das colunas
echo "variacao_C_por_ano,pais"

# O comando entre $() é rodado primeiro. Ele lista os arquivos que terminam em
# .csv na pasta dada (ls) e conta o número de linhas (wc) na resposta, dando
# o número de arquivos. O >&2 significa redirecionar a saída para o canal de
# erros. Assim essa mensagem não será adicionada ao arquivo quando
# redirecionarmos a saída desse script. Isso normalmente é usado para imprimir
# mensagens durante o processamento que não são parte do resultado do script.
echo "Analisando $(ls "$1"/*.csv | wc -l) arquivos:" >&2

# Para cada arquivo que termina em .csv, faça:
for file in "$1"/*.csv; do
    echo -n "  Processando $file ..." >&2

    # Roda o script Python com o arquivo.
    # O $(dirname $0) pega o diretório de desse script. Assim o script Python
    # é achado sempre, mesmo se rodarmos o script fora dessa pasta.
    python "$(dirname "$0")"/variacao_temperatura.py "$file"

    echo " feito!" >&2
done
echo "Processo terminado." >&2
