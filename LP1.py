# Calculos Geométricos
#1. Defina uma função que calcule a  área de um retângulo dados seus dois lados. Teste pelo menos para os
# seguintes pares de entrada:
• 5 e 7; resposta esperada  ́e 35
• 15 e 2; resposta esperada  ́e 30
• 500 e 700; resposta esperada  ́e 350000
#
def geocalc(a,b):
  return a * b

geocalc(5,7)
geocalc(15,2)
geocalc(500,700)

# 2. Defina uma função que calcule a área da superfície de um cubo que tem c por aresta.'''
def areacubo(c):
  return c ** 2

areacubo()

# 3. Defina uma função que calcula a área da coroa circular com base em dois raios, r1 e r2, onde r1 é o raio externo e r2 é o raio interno:
def calcular_area_coroa_circular(r1, r2):
    if r1 <= r2:
        return "Erro: r1 deve ser maior do que r2."
    else:
        pi = 3.14
        area_coroa_circular = pi * (r1**2 - r2**2)
        return area_coroa_circular
      
calcular_area_coroa_circular(2, 1)
calcular_area_coroa_circular(15, 5)
calcular_area_coroa_circular(100, 0)
  
# 4. 
def parescalc(a,b):
  return (a + b) / 2
parescalc(-5,7)
parescalc(2, -2)
parescalc(5, 5)
parescalc(3, 4)
parescalc(3.0, 4.0)

# 5.
def calcular_ordenada_segundo_grau(a, b, c, x):
    y = a * x**2 + b * x + c
    return y

# 6.
def calcular_media_ponderada(numero1, peso1, numero2, peso2):
    # Calcula a média ponderada utilizando a fórmula (numero1 * peso1 + numero2 * peso2) / (peso1 + peso2)
    media_ponderada = (numero1 * peso1 + numero2 * peso2) / (peso1 + peso2)
    return media_ponderada

  # Função para calcular a gorjeta do garçom com base no valor da conta (15% fixo)
def calcular_gorjeta_fixa(valor_conta):
    gorjeta = 0.15 * valor_conta
    return gorjeta

# Função para calcular a gorjeta do garçom com base no valor da conta e na porcentagem de gorjeta informada
def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = porcentagem_gorjeta * valor_conta / 100
    return gorjeta

# Função para calcular o saldo final de uma conta com base no saldo inicial, número de meses e taxa de juros mensal (juros simples)
def calcular_saldo_final(saldo_inicial, num_meses, taxa_juros_mensal):
    saldo_final = saldo_inicial + (saldo_inicial * taxa_juros_mensal * num_meses)
    return saldo_final

