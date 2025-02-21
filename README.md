# Kit de sobrevivência digital para cientistas

Minicurso de 15h que ensina o uso de algumas ferramentas indispensáveis para
o kit de qualquer cientista que lida com dados.

**Autores:**
[Leonardo Uieda](https://www.leouieda.com/),
[Yago Moreira Castro](https://github.com/YagoMCastro),
[Arthur Siqueira de Macêdo](https://github.com/arthursmacedo)

| | Info |
|--:|:--|
| **Onde** | XXVII Escola de Verão de Geofísica do [IAG - USP](https://www.iag.usp.br/) |
| **Quando** | 17-21 de fevereiro de 2025 |
| **Instrutor** | [Leonardo Uieda](https://www.leouieda.com/) |
| **Monitores** | [Arthur Siqueira de Macêdo](https://github.com/arthursmacedo), [Yago Moreira Castro](https://github.com/YagoMCastro) |
| **Inscrições** | Até 2024-11-25: https://www.iag.usp.br/eventos/curso-extensao-escola-verao-2025 |

> Este curso foi desenvolvido como parte das atividades de Leonardo Uieda como
> Embaixador da
> [Rede Brasileira de Reprodutibilidade](https://www.reprodutibilidade.org/),
> uma iniciativa multidisciplinar para promoção de práticas de pesquisa
> transparentes e confiáveis na comunidade científica brasileira.

## Objetivos

Nosso principal objetivo é difundir o uso de ferramentas que nos auxiliam
a garantir a reprodutibilidade de nossos experimentos e análises
computacionais.
Para tanto, ensinaremos noções básicas de diversas ferramentas digitais
(shell/bash, git, GitHub, make, LaTeX) que podem poupar esforços e frustrações
de pesquisadores, alunos e profissionais que lidam com dados (amplamente
definido).
Além disso, o uso das ferramentas e práticas ensinadas pode potencializar sua
produtividade e a robustez de seus fluxos de trabalho.
A fluência no uso destas ferramentas também permitirá a colaboração em projetos
de software livre desenvolvidos pela comunidade.

## Pré-requisitos

Este curso tem como público alvo graduandos, pós-graduandos, pós-doutorandos
e profissionais atuantes das áreas de Geofísica, Geologia, Meteorologia,
Astronomia ou outras áreas correlatas das Ciências Exatas. Assim, os
pré-requisitos são:

* **Conhecimento básico de programação** (de preferência na linguagem Python):
  variáveis, funções, loops, criar gráficos. Os exemplos dados em aula
  utilizarão scripts e notebooks em Python mas não serão o foco das aulas.
* **Conhecimento básico de análise de dados**: regressão linear, médias, desvio
  padrão. Os exemplos dados em aula utilizarão alguns desses conceitos mas eles
  não serão o foco das aulas.

## Ementa

O curso tem como objetivo difundir o uso de algumas ferramentas computacionais
que têm o potencial de facilitar a vida de profissionais e cientistas que lidam
com dados e produção de textos técnicos e científicos. As ferramentas podem ser
utilizadas em diversos contextos: profissional, ensino, estudos, pesquisa,
extensão, etc.

O programa do curso será:

1. **Uso do terminal e de shell scripts:** Em qualquer sistema operacional,
   aprender a utilizar o terminal pode parecer arcaico mas pode ser
   extremamente eficaz para executar tarefas repetitivas e automatizar
   conjuntos de operações que são feitas com frequência. Aprender a navegar em
   um terminal e utilizar a linguagem Bash abrem portas para várias outras
   ferramentas úteis.
2. **Controle de versão e colaboração online com git e GitHub:** Sistemas de
   controle de versão, como o git, servem para rastrear mudanças feitas
   a conjuntos de arquivos. Se utilizadas de maneira correta, podem fornecer
   fontes de backup e a segurança para alterar o conteúdo de arquivos sem
   o medo de perder a versão original. Pareados com plataformas online, como
   o GitHub e GitLab, o uso desses sistemas permite a colaboração em projetos
   de software, websites e até mesmo artigos, livros e teses.
3. **Automatização de workflows com Make:** O programa Make é amplamente
   utilizado desde a década de 70 para automatizar fluxos de trabalho. O uso
   mais comum é para a compilação de códigos complexos, mas seu uso vai muito
   além disso. Com o Make, é possível automatizar tarefas comuns, como rodar
   scripts para produzir figuras, criar PDFs a partir de código LaTeX, etc.
4. **Criação de artigos, livros e teses com LaTeX:** O LaTeX é um "typesetting
   system", que transforma código em PDFs. Embora seja mais trabalhoso de
   aprender do que softwares como Word, o fato do texto ser escrito em forma de
   código possui diversas vantagens: o mesmo texto pode ser usado para gerar
   documentos com temas diferentes, facilidade na utilização de referências
   cruzadas, geração automática de bibliografia e citações, numeração
   automática de equações, figuras e capítulos, etc.

O formato do curso conterá:

* **Aulas expositivas:** Para ensinar uma ferramenta nova, o ministrante
  realizará uma demonstração ao vivo com os participantes seguindo em seus
  próprios computadores.
* **Exercícios:** Intercalado com as aulas expositivas, os participantes
  receberão pequenos desafios e exercícios para serem realizados
  individualmente e em grupos.
* **Aplicações:** O curso reservará parte do tempo para a aplicação das
  ferramentas ensinadas em problemas trazidos pelos participantes. Essas
  aplicações podem ser individuais ou compartilhadas com todos os
  participantes.

Ao final do curso, os participantes saberão como desenvolver projetos complexos
em equipe e com fluxos de trabalho automatizados para produção de resultados
e relatórios/teses/artigos de alta qualidade. As ferramentas aprendidas também
formam a base para melhorar a reprodutibilidade de resultados e para a prática
de Ciência Aberta.

## O material

Cada dia do curso teremos alguns produtos que iremos construir passo-a-passo.
Os códigos deste repositório são as versões finais do que iremos construir.
Estão presentes aqui para termos uma referência que possa ser utilizada por
quem precisar.

Ao final do curso, todos terão gerado um repositório para um artigo que contém
o código para análise dos dados, o código de um artigo LaTeX e um `Makefile`
que coordenada todo o workflow.
Um exemplo de tal repositório é: https://github.com/leouieda/kit-exemplo-2025-02

Como exemplo, utilizamos dados de médias de temperatura média mensal para
diversos países. Os dados estão disponíveis
https://github.com/compgeolab/temperature-data sob uma licença CC-BY-NC.
Estes dados foram derivados dos dados produzidos pelo
[Berkeley Earth](https://berkeleyearth.org/) que também estão disponíveis sob
a licença CC-BY-NC.

## Instalando os softwares no seu computador

**Siga as instruções em [INSTALL.md](INSTALL.md)** para instalar os softwares
que utilizaremos durante o curso no seu computador.

## Cronograma

> O cronograma a seguir é um **esboço** e está **sujeito a mudanças** até a data do curso.

### Dia 1 - O terminal e scripts em Bash

* Introdução ao curso
* O terminal e a linguagem Bash
* Navegando pelo terminal: Diretórios, caminhos, e arquivos (comandos `cd`, `ls`, `pwd`)
* Manipulando arquivos e diretórios (comandos `cp`, `mkdir`, `mv`, `rm` e uso de wildcards)
* Redirecionamento de saída e entrada (comandos `cat`, `wc`, `head`, `sort`)
* Exemplo: Calculando o número de arquivos de dados que temos.
* Loops com `for`
* Exemplo: Calculando o número de dados em cada arquivo.
* Exemplo: Rodando a análise da variação de temperatura para cada arquivo.

### Dia 2 - Controle de versão com git e GitHub

* Para que servem sistemas de controle de versão
* Configurando o git (comando `git config`)
* Criando um repositório (comando `git init`)
* Populando o repositório  e rastreando mudanças (comandos `git add`, `git
  status`, `git commit`)
* Explorando o histórico de mudanças (comandos `git diff`, `git log`, `git
  checkout`)
* Cópias remotas do repositório no GitHub (comandos `git remote`, `git push`,
  `git pull` e chaves SSH de acesso)
* Adicionando arquivos `README.md` para documentar seu repositório
* Exemplo: Criando um repositório para nosso artigo de variações de temperatura

Caso dê tempo:

* Colaborando com outras pessoas (comandos `git branch`, `git switch`, `git
  merge` + forks e pull requests)
* Resolvendo conflitos
* Exemplo: Adicione seu nome como coautor do artigo em outro repositório

### Dia 3 - Automatização de tarefas com GNU Make

* O problema de dependências em fluxos de trabalho
* A estrutura geram de um `Makefile`: alvo, requisitos e comandos
* O que acontece quando requisitos são atualizados
* Criando alvos "phony"/fictícios: `all`, `clean`
* Exemplo: Criando alvos para nossa análise de temperaturas

### Dia 4 - Escrita científica com LaTeX

* LaTeX vs Word, qual é a diferença?
* Estrutura básica de um documento LaTeX: cabeçalho e corpo
* Usando o comando `\documentclass`
* Compilando um documento com o `tectonic`
* Configurando o idioma com o pacote `babel`
* Adicionando título e autores com `\title`, `\author` e `\maketitle`
* Criando seções com `\section`
* Adicionando citações com Bibtex e o pacote `natbib`
* Obtendo referências em formato Bibtex com https://www.doi2bib.org
* Incluindo figuras com o pacote `graphicx`
* Criando variáveis com `\newcommand` e inserindo resultados no seu documento

### Dia 5 - Projetos individuais

O último dia estará reservado para que participantes tragam seus próprios
projetos (artigos, dissertações, monografias, etc) aos quais desejem aplicar os
conhecimentos adquiridos ao longo do curso. O instrutor e os monitores
auxiliarão na implementação. Participantes que não tiverem projetos podem
auxiliar em projetos de outras pessoas ou o instrutor pode sugerir algum
projeto.

## Bibliografia

O material abaixo complementa e expande o que veremos em aula:

> Recomendamos que todos leiam o material antes das aulas e que os estudem
> a fundo depois das aulas para fixar o conteúdo.

* [Lição de Bash do Software Carpentry](https://swcarpentry.github.io/shell-novice)
* [Lição de Git do Software Carpentry](https://swcarpentry.github.io/git-novice)
* [Lição de Make do Software Carpentry](https://swcarpentry.github.io/make-novice)
* [Documentação de LaTeX do Overleaf](https://www.overleaf.com/learn)
* [Lição de Python do Software Carpentry](https://swcarpentry.github.io/python-novice-inflammation)

Além disso, aqui estão mais alguns links para videos e exemplos que vão te
ajudar no dia-a-dia de um cientista digital:

* [How to name files - Jennifer Bryan](https://www.youtube.com/watch?v=ES1LTlnpLMk).
  Provavelmente o vídeo mais útil já feito para qualquer pessoa que trabalha
  com dados. Vários outros videos da [NormConf](https://www.youtube.com/@normconf)
  valem a pena também.
* [Pooch](https://www.fatiando.org/pooch/latest/). Ferramenta em Python para
  baixar dados. Muito útil para lidar com workflows envolvendo dados públicos.
* [Exemplo de artigo feito nos modelos do curso](https://github.com/compgeolab/euler-inversion).
  Infelizmente, esse artigo usava Jupyter notebooks e eles não funcionam bem
  com o Make (Leo: Sinceramente, provavelmente vou voltar para scripts `.py` no
  próximo artigo mesmo depois de 13 anos com o Jupyter). Feito com base no
  [template de artigos do CompGeoLab](https://github.com/compgeolab/paper-template).
* [Exemplo de tese feita em LaTeX](https://github.com/santisoler/phd-thesis).
  Tese do [Santiago Soler](https://www.santisoler.com/) com ótimo design
  e várias boas práticas de LaTeX.
* [Exemplo de memorial acadêmico para concurso feito em LaTeX](https://github.com/leouieda/memorial2023).
  Memorial escrito pelo Leo para o concurso de professor do IAG em 2023.
  Utiliza estilo customizado com detalhes gráficos.
* [Exemplo de CV feito em LaTeX](https://github.com/leouieda/cv).
  Currículo resumido do Leo em formato relativamente simples e limpo.
* [Template para projetos de pesquisa em LaTeX](https://github.com/compgeolab/grant-fapesp-template).
  Baseada no modelo de projetos da FAPESP mas pode ser adaptada para outras
  agências de fomento.
* [Tutorial de como escolher o tamanho de figuras](https://duetosymmetry.com/code/latex-mpl-fig-tips/).
  Explica como calcular o tamanho da figura que é gerada pelo código para
  que a fonte da figura seja exatamente do mesmo tamanho que a fonte do
  texto quando inserida no LaTeX.

Para os interessados e mais material tangencial ao curso:

* [Python Challenge](http://www.pythonchallenge.com/). Teste suas habilidades
  e aprenda como fazer várias coisas com Python que são muito úteis quando
  lidamos com dados.
* [Learn Vim Progressively](https://yannesposito.com/Scratch/en/blog/Learn-Vim-Progressively/).
  Guia de como aprender a usar o editor de texto Vim. Recomendo instalar
  o [NeoVim](https://neovim.io/) que é uma versão mais moderna e compatível com
  o Vim clássico.
* [Choose a License](https://choosealicense.com/). Guia de como escolher e usar
  licenças abertas quando você compartilha código e material online.

## Licença

O conteúdo deste curso pode ser livremente utilizado e adaptado dentro das
restrições estabelecidas pelas licenças [MIT](LICENSE-MIT.md)
e [CC-BY](LICENSE-CC-BY.md). Por favor, dê atribuição aos autores e inclua um
link para esse repositório quando utilizar esse material.

* O código fonte LaTeX, Python, Bash e Makefile são distribuídos segundo a
  licença de software livre [MIT](LICENSE-MIT.md).
* O texto da fonte LaTeX e dos arquivos Markdown (`*.md`) são distribuídos
  segundo a licença [Creative Commons Attribution (CC-BY)](LICENSE-CC-BY.md).
