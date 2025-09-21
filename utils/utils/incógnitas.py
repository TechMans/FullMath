from sympy import symbols, Eq, solve, sympify


#Regra para encontrar as funções e incógnitas de uma equação:

#"x + 10 + 15 + somar(20 + 17, 5) * c"


#Transformamos todos os sinais em espaços (incluindo as vírgulas)
#"x   10   15   somar(20   17  5)   c"

#Logo em seguida aplicamos o split nos espaços
#[ "x", "10", "15", "somar(20", "17", "5)" ]

#Removendo todos os números e caracteres especiais (exceto o "(" )
#[ "x", "somar(" ]

#A função será quem possuir o parênteses no final. Quem não o possuir, é uma incógnita

#print(separar_incógnitas_e_funções("x + 10 + 15 + somar(20 + 17, multiplicar(5, 2)) * c"))  #Utilize este caso para testes

def separar_incógnitas_e_funções(equação : str):

    for elemento in ["+", "-", "*", "/", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ",", ")"]: #Estes são todos os elementos que iremos transformar em espaço, seguindo a descrição acima
        equação = equação.replace(elemento, " ")

    equação = equação.split() #Agora iremos dividir a equação nestes espaços, ou seja, a única coisa que sobra agora é somente as incógnitas e as funções

    elementos = {   #Este é o dicionário que iremos retornar
        "incógnitas" : [],  #Este campo representa todas as incógnitas da equação
        "funções" : []  #E este campo todas as funções presentes na equação
    }

    for elemento in equação:  #A equação neste momento só possui as incógnitas e as funções, ou seja, na primeira repetição será atribuido a variável elemento ou uma função, ou uma incógnita

        if "(" in elemento:  #Se possuir este parêntese, então significa que estamos trabalhando com uma função

            elemento = elemento.replace("(", "") #Removêmos o parêntese, pois o mesmo não é mais necessário

            elementos["funções"].append(elemento)  #Adicionamos esta função ao campo de funções
        
        else: #Se não possuír este parêntese, então significa que trata-se de uma incógnita
            elementos["incógnitas"].append(elemento)  #Adicionando a nossa incógnita a lista de incógnitas

    return elementos  #Retornando o dicionário, o qual separa as incógnitas das funções

















