# Conta o número de dados de cada arquivo
#
# Recebe o caminho até a pasta com os dados na linha de comando. Imprime os
# resultados para a tela (STDOUT).

# Para cada arquivo .csv na pasta data como argumento
# As variáveis 1, 2, 3, ..., contem os argumentos passados na linha de comando
# para o script. Nesse caso, "$1" é o primeiro argumento passado (a pasta onde
# estão os dados).
for arquivo in "$1"/*.csv
do
    # O comando "echo" imprime algo na tela.
    # O que está entre $() é executado primeiro e o seu resultado é passado
    # como argumento do outro comando. No caso, o resultado do "tail ..."
    # é passado como o primeiro argumento do echo e o segundo é o nome do
    # arquivo, fazendo ele imprimir o número de dados seguidos do nome do
    # arquivo. Usa o tail para remover o cabeçalho dos arquivos.
    echo "$(tail -n +7 "$arquivo" | wc -l)" "$arquivo"
done
