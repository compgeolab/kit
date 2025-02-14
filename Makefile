# Pipeline que gera os resultados, figuras e o PDF do artigo
VARIAVEIS = paper/variaveis/n_paises.tex paper/variaveis/paises.tex
FIGURAS =
DADOS = $(wildcard dados/*.csv)

pdf: paper/paper.pdf

resultados/variacao_temperatura.csv: code/variacao_temperatura.py $(DADOS)
	echo "variacao_C_por_ano,pais" > $@
	for f in "${DADOS}"; do python $< $f >> $@; done

paper/variaveis/n_paises.tex: $(DADOS)
	printf "%s" "\\newcommand{\\NPaises}{`ls dados/*.csv | wc -l`}" > $@

paper/variaveis/paises.tex: code/lista_paises.py $(DADOS)
	python $< dados > $@

paper/paper.pdf: paper/paper.tex paper/referencias.bib $(FIGURAS) $(VARIAVEIS)
	tectonic -X compile $<
