# Pipeline que gera os resultados, figuras e o PDF do artigo
###############################################################################

# Define variáveis para utilizar ao longo do Makefile
###############################################################################
# Lista de arquivos com variáveis LaTeX gerados pelo código
VARIAVEIS = paper/variaveis/n_paises.tex paper/variaveis/paises.tex
# Lista de figuras para o artigo
FIGURAS =
# Lista de arquivos de dados. A função wildcard do Make expande o *.csv em
# vários nomes de arquivos.
DADOS = $(wildcard dados/*.csv)

# Regras para geração dos produtos
###############################################################################
# Atalho para gerar o PDF sem ter que escrever "make paper/paper.pdf"
pdf: paper/paper.pdf

# Gera o PDF com o tectonic. Depende do LaTeX, Bibtex, figuras e variáveis
paper/paper.pdf: paper/paper.tex paper/referencias.bib $(FIGURAS) $(VARIAVEIS)
	tectonic -X compile $<

# Regra para remover todos os arquivos gerados pelo Make. Isso é padrão em
# quase todos os Makefiles.
clean:
	rm -v -f paper/paper.pdf resultados/variacao_temperatura.csv $(VARIAVEIS)

# Gera os resultados de variação de temperatura
resultados/variacao_temperatura.csv: code/variacao_temperatura_todos.sh code/variacao_temperatura.py $(DADOS)
	# O mkdir -p cria a pasta caso ela não exista. O -p faz com que não ocorra
	# um erro se a pasta já existir.
	mkdir -p resultados
	bash $< dados > $@

# Regras para gerar as variáveis utilizadas no LaTeX
paper/variaveis/n_paises.tex: $(DADOS)
	# O mkdir -p cria a pasta caso ela não exista. O -p faz com que não ocorra
	# um erro se a pasta já existir.
	mkdir -p paper/variaveis
	printf "%s" "\\newcommand{\\NPaises}{`ls dados/*.csv | wc -l`}" > $@

paper/variaveis/paises.tex: code/lista_paises.py $(DADOS)
	# O mkdir -p cria a pasta caso ela não exista. O -p faz com que não ocorra
	# um erro se a pasta já existir.
	mkdir -p paper/variaveis
	python $< dados > $@
