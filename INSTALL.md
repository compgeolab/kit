# Instalando os softwares no seu computador

Durante o curso, utilizaremos alguns softwares para acessar o `git`, `make`,
`python` e LaTex:

* **Git:** O `git` já vem com a maioria dos sistemas Linux. No Windows,
  utilizaremos o [Git for Windows](https://gitforwindows.org/) que já vem com
  um terminal com Bash (que é muito melhor que o `cmd.exe`).
* **Miniforge:** Para acessar o Python, utilizaremos a distribuição
  [Miniforge](https://conda-forge.org/download/). Ela é melhor que o Anaconda
  pois vem somente com o Python e o programa `conda` que é utilizado para
  instalar outros pacotes. Assim, fica mais fácil instalar novos pacotes
  e atualizá-los sem ter conflitos entre versões, como acontece rotineiramente
  no Anaconda. O Miniforge também é o jeito mais fácil de instalar o `make`
  e o compilador de LaTeX `tectonic` no Windows.
* **Tectonic:** Existem diversos compiladores de LaTeX para as diferentes
  plataformas. A maioria costuma ser grande e difícil de instalar,
  principalmente no Windows.
  O [Tectonic](https://tectonic-typesetting.github.io/en-US/) é um compilador
  novo de LaTeX que é fácil de instalar pelo Miniforge e mais fácil de rodar
  que os outros compiladores de LaTeX.

**Siga as instruções abaixo para instalá-los corretamente!**

## Windows

### 1. Editor de texto

Baixe e instale um editor de texto, como
[VSCode](https://code.visualstudio.com/) ou
[Notepad++](https://notepad-plus-plus.org/).
Utilize o que achar melhor. Durante o curso utilizaremos o Notepad++ pois
é simples e já está instalado nos computadores da sala.
**Instale o editor de texto primeiro!**

### 2. Git e um terminal

1. Baixe o [Git for Windows](https://gitforwindows.org/). Ele te dará um
   terminal com Bash e Git instalados.
1. Durante a instalação, siga os passos com a configuração padrão **exceto**:
    1. Na parte "Choosing the default editor used by Git": Selecione o seu
       editor de texto no menu.

       ![](img/git-windows-1.png)

    1. Na parte "Adjusting the name of the initial branch in new repositories":
       Selecione "Override the default branch name for new repositories"

       ![](img/git-windows-2.png)

    1. Na parte "Configuring the terminal emulator to use with Git Bash":
       Selecione "Use Windows' default console window"

       ![](img/git-windows-3.png)

Ao final, você terá acesso ao programa "Git Bash" que te fornecerá um terminal
com a linguagem Bash e o programa Git instalado.

### 3. Miniforge

1. Baixe o [Miniforge](https://conda-forge.org/download/) para Windows.
1. Durante a instalação, siga os passos com a configuração padrão **exceto**:
    1. Na parte "Advanced installation options": Selecione "Add Miniforge3 to
       my PATH environment variable".

       ![](img/miniforge-1.png)

Ao final, você poderá usar os comandos `python` e `conda` no terminal do Git
Bash.

### 4. Make, Tectonic e outros

1. Abra o Git Bash.
1. Digite `conda install -y make tectonic numpy pandas matplotlib` e aperte
   *Enter*.
   Isso deve baixar e instalar o programa `make`, o Tectonic e as bibliotecas
   de Python que iremos utilizar.

## Linux

Na maioria dos sistemas Linux você já terá um terminal com Bash, `make` e o Git
instalados. Caso seja necessário, instale um editor de texto também, embora
a maioria das distribuições já venha com um.

1. Baixe e instale o [Miniforge](https://github.com/conda-forge/miniforge). Ele
   te dará o Python e o gerenciador de software `conda` que utilizaremos para
   instalar o LaTeX. Siga os passos do instalador para colocar as coisas no seu
   `PATH`.
1. Rode o comando `conda install -y tectonic numpy pandas matplotlib` no
   terminal após instalar o Miniforge.
   Isso deve baixar e instalar o Tectonic e as bibliotecas de Python que iremos
   utilizar.

