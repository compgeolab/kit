# Conta o número de dados de cada arquivo
#
# Imprime os resultados para a tela (STDOUT).
# Deve ser rodado a partir da raiz do repositório.

# Para cada arquivo .csv na pasta data como argumento
for arquivo in dados/temperatura/*.csv
do
    # O comando "echo" imprime algo na tela.
    # O que está entre $() é executado primeiro e o seu resultado é passado
    # como argumento do outro comando. No caso, o resultado do "tail ..."
    # é passado como o primeiro argumento do echo e o segundo é o nome do
    # arquivo, fazendo ele imprimir o número de dados seguidos do nome do
    # arquivo. Usa o tail para remover o cabeçalho dos arquivos.
    echo "$(tail -n +7 "$arquivo" | wc -l)" "$arquivo"
done
