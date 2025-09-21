#Tem como objetivo importar o nosso banco de dados no formato JSON. Isto é feito, pois uma vez que um arquivo
#é importado, o python não irá o importar novamente caso seja utilizado o import, diferentemente de se utilizarmos
#a abertura de arquivos. com a abertura de arquivos, o arquivo será aberto várias e várias vezes, até que o consumo de
#memória RAM se torne incontrolável

import json


with open(r"DB\localizador_funcoes\localizacao_funcoes.json", "r", encoding="utf-8") as f:  #Aqui estamos abrindo o noso banco de dados
    localizacao_funcoes = json.load(f) #localizacao_funcoes é a variável a qual será acessada posteriormente na importação
