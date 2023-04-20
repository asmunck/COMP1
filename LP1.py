# Calculos Geométricos
#1. Defina uma função que calcule a  área de um retângulo dados seus dois lados. Teste pelo menos para os
# seguintes pares de entrada:
# 5 e 7; resposta esperada é 35
# 15 e 2; resposta esperada é 30
# 500 e 700; resposta esperada é 350000
#
def geocalc(a,b):
  return a * b

geocalc(5,7)
geocalc(15,2)
geocalc(500,700)

# 2. Defina uma função que calcule a área da superfície de um cubo que tem c por aresta.
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
  
# 4. Definir uma função que calcule uma média de dois números.
def parescalc(a,b):
  return (a + b) / 2
parescalc(-5,7)
parescalc(2, -2)
parescalc(5, 5)
parescalc(3, 4)
parescalc(3.0, 4.0)

# 5. Defina uma função que calcule a ordenada de uma função de segundo grau dado os parâmetros a, b, c e a abscissa.
def calcular_ordenada_segundo_grau(a, b, c, x):
    y = a * x**2 + b * x + c
    return y

# 6. Defina uma função que calcule a média de dois números com seus respectivos pesos.
def calcular_media_ponderada(numero1, peso1, numero2, peso2):
    media_ponderada = (numero1 * peso1 + numero2 * peso2) / (peso1 + peso2)
    return media_ponderada
  
# 7. Defina uma função qu calcule o erro entre a soma de uma PG infinita.
def erro_pg_inifinita(q, n):
    if q < 0 or q >= 1:
        return "q deve estar entre 0 e 1."
    soma_n_termos = (1 - q**n)/(1 - q)
    soma_infinita = 1/(1 - q)
    erro = abs(soma_infinita - soma_n_termos)
    return erro

  
# 8. Defina uma função para calcular a gorjeta do garçom com base no valor da conta (15% fixo).
def calcular_gorjeta_fixa(valor_conta):
    gorjeta = 0.15 * valor_conta
    return gorjeta

# 9. Defina uma função para calcular a gorjeta do garçom com base no valor da conta e na porcentagem de gorjeta informada.
def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = porcentagem_gorjeta * valor_conta / 100
    return gorjeta

# 10. Defina uma função para calcular o saldo final de uma conta com base no saldo inicial, número de meses e taxa de juros mensal (juros simples).
def calcular_saldo_final(saldo_inicial, num_meses, taxa_juros_mensal):
    saldo_final = saldo_inicial + (saldo_inicial * taxa_juros_mensal * num_meses)
    return saldo_final

# 11. Função para calcular o saldo final de uma conta com base no saldo inicial, número de meses e taxa de juros mensal (juros simples).
def calcular_saldo_final(saldo_inicial, num_meses, taxa_juros_mensal):
    saldo_final = saldo_inicial + (saldo_inicial * taxa_juros_mensal * num_meses)
    return saldo_final

# 12. Definir uma função que calcule a distância na qual a correnteza arrasta um barco que atravessa o rio.
import math

def calcular_distancia_correnteza(velocidade_correnteza, largura_rio, velocidade_barco):
    # Converter a velocidade do barco para m/s
    velocidade_barco_m_s = velocidade_barco / 3.6

    # Calcular o tempo necessário para atravessar o rio
    tempo_travessia = largura_rio / velocidade_barco_m_s

    # Calcular a distância arrastada pela correnteza (hipotenusa do triângulo retângulo)
    distancia_correnteza = velocidade_correnteza * tempo_travessia

    return distancia_correnteza
