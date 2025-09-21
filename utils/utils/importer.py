#Tem como objetivo importar qualquer função / objeto de qualquer módulo dinamicamente

import importlib

#Caminho: O caminho até o módulo  Ex.: "utils.matematica.formulas.geometria.plana.others"
#alvo: o que será importado deste módulo   Ex.: "Pythagoran_theorem"

def importar(caminho : str, alvo : str):

    modulo = importlib.import_module(caminho) #Estamos acessando a função a qual nos permite importar um módulo somente através de seu caminho

    return getattr(modulo, alvo)  #nos é retornado um objeto. Utilizamos a função getattr para acessarmos o que queremos, seja uma função, constante ou objeto, todos eles serão atributos deste objeto


#Exemplo de uso
#função = importar("utils.matematica.Formulas.Geometria.Plana.others", "exibir")

#função()

#IMPORTANTE: O caminho é sempre relativo a quem está executando o código, e não ao local de armazenamento deste arquivo .py específico