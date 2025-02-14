# Pipeline que gera os resultados, figuras e o PDF do artigo
###############################################################################

# Regras para geração dos produtos
###############################################################################

# Gera o PDF com o tectonic. Depende do LaTeX, Bibtex, figuras e variáveis
paper/paper.pdf: paper/paper.tex paper/referencias.bib figuras/taxas_variacao.png paper/variaveis/n_paises.tex paper/variaveis/paises.tex
	tectonic -X compile paper/paper.tex

# Regra para remover todos os arquivos gerados pelo Make.
# Isso é padrão em quase todos os Makefiles.
clean:
	rm -v -r -f paper/paper.pdf resultados/ paper/variaveis/ dados/ figuras/

dados/temperature-data.zip: code/baixa_dados.py
	python code/baixa_dados.py dados/

# Gera os resultados de variação de temperatura
resultados/variacao_temperatura.csv: code/variacao_temperatura_todos.sh code/variacao_temperatura.py dados/temperature-data.zip
	# O mkdir -p cria a pasta caso ela não exista.
	# O -p faz com que não ocorra um erro se a pasta já existir.
	mkdir -p resultados
	bash code/variacao_temperatura_todos.sh dados/temperatura > resultados/variacao_temperatura.csv

# Gera a figura a partir dos resultados
figuras/taxas_variacao.png: code/plota_dados.py resultados/variacao_temperatura.csv
	# O mkdir -p cria a pasta caso ela não exista.
	# O -p faz com que não ocorra um erro se a pasta já existir.
	mkdir -p figuras
	python code/plota_dados.py resultados/variacao_temperatura.csv figuras/taxas_variacao.png

# Regras para gerar as variáveis utilizadas no LaTeX
paper/variaveis/n_paises.tex: dados/temperature-data.zip
	# O mkdir -p cria a pasta caso ela não exista. O -p faz com que não ocorra
	# um erro se a pasta já existir.
	mkdir -p paper/variaveis
	printf "%s" "\\newcommand{\\NPaises}{`ls dados/temperatura/*.csv | wc -l`}" > paper/variaveis/n_paises.tex

paper/variaveis/paises.tex: code/lista_paises.py dados/temperature-data.zip
	# O mkdir -p cria a pasta caso ela não exista. O -p faz com que não ocorra
	# um erro se a pasta já existir.
	mkdir -p paper/variaveis
	python code/lista_paises.py dados/temperatura > paper/variaveis/paises.tex
