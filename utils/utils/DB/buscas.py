#Neste arquivo estarão presentes todas as funções de busca para nosso banco de dados


import difflib

#Esta função tem como objetivo realizar buscas via aproximação. Ex.: alvo -> "area_quadado" -> resultado "área_quadrado"
#é um corretor de texto, porém com correção para as chaves primárias de nosso banco de dados

#alvo: é o que queremos encontrar no banco de dados. Ex.: "area_quadado". A função irá retornar o valor associado a essa chave
# db: é o banco de dados no qual será realizada a busca
# total_resultados: Qual é o número limite de resultados aproximados se deseja obter? por padrão será 1
def busca_por_semelhanca(alvo : str, db : dict, total_resultados = 1):

    chaves = db.keys()  #Estamos obtendo a lista de chaves do nosso banco de dados. Este será o nosso "vocabulário" para correção

    possíveis_resultados : list[str] = difflib.get_close_matches(alvo, chaves, n=total_resultados) #função da biblioteca difflib a qual compara uma string com um conjunto de strings
    #sendo o alvo a nossa string, e chaves o conjunto de strings. n representa o número máximo de resultados que podem ser ordenados. 

    resultado = {} #Este dicionário irá armazenar o resultado de nossa busca. 

    for possível_resultado in possíveis_resultados:  #Este for percorre cada um dos resultados de nossa correção

        resultado.update({possível_resultado : db[possível_resultado]})  #O objetivo deste dicionário é armazenar a correção associada ao respecitivo valor
        #no banco de dados. É uma extração, estamos extraindo uma parte do banco de dados e adicionando a este dicionário.

    return resultado #devolvemos o trecho "copiado" do banco de dados para o usuário



