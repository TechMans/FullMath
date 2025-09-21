from utils.utils.importer import importar

from DB.localizador_funcoes.importador_do_banco import localizacao_funcoes

from utils.utils.incógnitas import separar_incógnitas_e_funções

from utils.utils.DB.buscas import busca_por_semelhanca

from sympy import symbols, Eq, solve, sympify



def resolver_equação_simples(equação : str, limite_incógnitas = 1, **kwargs):   #Resolve uma equação simples, sem condições
    #**kwargs -> o valor de todas as incógnitas da equação. Todas devem ser informadas. em caso de valor desconhecido, deve ser utilizado None

    funções_nomes = separar_incógnitas_e_funções(equação)["funções"]  #Estamos obtendo somente a lista de funções, para que póssamos carregar todas as funções necessárias

    funções_numpy = {}  #Este dicionário irá armazenar as funções que o Numpy irá utilizar para os cálculos. Estrutura: {"nome_função" : função}

    for função_nome in funções_nomes:  #já encontramos todas as funções da incógnita, agora basta saber onde elas estão no banco de dados, qual é o caminho de acesso de cada uma
        resultados = busca_por_semelhanca(função_nome, localizacao_funcoes)  #realizamos a busca por aproximação. o values, é porque queremos somente a lista com os
        #caminhos. 

        nome_antigo = função_nome  #estamos salvando o nome antigo, pois utilizaremos esta informação para corrigir qualquer erro de digitação na equação

        função_nome = list(resultados.keys())[0]  #estamos obtendo o nome corrigido da função, caso estivesse errado
        função_caminho = list(resultados.values())[0]  #E aqui estamos obtendo o caminho para esta função

        função_código = importar(função_caminho, função_nome)  #será atribuido a função em si, como valor. import retornará a função diretamente

        funções_numpy.update({função_nome : função_código})   #Associando o nome da função com a função em si

        equação = equação.replace(nome_antigo, função_nome) #Estamos corrigindo todas as ocorrências da função antiga pela versão correta


    

    total_incógnitas = 0  #Esta variável representa o número total de incógneteas desconhecidas que foram passadas na equação

    for nome in kwargs.keys():  #Estamos obtendo a lista de nomes das variáveis que foram passadas via parâmetro 

        if kwargs[nome] == None:  #Estamos verificando se a variável possui valor None. Se sim, então esta será transformada em uma incógnita
            kwargs[nome] = symbols(nome) #Estamos criando uma incógnita com o nome da variável, e atribuindo esta incógnita ao respectivo campo que representa a variável
            total_incógnitas += 1   #criamos mais uma incógnita, e por isso adicionamos 1 a nossa variável contadora de incógnitas

        if total_incógnitas > limite_incógnitas:   #Estamos verificando se já criamos mais incógnitas que o limite definido
            return False   #Excedemos o limite, e por isso retornamos False



    # Criar um dict com todas as variáveis e funções que o sympify deve conhecer
    informações = {}

    informações.update(kwargs)  #Estamos adicionando todas as incógnitas conhecidas (as que possuem valor) e desconhecidas (as que são Symbol) ao dicionário
    informações.update(funções_numpy)   #E aqui todas as funções que o Numpy deve conhecer previamente
 

    lado1_equação, lado2_equação = equação.split("=")  #Aqui receberemos uma equação normal, com sinal de igual, e então a dividimos em dois lados


    lado1_equação = sympify(lado1_equação, locals=informações)  #Estamos transformando a equação no formato de string em uma equação simbólica Sympy
    lado2_equação = sympify(lado2_equação, locals=informações)  #lado1_equação = lado2_equação   é esta a separação que está sendo realizada


    equação = Eq(lado1_equação, lado2_equação)  #Estamos transformando as duas operações em equações realmente




    # Resolver
    resultados_equação = solve(equação, dict=True)   #Estamos obtendo uma lista de dicionários com todos os resultados para a equação.
    #[{c : 20}] como exemplo. O, nossa incógnita, é um Symbol, e não uma string. Precisamos converter para string para que póssamos acessar via indexação
   
    for resultado_equação in resultados_equação: #Estamos iterando sobre a lista de resultados

        for variável, resultado in resultado_equação.items():  #para cada resultado na equação, acessamos o nome da variável (representado pela variável "variável") e também o seu valor

            kwargs.update({str(variável) : resultado})  #Aqui convertemos todas as incógnitas do formato Symbol para o formato str
        
    return kwargs  #Retornamos o dicionário que representa o valor de cada uma das incógnitas da equação


#print(resolver_equação_simples("somar(a, b) = c", a = 10, b = None, c = 30)) #20      Caso de exemplo para testes