from sympy import symbols, Eq, solve


def triangulo_retangulo(precisão, área = None, largura = None, h = None):
    """
Resolve a icógnetea a qual representa a área do triângulo retângulo, podendo assim encontrar qualquer valor.
Todos os parâmetros da equação, como área, largura etc. devem ser informados. O limite é de apenas um único parâmetro o qual poderá ser ignorado

Args:
    precisão (int): O número máximo de casas decimais que o resultado deve possuir.
    area (float): Um valor que representa a área do triângulo retângulo
    largura (float): Um valor que representa a largura do triângulo retângulo
    h (float): Um valor que representa a altura do triângulo retângulo

Returns:
    List|bool: Lista com as soluções encontradas ou False caso algum parâmetro não tenha sido passado corretamente.
    """

    total_incógnitas = 0  #Esta variável representa o número total de incógneteas desconhecidas que foram passadas na equação

    if área is None:  #Se a área for None, isso significa que o valor padrão do parâmetro se manteve o mesmo, logo o valor da área não foi
        #informado, ou seja, área é uma incógnita

        área = symbols("área")  #Aqui estamos criando a incógnita área e atribuindo ela a variável área
        incógnita = área  #Estamos atribuindo a incógnita a esta variável, e em todos os outros ifs, pois é necessário informar com qual incógnita
        #iremos trabalhar, ou seja, qual queremos encontrar. 
        total_incógnitas += 1  #Estamos contando o total de incógnitas. O número limite varia de equação para equação, mas no geral é 1

    if largura is None:
        largura = symbols("área")
        incógnita = largura
        total_incógnitas += 1

    if h is None:
        h = symbols("área")
        incógnita = largura
        total_incógnitas += 1

    





x = symbols('x')

# Criar a equação x^2 - 4 = 0
equacao = Eq(x**2 - 4, 0)

print(equacao)  # x**2 - 4 = 0