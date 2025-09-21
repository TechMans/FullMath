# Estrutura de arquivos e diretórios do projeto

O projeto é dividido em 6 diretórios na raiz do projeto, sendo eles:

## .venv

Este é um diretório do próprio python, dedicado ao armazenamento de dependências de código, e também do próprio python

## Back_End

Este projeto é uma parte de um MonoRepo, ou seja, na pasta Back_end estão partes de código muito específicas deste projeto, ou seja, não podem ser aproveitados em outros projetos.

## DB

Neste diretório está localizado todo o banco de dados do projeto

### localizacao_funcoes.json

O objetivo deste JSON é guardar a localização de cada uma das funções matemáticas, físicas e financeiras do projeto, para que possam ser importadas dinamicamente, permitindo assim que as funções sejam acessadas de forma arbitrária, porém sem a necessidade de utilizar comandos perigosos, como o exec, o qual poderia criar a função em runtime.

## Doc

Este é o diretório em que você está agora. Aqui são armazenadas todas as informações referentes a documentação do projeto, mas não necessariamente toda a documentação está aqui. A documentação dos códigos, muitas vezes estará no próprio código.

## Front_End

Neste diretório estarão todas as páginas de nosso APP, tudo o que é voltado para interface.

### Global_CSS

Neste diretório serão armazenados arquivos CSS que podem ser válidos para mais de uma página, como um estilo de um elemento (Gradiente etc.)

### Global_JS

Arquivos JS que podem valer para várias páginas, como alternar entre arquivos utilizando uma guia.

### Global_Templates

Esta será a nossa forma de tornar o HTML dinâmico. Serão trechos de HTML-CSS-JS já prontos, e que poderão ser adicionados a qualquer página. O conteúdo do arquivo é carregado, via função do back end, e enviado para o JS, para que então possa renderizar o conteúdo do arquivo na respectiva página.

### Paginas

Neste diretório serão armazenadas as páginas do projeto, com HTML-CSS-JS

#### Calculadora

neste diretório será armazenada a página da calculadora do projeto.

#### Conversor
neste diretório será armazenada a página do conversor do projeto. O conversor poderá converter bases numéricas, como de decimal para binário, binário para hexadecimal etc. Assim como tabmém poderá converter para medidas, como M/S para Km/H, litro para metro cúbico, e assim por diante.

### Funcoes

neste diretório será armazenada a página da seção de funções do projeto, onde poderemos analisar o gráfico de uma função, o valor de cada incógnita, suas propriedades etc.

### Pagina_inicial

Esta será a página inicial do projeto, o hub principal, onde estarão os arquivos recentes, uma seção para criar novos arquivos etc.

### Geometria

Esta seção é dividida em duas outras sub seções, uma para geometria 2d, e a outra para geometria 3d


## Utils

Dentro do diretório Utils é onde serão armazenadas classes e funções que podem ser utilizadas em outros projetos, uma vez que este é um MonoRepo. O diretório utils se divide em vários módulos menores, como financas, fisicas, matematica e utils.

### utils

Este utils dentro do diretório utils, são funções e classes genéricas que podem ser utilizadas dentro do diretório utils. Isso é util, pois evita referência circular e uma teia de aranha sem fim de ligação entre módulos. Desta forma, um módulo nunca chama ao outro, o único módulo que pode ser chamado por outro módulo, é somente o utils, porém o utils nunca deve chamar nenhum outro módulo, exceto o módulo DB. Este pode ser chamado por qualquer um.

### financas

Este módulo possui várias e várias fórmulas financeiras, como valor futuro, valor presente, juros etc. 

### fisica

Este módulo possui várias e várias fórmulas físicas, como velocidade média etc. A fins de organização, as fórmulas físicas foram separas em módulos, como Eletricidade, Eletromagnetismo etc.

### Matematica

Este módulo possui várias e várias fórmulas matemáticas, como velocidade média etc. A fins de organização, as fórmulas matemáticas foram separas em módulos, como Funções, Geometria etc.

## Main.py

Este é o arquivo principal do projeto, o arquivo que inicializa o projeto. A execução do projeto sempre deve ser realizada através dele.