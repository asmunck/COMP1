'''Defina uma função que retorne o valor absoluto de um número fornecido. Observamos que Python provê uma função "abs" para esse fim. Faça a sua sem usá-la.
Para refletir: Compare o comportamento da sua função e da função "abs" do Python para diferentes tipos de dados numéricos, incluindo complexos. Há diferenças? Lembre-se de fazer com que a descrição da sua função mostre para que tipos numéricos ela funciona.'''

# Essa função retorna o valor absoluto de um número desde que ele seja inteiro ou flutuante. Diferente da função abs que engloba uma gama de números muito maiores e mais complexos.

def valor_absoluto(num):
    if num < 0:
        return -num
    else:
        return num

'''Defina uma função que retorne quantas (uma, duas ou nenhuma) são as raízes reais de uma equação de segundo grau, dados os valores dos três coeficientes.'''

# Essa função calcula o valor do discriminante 

def numero_raizes_reais(a, b, c):
    delta = b**2 - 4*a*c
    if delta > 0:
        return 2
    elif delta == 0:
        return 1
    else:
        return 0

'''Imagine que você quer enviar uma mensagem de felicitações e gostaria de repetir essas felicitações muitas vezes na mensagem. Algo do tipo "Feliz aniversário!! Feliz aniversário!! Feliz aniversário!! ..." até encher a tela do seu amigo. Você pode escrever uma vez e ir copiando e colando. Aí você percebe, lá no meio do caminho, que digitou errado... Ai! Agora que você sabe usar Python para fazer o trabalho para você, faça uma função que receba como entrada um texto e o número n de repetições desejado e retorne uma sequência de caracteres composta por n repetições deste texto. '''
def repetir_texto(texto, n):
    return texto * n
repetir_texto("Exemplo", 10)

'''Defina uma função em Python que receba como entrada três números inteiros representando, respectivamente, dia, mês e ano. Sua função deve retornar uma única sequência de caracteres com estas informações formatadas no padrão usual de notação de datas: "dia/mês/ano".'''
# Essa função recebe os três parâmetros como números inteiros e converte cada um deles para string, adicionando o caractere "/" entre cada um deles. 
def formatar_data(dia, mes, ano):
    data_formatada = str(dia) + '/' + str(mes) + '/' + str(ano)
    return data_formatada


"""6"""
# a) Uma função que calcule e retorne o valor do desconto de INSS de acordo com a tabela do INSS:
def inss(salario_bruto):
    if salario_bruto <= 2000:
        desconto = salario_bruto * 0.06
    elif salario_bruto <= 3000:
        desconto = salario_bruto * 0.08
    else:
        desconto = salario_bruto * 0.1
    return desconto

  
# b) Uma função que calcule e retorne o valor do desconto de IR de acordo com a tabela do IR:
def ir(salario_bruto):
    if salario_bruto <= 2500:
        desconto = salario_bruto * 0.11
    elif salario_bruto <= 5000:
        desconto = salario_bruto * 0.15
    else:
        desconto = salario_bruto * 0.22
    return desconto

# c) Uma função que calcule e retorne o salário líquido:
def salario_liquido(salario_bruto):
    desconto_inss = inss(salario_bruto)
    desconto_ir = ir(salario_bruto)
    salario_liquido = salario_bruto - desconto_inss - desconto_ir
    return salario_liquido
