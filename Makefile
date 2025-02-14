# Pipeline que gera os resultados, figuras e o PDF do artigo
VARIAVEIS = paper/variaveis/n_paises.tex paper/variaveis/paises.tex
FIGURAS =
DADOS = $(wildcard dados/*.csv)

pdf: paper/paper.pdf

paper/paper.pdf: paper/paper.tex paper/referencias.bib $(FIGURAS) $(VARIAVEIS)
	tectonic -X compile $<

clean:
	rm -v -f paper/paper.pdf resultados/variacao_temperatura.csv $(VARIAVEIS)

resultados/variacao_temperatura.csv: code/variacao_temperatura_todos.sh code/variacao_temperatura.py $(DADOS)
	mkdir -p resultados
	bash $< dados > $@

paper/variaveis/n_paises.tex: $(DADOS)
	mkdir -p paper/variaveis
	printf "%s" "\\newcommand{\\NPaises}{`ls dados/*.csv | wc -l`}" > $@

paper/variaveis/paises.tex: code/lista_paises.py $(DADOS)
	mkdir -p paper/variaveis
	python $< dados > $@
